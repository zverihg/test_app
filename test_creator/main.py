#!/usr/bin/env python

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys, os
from PyQt5 import QtWidgets
import json
from Ui_main import Ui_MainWindow
from copy import copy

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


class TypesQuestions():

    instructions_DPCH_PDT:dict[QuestionPool]
    dezh_po_parku:dict[QuestionPool]
    dezh_po_UBM:dict[QuestionPool]

    def __init__(self):

        self.instructions_DPCH_PDT = {}
        self.dezh_po_parku = {}
        self.dezh_po_UBM = {}

    def _get_json(self):
        raw = {
            "instructions_DPCH_PDT": {},
            "dezh_po_parku": {},
            "dezh_po_UBM": {},
        }

        item_list = {
            "instructions_DPCH_PDT": self.instructions_DPCH_PDT,
            "dezh_po_parku": self.dezh_po_parku,
            "dezh_po_UBM": self.dezh_po_UBM,
        }

        for qustion_type, pool in item_list.items():
            for idx, question in pool.items():
                raw[qustion_type][idx] = {
                    'id_question':question.id_question,
                    'question':question.question,
                    'answers':question.answers,
                    'right_answers':question.right_answers,
                    'choosen_var':question.choosen_var,
                    'answer_result':question.answer_result,
                }

        return raw

