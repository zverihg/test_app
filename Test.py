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




class Question_data():

    id_question:int
    question:str
    answers:list
    right_answers:list

    def __init__(self, id_question, data):
        self.id_question = id_question
        self.answers = data["answers"]
        self.right_answer = data["right_answers"]
        self.question = data["question"]



class Question_gui():

    actual_question:int = 0

    question_text:QLabel

    choose_answer_1:QCheckBox
    choose_answer_2:QCheckBox
    choose_answer_3:QCheckBox
    choose_answer_4:QCheckBox

    answer_var_1:QLabel
    answer_var_2:QLabel
    answer_var_3:QLabel
    answer_var_4:QLabel


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


    def set_quest(self, data):

        self.actual_question +=1

        now_quest = data[str(self.actual_question)]

        self.choose_answer_1.setCheckState(False)
        self.choose_answer_2.setCheckState(False)
        self.choose_answer_3.setCheckState(False)
        self.choose_answer_4.setCheckState(False)

        self.answer_var_1.setText(now_quest['answers']['1'])
        self.answer_var_2.setText(now_quest['answers']['2'])
        self.answer_var_3.setText(now_quest['answers']['3'])
        self.answer_var_4.setText(now_quest['answers']['4'])

        self.question_text.setText(now_quest['question'])

    def get_answer(self):

        data = []
        if self.choose_answer_1.isChecked(): data.append('1')
        if self.choose_answer_2.isChecked(): data.append('2')
        if self.choose_answer_3.isChecked(): data.append('3')
        if self.choose_answer_4.isChecked(): data.append('4')

        return [data]

class MainWindow(QtWidgets.QMainWindow):

    question_list:dict = {}
    question:Question_gui
    actual_test:str = 'pomdezh_po_chasti'

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        uic.loadUi('testing_gui.ui', self)

        self.init_hide()

        self.question_data = self.init_question_poll()
        self.question = Question_gui(self)

        self.next_question.clicked.connect(self.set_next_question)
        self.test_button.clicked.connect(self.go_to_test)
        self.back_to_main_window.clicked.connect(self.go_back_to_main_window)
        self.pom_dezh_po_chasti.clicked.connect(self.run_test_pomdezh_po_chasti)

    def init_hide(self):
        self.test_menu.hide()
        self.test_box.hide()
        self.main_layout.show()

    def set_next_question(self):

        answers = self.question.get_answer()
        self.question.set_quest(data = self.question_data[self.actual_test])



    def go_to_test(self):

        self.main_layout.hide()
        self.test_menu.show()

    def go_back_to_main_window(self):
        
        self.main_layout.show()
        self.test_menu.hide()

    def init_question_poll(self) -> dict:

        with open('./tests_v0.json', "r") as dta:
            question_data = json.load(dta)

        data = {}

        for type_test, test in question_data.items():
            data[type_test] = {}
            for idx, data_quest in test.items():
                data[type_test][idx] = Question_data(idx, data_quest)

        return question_data


    def run_test_pomdezh_po_chasti(self):

        self.test_menu.hide()
        self.test_box.show()
        self.main_layout.hide()


        self.question.set_quest(self.question_data[self.actual_test])


        pass

app = QtWidgets.QApplication(sys.argv)
graf = MainWindow()
graf.show()

sys.exit(app.exec_())