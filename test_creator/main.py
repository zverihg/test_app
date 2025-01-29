#!/usr/bin/env python

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
import sys, os
from PyQt5 import QtWidgets
import json
from Ui_main import Ui_MainWindow
from copy import copy
from enum import Enum

class Active_type(Enum):
    pomdezh_po_chasti = 1
    dezh_po_chasti = 2

class Question():
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

class Test():

    description:str
    time:int
    poll_questions:dict = {}

    def __init__(self):
        self.poll_questions = dict()

    def set_data(self,data):

        self.description = data['description']
        self.time = data['time']
        self.poll_questions = data['poll_questions']

    def add_question(self,quest):

        data = {
            'id_question':quest['id_question'],
            'question': quest['question'],
            'answers':quest['answers'],
            'right_answers':quest['right_answers'],
        }
        self.poll_questions[quest['id_question']] = Question(data)

    def get_json_ready_object(self):

        dict_poll_questions = {}

        for idx, itm in self.poll_questions.items():

            dict_poll_questions[idx] = {
                'id_question':itm.id_question,
                'question':itm.question,
                'answers':itm.answers,
                'right_answers':itm.right_answers,
                'choosen_var':itm.choosen_var,
                'answer_result':itm.answer_result,
            }

        json_data = {
            "description":self.description,
            "time":self.time,
            "poll_questions":dict_poll_questions
        }

        return json_data

    def del_quest(self, idx_quest):

        self.poll_questions.pop(idx_quest)
        tmp = copy(self.poll_questions)
        self.poll_questions = {}
        counter = 1
        for idx, itm in tmp.items():
            itm.id_question = str(counter)
            self.poll_questions[str(counter)] = itm
            counter += 1

