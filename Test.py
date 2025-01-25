#!/usr/bin/env python

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
import sys  
from PyQt5 import QtWidgets, uic
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import json
from datetime import datetime as dt

class Question_data():
    '''
        Данные из JSON файла 
    '''
    id_question:int
    question:str
    answers:list
    right_answers:list
    choosen_var:list = []
    answer_result:bool = False

    def __init__(self, id_question, data):
        self.id_question = id_question
        self.answers = data["answers"]
        self.right_answer = data["right_answers"]
        self.question = data["question"]


class Question_gui():
    '''
        Класс для управления GUI теста
    '''

    actual_question:int = 0
    qty_question:int = 0
    question_text:QLabel

    choose_answer_1:QCheckBox
    choose_answer_2:QCheckBox
    choose_answer_3:QCheckBox
    choose_answer_4:QCheckBox

    answer_var_1:QLabel
    answer_var_2:QLabel
    answer_var_3:QLabel
    answer_var_4:QLabel
    qty_question_label:QLabel

    def __init__(self,main_win):

        self.choose_answer_1 = main_win.choose_answer_1
        self.choose_answer_2 = main_win.choose_answer_2
        self.choose_answer_3 = main_win.choose_answer_3
        self.choose_answer_4 = main_win.choose_answer_4

        self.answer_var_1 = main_win.answer_var_1
        self.answer_var_2 = main_win.answer_var_2
        self.answer_var_3 = main_win.answer_var_3
        self.answer_var_4 = main_win.answer_var_4
        
        self.question_text = main_win.question_text
        self.qty_question_label = main_win.qty_question_label


    def get_actual_question(self):
        return self.actual_question

    def reset_actual_question(self):
        self.actual_question = 0


    def set_quest(self, data):

        self.actual_question +=1

        now_quest = data[str(self.actual_question)]

        self.choose_answer_1.setCheckState(False)
        self.choose_answer_2.setCheckState(False)
        self.choose_answer_3.setCheckState(False)
        self.choose_answer_4.setCheckState(False)

        self.answer_var_1.setText(now_quest.answers['1'])
        self.answer_var_2.setText(now_quest.answers['2'])
        self.answer_var_3.setText(now_quest.answers['3'])
        self.answer_var_4.setText(now_quest.answers['4'])


        self.question_text.setText(now_quest.question)
        self.qty_question_label.setText(f'{self.actual_question}/{self.qty_question}')


    def get_answer(self):

        data = []
        if self.choose_answer_1.isChecked(): data.append('1')
        if self.choose_answer_2.isChecked(): data.append('2')
        if self.choose_answer_3.isChecked(): data.append('3')
        if self.choose_answer_4.isChecked(): data.append('4')

        return data


class MainWindow(QtWidgets.QMainWindow):

    meta_data_test: dict = {}
    question_list:dict = {}
    question:Question_gui
    actual_test:str = ''
    start_test: dt = None

    screen_list:list = None


    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('testing_gui.ui', self)

        self.screen_list = [ self.test_menu, self.test_box, self.test_result_box, self.main_layout, ]

        self.go_to_screen(self.main_layout)
        self.question_data, self.meta_data_test = self.init_question_poll()

        self.next_question.clicked.connect(self.set_next_question)
        self.pom_dezh_po_chasti.clicked.connect(self.run_test_pomdezh_po_chasti)

        self.test_button.clicked.connect(lambda: self.go_to_screen(self.test_menu))
        self.back_to_main_window.clicked.connect(lambda: self.go_to_screen(self.main_layout))
        self.back_main_menu.clicked.connect(lambda: self.go_to_screen(self.main_layout))

    def timedelta_formatter(self, td):                       # defining the function
        td_sec = td.seconds                                  # getting the seconds field of the timedelta
        hour_count, rem = divmod(td_sec, 3600)               # calculating the total hours
        minute_count, second_count = divmod(rem, 60)         # distributing the remainders
        msg = "{} Минут, {} Секунд".format(minute_count,second_count)
        return msg                                           # returning the custom output

    def _hide_all(self):
        for screen in self.screen_list: screen.hide()

    def go_to_screen(self, screen):
        self._hide_all()
        screen.show()

    def set_next_question(self):

        answer = self.question.get_answer()
        id_question = self.question.get_actual_question()
        question = self.question_data[self.actual_test][str(id_question)]

        question.choosen_var = answer
        question.answer_result = question.choosen_var == question.right_answer

        if self.question.qty_question > id_question:
            self.question.set_quest(data = self.question_data[self.actual_test])
        else:
            self.go_to_screen(self.test_result_box)
            self.question.reset_actual_question()

            end_test = dt.now()
            meta_quest = self.meta_data_test[self.actual_test]
            kek = end_test- self.start_test
            self.type_test_label.setText(meta_quest["description"])
            self.time_wasted_label.setText(self.timedelta_formatter(kek))

            right_ans_qty = 0

            for idx, quest in self.question_data[self.actual_test].items():
                if quest.answer_result: right_ans_qty += 1

            self.correct_answers_label.setText(f"{right_ans_qty}/{self.question.qty_question}")

    def init_question_poll(self) -> dict:

        with open('./tests_v0.json', "r") as dta: question_data = json.load(dta)

        data = {}
        meta_data_test = {}

        for type_test, test in question_data.items():
            data[type_test] = {}

            meta_data_test[type_test] = {
                "description": question_data[type_test]["description"],
                "time": question_data[type_test]["time"]
            }

            for idx, data_quest in test['poll_questions'].items():
                data[type_test][idx] = Question_data(idx, data_quest)

        return data, meta_data_test

    def run_test_pomdezh_po_chasti(self):

        self.go_to_screen(self.test_box)

        self.question = Question_gui(self)
        self.actual_test = "pomdezh_po_chasti"
        self.question.qty_question = len(self.question_data[self.actual_test])
        self.question.set_quest(self.question_data[self.actual_test])
        self.start_test = dt.now()

app = QtWidgets.QApplication(sys.argv)
graf = MainWindow()
graf.show()

sys.exit(app.exec_())