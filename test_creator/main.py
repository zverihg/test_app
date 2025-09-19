#!/usr/bin/env python

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys, os
from PyQt5 import QtWidgets
from Ui_main import Ui_MainWindow
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Column, Integer, String, Boolean, MetaData, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from datetime import datetime as dt

from enum import Enum

metadata = MetaData()
engine = create_engine('sqlite:///dbname.db')
Base = declarative_base()

class TypeTest(Enum):

    instructions_DPCH_PDT = "Инструкции по ДПЧ и ПДТ"
    dezh_po_parku = "Дежурный по парку"
    dezh_po_UBM = "Дежурный по УБМ"

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    completedtests = relationship("CompletedTest", back_populates="users")

class CompletedTest(Base):
    __tablename__ = 'completedtests'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    test_type = Column(String)
    test_date = Column(DateTime, default=dt.now)
    total_time = Column(String)
    right_ans_qty = Column(Integer)
    description = Column(String)
    users = relationship("User", back_populates="completedtests")
    completedquestions = relationship("CompletedQuestion", back_populates="completedtests")
    grade = Column(Integer)

class CompletedQuestion(Base):
    __tablename__ = 'completedquestions'
    id = Column(Integer, primary_key=True)
    test_id = Column(Integer, ForeignKey("completedtests.id"))
    text = Column(String)
    result = Column(Boolean, default=False)
    completedanswers = relationship("CompletedAnswer", back_populates="completedquestions")
    completedtests = relationship("CompletedTest", back_populates="completedquestions")

class CompletedAnswer(Base):
    __tablename__ = 'completedanswers'
    id = Column(Integer, primary_key=True)
    ans_id = Column(Integer)
    question_id = Column(Integer, ForeignKey("completedquestions.id"))
    text = Column(String)
    is_correct = Column(Boolean, default=False)
    choosen = Column(Boolean, default=False)
    completedquestions = relationship("CompletedQuestion", back_populates="completedanswers")

class Question(Base):

    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    answers = relationship("Answer", back_populates="question")
    question_type = Column(String)

class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    ans_id = Column(Integer)
    question_id = Column(Integer, ForeignKey("questions.id"))
    text = Column(String)
    is_correct = Column(Boolean)
    question = relationship("Question", back_populates="answers")


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