class MainWindow(QtWidgets.QMainWindow):

    active_type:Active_type = Active_type.pomdezh_po_chasti
    tests:Test = None
    ans_lst:dict = {}
    chooses_lst:dict = {}

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.tests = {Active_type.pomdezh_po_chasti:Test(), Active_type.dezh_po_chasti:Test()}

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ans_lst = { '1':self.ui.answer_1, '2':self.ui.answer_2, '3':self.ui.answer_3, '4':self.ui.answer_4,}
        self.chooses_lst = { '1':self.ui.choose_1, '2':self.ui.choose_2, '3':self.ui.choose_3,'4':self.ui.choose_4,}
        self.load_json()

        self.ui.save_curent_question.clicked.connect(self.save_question)
        self.ui.list_questions.clicked.connect(self.clicked_on_row)
        self.ui.add_new_question.clicked.connect(self.add_new_question)
        self.ui.type_test_choose.currentIndexChanged.connect(self.change_type)
        self.ui.delete_curent_question.clicked.connect(self.del_question)

    def del_question(self):
        
        idx_quest = self.ui.list_questions.currentItem().text().replace("Вопрос ", "")
        self.tests[self.active_type].del_quest(idx_quest)
        self.set_question_list_gui()
        self.save_to_json()

    def change_type(self):

        self.active_type = Active_type[self.ui.type_test_choose.currentText()]
        self.set_question_list_gui()

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
        self.tests[self.active_type].add_question(copy(data))

        self.ui.list_questions.addItem(f"Вопрос {idx}")

    def clicked_on_row(self):

        for itm in self.chooses_lst.values(): itm.setChecked(False)
        for itm in self.ans_lst.values(): itm.setText("")
        idx_quest = self.ui.list_questions.currentItem().text().replace("Вопрос ", "")
        quest = self.tests[self.active_type].poll_questions[idx_quest]
        self.ui.test_question.setText(quest.question)

        for idx, txt in quest.answers.items():
            self.ans_lst[idx].setText(txt)

        for idx in quest.right_answers:
            self.chooses_lst[idx].setChecked(True)

    def create_new_json(self):

        raw_json = {
            "pomdezh_po_chasti": {
                "description": "Помошник дежурного по части",
                "time": 600,
                "poll_questions": {}
            },
            "dezh_po_chasti": {
                "description": "Дежурный по части",
                "time": 600,
                "poll_questions": {}
            }
        }

        with open(f'./tests_v0.json', 'w') as fp:
            json.dump(raw_json,fp)

        self.tests[Active_type.pomdezh_po_chasti].description = raw_json['pomdezh_po_chasti']['description']
        self.tests[Active_type.pomdezh_po_chasti].time = raw_json['pomdezh_po_chasti']['time']

        self.tests[Active_type.dezh_po_chasti].description = raw_json['dezh_po_chasti']['description']
        self.tests[Active_type.dezh_po_chasti].time = raw_json['dezh_po_chasti']['time']

        self.ui.list_questions
        self.ui.type_test_choose.addItems(['pomdezh_po_chasti', 'dezh_po_chasti'])

        data = {
            'id_question':'1',
            'question': self.ui.test_question.text(),
            'answers':{},
            'right_answers':{},
        }

        self.tests[Active_type.pomdezh_po_chasti].add_question(copy(data))
        self.tests[Active_type.dezh_po_chasti].add_question(copy(data))

        self.ui.list_questions.addItem('Вопрос 1')

    def save_to_json(self):

        with open('./tests_v0.json', 'r') as fil: data = json.load(fil)

        pomdezh_po_chasti = self.tests[Active_type.pomdezh_po_chasti].get_json_ready_object()
        dezh_po_chasti = self.tests[Active_type.dezh_po_chasti].get_json_ready_object()

        data['pomdezh_po_chasti'] = pomdezh_po_chasti
        data['dezh_po_chasti'] = dezh_po_chasti

        with open('./tests_v0.json', 'w') as fil: data = json.dump(data,fil)

    def set_question_list_gui(self):

        for itm in self.chooses_lst.values(): itm.setChecked(False)
        for itm in self.ans_lst.values(): itm.setText("")
        self.ui.test_question.setText('')
        self.ui.list_questions.clear()
        poll_questions = self.tests[self.active_type].poll_questions
        for idx, quest in poll_questions.items():
            self.ui.list_questions.addItem(f"Вопрос {idx}")

    def load_json(self):

        try:
            with open('./tests_v0.json', 'r') as fil: data = json.load(fil)

            test_dict = {
                'pomdezh_po_chasti':{},
                'dezh_po_chasti':{},
            }

            self.ui.type_test_choose.addItems(['pomdezh_po_chasti','dezh_po_chasti'])
            self.active_type = Active_type.pomdezh_po_chasti
            if not data['pomdezh_po_chasti']['poll_questions'] and not data['dezh_po_chasti']['poll_questions']:
                self.create_new_json()
                return 0
            
            for type_test, itm in data.items():

                poll_questions = itm['poll_questions']
                self.tests[Active_type[type_test]].description = itm['description']
                self.tests[Active_type[type_test]].time = itm['time']
                for val in poll_questions.values():
                    self.tests[Active_type[type_test]].add_question(val)
                print(itm)

        except:
            self.create_new_json()
        finally:
            self.set_question_list_gui()

    def save_question(self):

        answers = {
            '1':self.ui.answer_1.toPlainText(),
            '2':self.ui.answer_2.toPlainText(),
            '3':self.ui.answer_3.toPlainText(),
            '4':self.ui.answer_4.toPlainText()
        }
        right_answers = []
        chooses = {
            '1':self.ui.choose_1.checkState(),
            '2':self.ui.choose_2.checkState(),
            '3':self.ui.choose_3.checkState(),
            '4':self.ui.choose_4.checkState(),
        }

        for idx, val in chooses.items():
            if val: right_answers.append(idx)

        id_question = str(self.ui.list_questions.currentItem().text().replace('Вопрос ',''))

        self.ui.list_questions.currentIndex().data
        data = {
            'id_question':id_question,
            'question': self.ui.test_question.text(),
            'answers':answers,
            'right_answers':right_answers,
        }

        test = Question(data)

        test_type = self.ui.type_test_choose.currentText()

        self.tests[self.active_type].poll_questions[id_question] = test

        self.save_to_json()

app = QtWidgets.QApplication(sys.argv)
graf = MainWindow()
graf.show()

sys.exit(app.exec_())