class MainWindow(QtWidgets.QMainWindow):

    ans_lst:dict = {}
    chooses_lst:dict = {}
    question_pool:TypesQuestions = TypesQuestions()
    
    active_question_poll:QuestionPool

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Конфигуратор тестов')
        self.setWindowIcon(QIcon(self._resource_path('i.png')))

        self.ans_lst = { '1':self.ui.answer_1, '2':self.ui.answer_2, '3':self.ui.answer_3, '4':self.ui.answer_4,}
        self.chooses_lst = { '1':self.ui.choose_1, '2':self.ui.choose_2, '3':self.ui.choose_3,'4':self.ui.choose_4,}
        self.load_json()

        self.ui.save_curent_question.clicked.connect(self.save_question)
        self.ui.list_questions.clicked.connect(self.clicked_on_row)
        self.ui.add_new_question.clicked.connect(self.add_new_question)
        self.ui.delete_curent_question.clicked.connect(self.del_question)

        self.ui.choose_type_question.addItems(["ДПЧ, ПДПЧ, ПДТ", "Дежурный по парку", "Дежурный по УБМ"])
        self.ui.choose_type_question.currentTextChanged.connect(self._change_test)


    def _change_test(self):
        print("fuck")
        test = self.ui.choose_type_question.currentIndex()

        if test == "ДПЧ, ПДПЧ, ПДТ":
            self.active_question_poll = self.question_pool.instructions_DPCH_PDT
        elif test == "Дежурный по парку":
            self.active_question_poll = self.question_pool.dezh_po_parku
        elif test == "Дежурный по УБМ":
            self.active_question_poll = self.question_pool.dezh_po_UBM
        else: print("fuck")

        self.set_question_list_gui()

    def _get_json_ready_object(self):

        dict_poll_questions = {}

        for idx, question in self.question_pool.items():

            dict_poll_questions[idx] = {
                'id_question':question.id_question,
                'question':question.question,
                'answers':question.answers,
                'right_answers':question.right_answers,
                'choosen_var':question.choosen_var,
                'answer_result':question.answer_result,
            }

        return dict_poll_questions

    def _resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def _onbin(self, a ): return ' '.join( format( ord(x), 'b') for x in ''.join( json.dumps( a ) ) )
    def _unbin(self, a ): return json.loads( ''.join( chr( int( x, 2 ) ) for x in a.split(' ') ) )

    def del_question(self):

        idx_question = self.ui.list_questions.currentItem().text().replace("Вопрос ", "")

        self.question_pool.pop(idx_question)

        tmp = copy(self.question_pool)
        self.question_pool = {}
        counter = 1
        for question in tmp.values():
            question.id_question = str(counter)
            self.question_pool[str(counter)] = question
            counter += 1

        self.set_question_list_gui()
        self.clicked_on_row()
        self.save_to_json()

    def add_new_question(self):

        try:
            idx = self.ui.list_questions.item(len(self.ui.list_questions)-1).text().replace("Вопрос ", "")
        except:
            idx = "0"

        idx = str(int(idx)+1)
        data = {
            'id_question':idx,
            'question': '',
            'answers':{},
            'right_answers':{},
        }
        self.question_pool[idx] = QuestionPool(data=copy(data))
        self.ui.list_questions.addItem(f"Вопрос {idx}")

    def clicked_on_row(self):

        for itm in self.chooses_lst.values(): itm.setChecked(False)
        for itm in self.ans_lst.values(): itm.setText("")
        idx_quest = self.ui.list_questions.currentItem().text().replace("Вопрос ", "")

        quest = self.active_question_poll[idx_quest]
        self.ui.test_question.setText(quest.question)

        for idx, txt in quest.answers.items():
            self.ans_lst[idx].setText(txt)

        for idx in quest.right_answers:
            self.chooses_lst[idx].setChecked(True)

    def create_new_json(self):
        self.ui.list_questions.clear()
        raw_json = {
            "instructions_DPCH_PDT": {},
            "dezh_po_parku": {},
            "dezh_po_UBM": {},
        }

        with open(f'./config.json', 'w') as fp:
            raw_bin_json = self._onbin(raw_json)
            json.dump(raw_bin_json,fp)

        init_question = {
            'id_question':'1',
            'question': self.ui.test_question.text(),
            'answers':{},
            'right_answers':{},
        }
        
        self.question_pool.dezh_po_parku['1'] = QuestionPool(data=copy(init_question))
        self.question_pool.dezh_po_UBM['1'] = QuestionPool(data=copy(init_question))
        self.question_pool.instructions_DPCH_PDT['1'] = QuestionPool(data=copy(init_question))
        self.active_question_poll = self.question_pool.instructions_DPCH_PDT
        self.ui.list_questions.addItem('Вопрос 1')

    def save_to_json(self):

        # json_question = self._get_json_ready_object()

        json_question = self.question_pool._get_json()

        bin_data = self._onbin(json_question)
        with open('./config.json', 'w') as fil:
            json.dump(bin_data,fil)
        with open('./raw_config.json', 'w') as fil:
            json.dump(json_question,fil)

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setInformativeText('Вопросы сохранены')
        msg.StandardButton(QMessageBox.Ok)
        msg.exec_()

    def set_question_list_gui(self):

        for itm in self.chooses_lst.values(): itm.setChecked(False)
        for itm in self.ans_lst.values(): itm.setText("")
        self.ui.test_question.setText('')
        self.ui.list_questions.clear()

        for idx in self.active_question_poll.keys():
            self.ui.list_questions.addItem(f"Вопрос {idx}")

        item = self.ui.list_questions.item(0)
        self.ui.list_questions.setCurrentItem(item)

    def load_json(self):

        try:
            with open('./config.json', 'r') as fil:
                bin_data = json.load(fil)
                data = self._unbin(bin_data)

            if not data:
                self.create_new_json()
            else:
                for idx, question in data.items():
                    self.question_pool[idx] = QuestionPool(question)

        except Exception as e:
            print(e)
            self.create_new_json()
        finally:
            self.set_question_list_gui()
            self.clicked_on_row()

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

            id_question = str(self.ui.list_questions.currentItem().text().replace('Вопрос ',''))

            data = {
                'id_question':id_question,
                'question': self.ui.test_question.text(),
                'answers':answers,
                'right_answers':right_answers,
            }

            self.active_question_poll[id_question] = QuestionPool(data)
            self.save_to_json()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setInformativeText('Выберите вопрос из списка')
            msg.exec_()

app = QtWidgets.QApplication(sys.argv)
graf = MainWindow()
graf.show()

sys.exit(app.exec_())