class MainWindow(QtWidgets.QMainWindow):

    ans_lst:dict = {}
    chooses_lst:dict = {}
    active_type:TypeTest = TypeTest.instructions_DPCH_PDT.name
    ids_question:dict = {}
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Конфигуратор тестов')
        self.setWindowIcon(QIcon(self._resource_path('i.png')))

        self.ans_lst = { '1':self.ui.answer_1, '2':self.ui.answer_2, '3':self.ui.answer_3, '4':self.ui.answer_4,}
        self.chooses_lst = { '1':self.ui.choose_1, '2':self.ui.choose_2, '3':self.ui.choose_3,'4':self.ui.choose_4,}

        self.set_question_list_gui()
        self.ui.save_curent_question.clicked.connect(self.save_question)
        self.ui.list_questions.clicked.connect(self.clicked_on_row)
        self.ui.add_new_question.clicked.connect(self.add_new_question)
        self.ui.delete_curent_question.clicked.connect(self.del_question)

        self.ui.choose_type_question.addItems(["ДПЧ, ПДПЧ, ПДТ", "Дежурный по парку", "Дежурный по УБМ"])
        self.ui.choose_type_question.currentTextChanged.connect(self._change_test)

    def _change_test(self):

        test = self.ui.choose_type_question.currentText()

        if test == "ДПЧ, ПДПЧ, ПДТ":
            self.active_type = TypeTest.instructions_DPCH_PDT.name
        elif test == "Дежурный по парку":
            self.active_type = TypeTest.dezh_po_parku.name
        elif test == "Дежурный по УБМ":
            self.active_type = TypeTest.dezh_po_UBM.name
        else: pass

        self.set_question_list_gui()

    def _resource_path(self, relative_path):
        base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def del_question(self):

        idx_gui_quest = int(self.ui.list_questions.currentItem().text().replace("Вопрос ", ""))
        idx_quest = self.ids_question[idx_gui_quest]
        question = session.query(Question).filter_by(id=idx_quest).delete()
        session.commit()
        self.set_question_list_gui()

    def add_new_question(self):

        idx = str(len(self.ids_question)+1)
 
        self.ui.list_questions.addItem(f"Вопрос {idx}")

        question = Question(text="введи сюда вопрос", question_type=self.active_type,
                            answers=[
                                Answer(text="введи сюда ответ", ans_id = 1, is_correct = False),
                                Answer(text="введи сюда ответ", ans_id = 2, is_correct = False),
                                Answer(text="введи сюда ответ", ans_id = 3, is_correct = False),
                                Answer(text="введи сюда ответ", ans_id = 4, is_correct = False)
                            ]
                            )
        session.add(question)
        session.commit()

        question = session.query(Question).filter_by(question_type=self.active_type).order_by(Question.id.desc()).first()

        self.ids_question[int(idx)] = question.id

        print(question.id)

    def clicked_on_row(self):

        for itm in self.chooses_lst.values(): itm.setChecked(False)
        for itm in self.ans_lst.values(): itm.setText("")
        idx_gui_quest = int(self.ui.list_questions.currentItem().text().replace("Вопрос ", ""))

        idx_quest = self.ids_question[idx_gui_quest]

        question = session.query(Question).filter_by(id = idx_quest).first()
        self.ui.test_question.setText(question.text)

        for answer in question.answers:
            self.ans_lst[str(answer.ans_id)].setText(answer.text)
            if answer.is_correct:
                self.chooses_lst[str(answer.ans_id)].setChecked(True)

    def set_question_list_gui(self):

        for itm in self.chooses_lst.values(): itm.setChecked(False)
        for itm in self.ans_lst.values(): itm.setText("")
        self.ui.test_question.setText('')
        self.ui.list_questions.clear()

        questions = session.query(Question).filter_by(question_type=self.active_type).count()

        if not questions:
            question = Question(text="введи сюда вопрос", question_type=self.active_type,
                                answers=[
                                    Answer(text="введи сюда ответ", ans_id = 1, is_correct = False),
                                    Answer(text="введи сюда ответ", ans_id = 2, is_correct = False),
                                    Answer(text="введи сюда ответ", ans_id = 3, is_correct = False),
                                    Answer(text="введи сюда ответ", ans_id = 4, is_correct = False)
                                ]
                                )
            session.add(question)
            session.commit()

        questions = session.query(Question).filter_by(question_type=self.active_type).all()

        for idx, question in enumerate(questions):
            self.ui.list_questions.addItem(f"Вопрос {idx+1}")
            self.ids_question[idx+1] = question.id

        item = self.ui.list_questions.item(0)
        self.ui.list_questions.setCurrentItem(item)

    def save_question(self):

        if self.ui.list_questions.currentItem():

            answers = {
                '1':self.ui.answer_1.toPlainText(),
                '2':self.ui.answer_2.toPlainText(),
                '3':self.ui.answer_3.toPlainText(),
                '4':self.ui.answer_4.toPlainText()
            }

            for answer in answers.values():
                if not answer:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setInformativeText('Все поля должны быть заполнены')
                    msg.exec_()
                    return 0

            chooses = {
                '1':self.ui.choose_1.checkState(),
                '2':self.ui.choose_2.checkState(),
                '3':self.ui.choose_3.checkState(),
                '4':self.ui.choose_4.checkState(),
            }

            right_answers = []

            for idx, val in chooses.items():
                if val: right_answers.append(idx)

            if not right_answers:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setInformativeText('Выберите хотябы один правильный ответ')
                msg.exec_()
                return 0

            if not self.ui.test_question.text():
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setInformativeText('Все поля должны быть заполнены')
                msg.exec_()
                return 0

            id_question = int(self.ui.list_questions.currentItem().text().replace('Вопрос ',''))

            idx = self.ids_question[id_question]

            question = session.query(Question).filter_by(id = idx).first()
            question.text = self.ui.test_question.text()

            question.answers[0].text = answers["1"]
            question.answers[1].text = answers["2"]
            question.answers[2].text = answers["3"]
            question.answers[3].text = answers["4"]

            for ans in question.answers:
                if str(ans.ans_id) in right_answers:
                    ans.is_correct = True
                else: 
                    ans.is_correct = False

            session.commit()

        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('Выберите вопрос из списка')
            msg.exec_()

app = QtWidgets.QApplication(sys.argv)
graf = MainWindow()
graf.show()

sys.exit(app.exec_())
