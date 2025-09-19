#!/usr/bin/env python

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import json
from datetime import datetime as dt
from Ui_admin import Ui_MainWindow
from threading import Thread
from question_gui import Question_gui, Status
from time import sleep
from random import sample
from fpdf import FPDF
from enum import Enum
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Column, Integer, String, Boolean, MetaData, Date, Time, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

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

class QuestionPool():
    id_question:str
    question:str
    answers:dict
    right_answers:list
    choosen_var:list = []
    answer_result:bool = False

    def __init__(self, data):

        self.id_question = data['id_question']
        self.question = data['question']
        self.answers = data['answers']
        self.right_answers = data['right_answers']
        self.choosen_var = data['choosen_var']
        self.answer_result = data['answer_result']

class Actual_test(Enum):
    pomdezh_po_chasti = "Помошник дежурного по части"
    instructions_DPCH_PDT = "Инструкции по ДПЧ и ПДТ"
    dezh_po_parku = "Дежурный по парку"
    dezh_po_chasti = "Дежурный по части"
    dezh_po_UBM = "Дежурный по УБМ"

class ThereadStatus(Enum):
    run = "run"
    stop = "stop"
    end = "end"
    timeout = "timeout"

class MainWindow(QtWidgets.QMainWindow):

    question_pool:dict = {}
    qty_question:int = 0
    question:Question_gui
    actual_test:str = ''
    actual_test_name:str = ''
    description:str = ''
    start_test: dt = None
    screen_list:list = None
    result_data:dict = {}
    time_thread:Thread = None
    question_timeout_thread:Thread = None
    test_status:ThereadStatus = ThereadStatus.run
    timeout_question:int = 60
    completedtest: CompletedTest
    last_fio:str=''
    last_file:str=''

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        os.makedirs('./export', exist_ok=True)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Приложение для тестов')
        self.setWindowIcon(QIcon(self._resource_path('i.png')))

        self.screen_list = [
            self.ui.test_box,
            self.ui.test_result_box_menue
        ]

        self._connect_clicks()
        self._go_to_screen(self.ui.test_result_box_menue)

        users = session.query(User).all()
        self.ui.folder_list.addItems([user.name for user in users])

    def _resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def _connect_clicks(self):


        self.ui.next_question.clicked.connect(self._set_next_question)
        self.ui.previous_question.clicked.connect(self._set_prev_question)

        self.ui.get_export_result.clicked.connect(lambda: self.get_report_preproc(True))
        self.ui.get_result_from_result.clicked.connect(lambda: self.get_result_window(hist=True))
        self.ui.folder_list.currentTextChanged.connect(self.change_list_tests)
        self.ui.tests_list.currentItemChanged.connect(self.get_test_result)

    def _timedelta_formatter(self, td):
        td_sec = td.seconds
        hour_count, rem = divmod(td_sec, 3600)
        minute_count, second_count = divmod(rem, 60)
        msg = "{} Минут, {} Секунд".format(minute_count,second_count)
        return msg

    def get_test_result(self):
        try:
            curent_fil = self.ui.tests_list.currentItem().text()
            current_dir = self.ui.folder_list.currentText()

            test_name = self.ui.tests_list.currentItem().text()
            
            test_id = test_name.split('/')[0]

            test = session.query(CompletedTest).filter_by(id = test_id).first()

            total_time_raw = dt.strptime(test.total_time,"%H:%M:%S.%f")
            total_time = f'{total_time_raw.minute} Минут, {total_time_raw.second} Секунд'

            self.ui.type_test_result.setText(test.description)
            self.ui.time_wasted_result.setText(total_time)
            self.ui.correct_answers_result.setText(f"{test.right_ans_qty}/{len(test.completedquestions)}")

        except Exception as e:
            print(e)

    def change_list_tests(self):
        self.ui.tests_list.clear()
        name = self.ui.folder_list.currentText()

        user = session.query(User).filter_by(name = name).first()

        tests = session.query(CompletedTest).filter_by(user_id=user.id)
        tests = user.completedtests

        for test in tests:
            self.ui.tests_list.addItem(f"{test.id}/{test.description}")

    def init_result_menue(self):
        self.ui.folder_list.clear()
        self.result_data = {}
        self._go_to_screen(self.ui.test_result_box_menue)
        users = session.query(User).all()
        self.ui.folder_list.addItems([user.name for user in users])

    def get_result_window(self, hist = False):

        if hist:

            test_name = self.ui.tests_list.currentItem().text()
            test_id = test_name.split('/')[0]
            test = session.query(CompletedTest).filter_by(id = test_id).first()

            if test.test_type == "pomdezh_po_chasti":
                self.actual_test = TypeTest.instructions_DPCH_PDT.name
                self.actual_test_name = "pomdezh_po_chasti"
            elif test.test_type == "dezh_po_chasti":
                self.actual_test = TypeTest.instructions_DPCH_PDT.name
                self.actual_test_name = "dezh_po_chasti"
            elif test.test_type == "instructions_DPCH_PDT":
                self.actual_test = TypeTest.instructions_DPCH_PDT.name
                self.actual_test_name = "instructions_DPCH_PDT"
            elif test.test_type == "dezh_po_parku":
                self.actual_test = TypeTest.dezh_po_parku.name
                self.actual_test_name = "dezh_po_parku"
            elif test.test_type == "dezh_po_UBM":
                self.actual_test = TypeTest.dezh_po_UBM.name
                self.actual_test_name = "dezh_po_UBM"

            self.actual_test = test.test_type

            data = { self.actual_test: {} }

            self.question_pool = test.completedquestions
            
            self.question = Question_gui(self)
            self.question_data = data
            self.question.qty_question = len(self.question_pool)
            self.question.set_hist_mode()

        self._go_to_screen(self.ui.test_box)
        if not hist: self.question.set_view_mode()
        self.question.set_next_quest()

    def _hide_all(self):
        for screen in self.screen_list: screen.hide()

    def _go_to_screen(self, screen):
        self._hide_all()
        screen.show()

    def _end_test(self):
        self._go_to_screen(self.ui.test_result_box_menue)
        self.question.reset_actual_question()

        if self.question.active == Status.test:

            end_test = dt.now()
            self.ui.type_test_label.setText(Actual_test[self.actual_test].value)

            total_time = end_test - self.start_test
            self.ui.time_wasted_label.setText(self._timedelta_formatter(total_time))
            right_ans_qty = 0
            for quest in self.question_pool.values():
                if quest.result: right_ans_qty += 1
            self.ui.correct_answers_label.setText(f"{right_ans_qty}/{self.question.qty_question}")

            if self.ui.fio_input.currentText() == "":
                fio_dir = "Гость"
            else:
                fio_dir = self.ui.fio_input.currentText()

            if right_ans_qty >=8:
                grade = 5
            elif right_ans_qty < 8 and right_ans_qty >= 6:
                grade = 4
            elif right_ans_qty < 6 and right_ans_qty >= 5:
                grade = 3
            else:
                grade = 2

            # res = {
            #     "start_test":str(self.start_test),
            #     "end_test":str(end_test),
            #     "total_time":str(total_time),
            #     "actual_test":self.actual_test,
            #     "right_ans_qty": right_ans_qty,
            #     "question_data":question_data_dict,
            #     "fio": fio_dir,
            #     "grade": grade,
            #     "date": str(dt.now()),
            #     'description': Actual_test[self.actual_test].value
            # }

            self.completedtest.test_date = dt.now()
            self.completedtest.total_time = str(total_time)
            self.completedtest.right_ans_qty = right_ans_qty
            self.completedtest.grade = grade
            session.commit()

        elif self.question.active == Status.hist:
            self._go_to_screen(self.ui.test_result_box_menue)

    def _question_timeout_counter(self):

        actual_question = self.question.actual_question
        question_start = dt.now()
        while True:
            if self.test_status == ThereadStatus.stop:return 0
            if actual_question != self.question.actual_question:return 0

            sleep(0.1)
            delta = dt.now() - question_start
            if delta.seconds >= self.timeout_question:
                if self.test_status == ThereadStatus.stop:
                    return 0
                else:
                    self.test_status = ThereadStatus.timeout
                    self._set_next_question()
                    return 0

            self.ui.time_counter.setText(f'На вопрос осталось {self.timeout_question - delta.seconds} секунд')

    def _set_next_question(self):

        id_question = self.question.get_actual_question()
        if not self.question.active == Status.test:

            if self.question.qty_question > id_question:
                self.question.set_next_quest()
            else:
                self._end_test()
            return 0

        if self.question.active == Status.test:
            answer = self.question.get_answer()
            
            question = self.question_pool[id_question-1]
            
            for itm in answer:
                question.completedanswers[int(itm)-1].choosen = True
                session.add(question.completedanswers[int(itm)-1])
            right_answers = []
            
            for ans in question.completedanswers:
                if ans.is_correct: right_answers.append(str(ans.ans_id))

            question.result = sorted(answer) == sorted(right_answers)
            session.add(question)
            session.commit()

        if self.question.qty_question > id_question:

            self.test_status = ThereadStatus.stop
            if self.test_status == ThereadStatus.timeout: return 0
            try: self.question_timeout_thread.join()
            except: pass
            self.question.set_next_quest()
            self.test_status = ThereadStatus.run
            self.question_timeout_thread = Thread(target=self._question_timeout_counter)
            self.question_timeout_thread.start()
        else:
            self.test_status = ThereadStatus.stop
            self._end_test()

    def _set_prev_question(self):
        self.question.set_prev_quest()

    def init_question_poll(self):

        questions_list = session.query(Question).filter_by(question_type=self.actual_test).all()

        if len(questions_list) >= 10:
            question_pool = sample(questions_list, 10)
        else:
            question_pool = sample(questions_list, len(questions_list))

        for idx, quest in enumerate(question_pool):

            ans1 = CompletedAnswer(
                text = quest.answers[0].text,
                ans_id=quest.answers[0].ans_id,
                is_correct = quest.answers[0].is_correct,
                choosen = False
            )
            ans2 = CompletedAnswer(
                text = quest.answers[1].text,
                ans_id=quest.answers[1].ans_id,
                is_correct = quest.answers[1].is_correct,
                choosen = False
            )
            ans3 = CompletedAnswer(
                text = quest.answers[2].text,
                ans_id=quest.answers[2].ans_id,
                is_correct = quest.answers[2].is_correct,
                choosen = False
            )
            ans4 = CompletedAnswer(
                text = quest.answers[3].text,
                ans_id=quest.answers[3].ans_id,
                is_correct = quest.answers[3].is_correct,
                choosen = False
            )
            
            session.add(ans1)
            session.add(ans2)
            session.add(ans3)
            session.add(ans4)
            session.commit()
            comp_quest = CompletedQuestion(
                text = quest.text,
                completedanswers=[ans1, ans2, ans3, ans4],
            )

            session.add(comp_quest)
            session.commit()
            self.question_pool[idx] = comp_quest

        if self.ui.fio_input.currentText() == "":
            name = "Гость"
        else:
            name = self.ui.fio_input.currentText()

        test = CompletedTest(
            test_type=self.actual_test,
            completedquestions = [itm for itm in self.question_pool.values()],
            description = self.description,
            )

        session.add(test)

        user = session.query(User).filter_by(name=name).first()

        if not user:
            user = User(
                name = name,
                completedtests = [test]
            )
            session.add(test)
        else:
            user.completedtests.append(test)

        session.commit()

        self.completedtest = test

        self.qty_question = len(self.question_pool)

    def _run_test(self):
        self.init_question_poll()
        self._go_to_screen(self.ui.test_box)
        self.question = Question_gui(self)
        self.question.set_test_mode()
        self.question.set_next_quest()
        self.question_timeout_thread = Thread(target=self._question_timeout_counter)
        self.question_timeout_thread.start()
        self.start_test = dt.now()

    def run_test_pomdezh_po_chasti(self):
        
        self.actual_test = TypeTest.instructions_DPCH_PDT.name
        self.actual_test_name = "pomdezh_po_chasti"
        self.description = Actual_test.pomdezh_po_chasti.value
        self._run_test()

    def run_test_dezh_po_chasti(self):
        self.actual_test = TypeTest.instructions_DPCH_PDT.name
        self.actual_test_name = "dezh_po_chasti"
        self.description = Actual_test.dezh_po_chasti.value
        self._run_test()

    def run_test_instructions_DPCH_PDT(self):
        self.actual_test = TypeTest.instructions_DPCH_PDT.name
        self.actual_test_name = "instructions_DPCH_PDT"
        self.description = Actual_test.instructions_DPCH_PDT.value
        self._run_test()

    def run_test_dezh_po_parku(self):
        self.actual_test = TypeTest.dezh_po_parku.name
        self.actual_test_name = "dezh_po_parku"
        self.description = Actual_test.dezh_po_parku.value
        self._run_test()

    def run_test_dezh_po_UBM(self):
        self.actual_test = TypeTest.dezh_po_UBM.name
        self.actual_test_name = "dezh_po_UBM"
        self.description = Actual_test.dezh_po_UBM.value
        self._run_test()

    def _get_report(self):

        test_name = self.ui.tests_list.currentItem().text()
        test_id = test_name.split('/')[0]
        test = session.query(CompletedTest).filter_by(id = test_id).first()

        type_test = test.description

        total_time_raw = dt.strptime(test.total_time,"%H:%M:%S.%f")
        total_time = f'{total_time_raw.minute} Минут, {total_time_raw.second} Секунд'
        test_date_str = test.test_date.strftime("%Y-%m-%d %H:%M:%S")
        pdf = FPDF()
        pdf.add_page()

        pdf.add_font('DejaVu', '', self._resource_path('DejaVuSansCondensed.ttf'), uni=True)
        pdf.set_font("DejaVu", size=14)
        pdf.cell(200, 10, txt="Отчёт по тесту", ln=1, align="C")
        pdf.set_font("DejaVu", size=12)
        pdf.cell(200, 10, txt=f"ФИО: {test.users.name}", ln=1, align="L")
        pdf.cell(200, 10, txt=f"Тип теста: {type_test}", ln=1, align="L")
        pdf.cell(200, 10, txt=f"Дата: {test_date_str}", ln=1, align="L")
        pdf.cell(200, 10, txt=f"Время теста: {total_time}", ln=1, align="L")
        pdf.cell(200, 10, txt=f"Количество правильных ответов: {test.right_ans_qty}", ln=1, align="L")

        for idx, question in enumerate(test.completedquestions, start=1):

            if not question.result:
                pdf.set_text_color(255, 0, 0)
            else:
                pdf.set_text_color(0, 0, 0)

            pdf.set_font("DejaVu", size=14)

            pdf.cell(200, 10, txt="", ln=1, align="C")
            pdf.cell(200, 10, txt=f"Вопрос: {idx}", ln=1, align="C")
            pdf.cell(200, 10, txt=question.text, ln=1, align="C")

            pdf.set_font("DejaVu", size=12)

            for ans_val in question.completedanswers:

                if ans_val.choosen:
                    # if ans_val.ans_id not in question['right_answers']:
                    if not ans_val.is_correct:
                        pdf.set_text_color(255, 0, 0)
                    else:
                        pdf.set_text_color(0, 0, 0)
                else:
                    pdf.set_text_color(0, 0, 0)

                pdf.multi_cell(0, 10, txt=f"{ans_val.text}", align="L")

        pdf.output(f"./export/{type_test}_{self.last_fio}.pdf")

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setInformativeText('Готово')
        msg.StandardButton(QMessageBox.Ok)
        msg.exec_()

    def get_report_preproc(self, end_test):

        if end_test:
            self.last_fio = self.ui.folder_list.currentText()
            self.last_file = self.ui.tests_list.currentItem().text()
        self._get_report()

app = QtWidgets.QApplication(sys.argv)
graf = MainWindow()
graf.show()

sys.exit(app.exec_())
