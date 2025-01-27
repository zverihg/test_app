from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *

from question_data import Question_data

class Question_gui():
    '''
        Класс для управления GUI теста
    '''

    active:bool = True
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

        self.choose_answer_1 = main_win.ui.choose_answer_1
        self.choose_answer_2 = main_win.ui.choose_answer_2
        self.choose_answer_3 = main_win.ui.choose_answer_3
        self.choose_answer_4 = main_win.ui.choose_answer_4

        self.answer_var_1 = main_win.ui.answer_var_1
        self.answer_var_2 = main_win.ui.answer_var_2
        self.answer_var_3 = main_win.ui.answer_var_3
        self.answer_var_4 = main_win.ui.answer_var_4
        
        self.question_text = main_win.ui.question_text
        self.qty_question_label = main_win.ui.qty_question_label


    def get_actual_question(self):
        return self.actual_question

    def reset_actual_question(self):
        self.actual_question = 0

    def set_view_mode(self):
        self.choose_answer_1.setEnabled(False)
        self.choose_answer_2.setEnabled(False)
        self.choose_answer_3.setEnabled(False)
        self.choose_answer_4.setEnabled(False)
        self.active = False

    def set_test_mode(self):
        self.choose_answer_1.setEnabled(True)
        self.choose_answer_2.setEnabled(True)
        self.choose_answer_3.setEnabled(True)
        self.choose_answer_4.setEnabled(True)
        self.active = True


    def set_quest(self, data):

        self.actual_question +=1
        now_quest = data[str(self.actual_question)]

        self.answer_var_1.setText(now_quest.answers['1'])
        self.answer_var_2.setText(now_quest.answers['2'])
        self.answer_var_3.setText(now_quest.answers['3'])
        self.answer_var_4.setText(now_quest.answers['4'])

        self.question_text.setText(now_quest.question)
        self.qty_question_label.setText(f'{self.actual_question}/{self.qty_question}')

        if self.active:

            self.choose_answer_1.setCheckState(False)
            self.choose_answer_2.setCheckState(False)
            self.choose_answer_3.setCheckState(False)
            self.choose_answer_4.setCheckState(False)
        else:

            self.choose_answer_1.setCheckState('1' in now_quest.choosen_var)
            self.choose_answer_2.setCheckState('2' in now_quest.choosen_var)
            self.choose_answer_3.setCheckState('3' in now_quest.choosen_var)
            self.choose_answer_4.setCheckState('4' in now_quest.choosen_var)

    def get_answer(self):

        data = []
        if self.choose_answer_1.isChecked(): data.append('1')
        if self.choose_answer_2.isChecked(): data.append('2')
        if self.choose_answer_3.isChecked(): data.append('3')
        if self.choose_answer_4.isChecked(): data.append('4')

        return data

