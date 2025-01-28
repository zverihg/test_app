#!/usr/bin/env python

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
import sys, os
from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import json
from datetime import datetime as dt
from Ui_main import Ui_MainWindow
from threading import Thread
from copy import copy
from time import sleep
from random import sample

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

class MainWindow(QtWidgets.QMainWindow):

    active_type:Active_type = Active_type.pomdezh_po_chasti
    tests:Test = None

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        os.makedirs('./result', exist_ok=True)

        self.tests = {Active_type.pomdezh_po_chasti:Test(), Active_type.dezh_po_chasti:Test()}

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_json()

        self.ui.save_curent_question.clicked.connect(self.save_question)
        self.ui.list_questions.clicked.connect(self.clicked_on_row)

    def clicked_on_row(self):
        print('fuck')

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

        pomdezh_po_chasti = self.tests['pomdezh_po_chasti'].get_json_ready_object()
        dezh_po_chasti = self.tests['dezh_po_chasti'].get_json_ready_object()

        data['pomdezh_po_chasti'] = pomdezh_po_chasti
        data['dezh_po_chasti'] = dezh_po_chasti

        with open('./tests_v0.json', 'w') as fil: data = json.dump(data,fil)

    def set_question_list_gui(self):

        ttt = self.tests[self.active_type]
        
        



    def load_json(self):

        with open('./tests_v0.json', 'r') as fil: data = json.load(fil)

        test_dict = {
            'pomdezh_po_chasti':{},
            'dezh_po_chasti':{},
        }
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

        self.tests[test_type].poll_questions[id_question] = test

        self.save_to_json()




app = QtWidgets.QApplication(sys.argv)
graf = MainWindow()
graf.show()

sys.exit(app.exec_())