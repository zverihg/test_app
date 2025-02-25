from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from enum import Enum
import time
class Status(Enum):
    hist = 1
    test = 2
    view = 3

class Question_gui():
    '''
        Класс для управления GUI теста
    '''

    question_pool:dict = {}

    active:Status = Status.hist
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
    previous_question:QPushButton
    answer_var_list:list

    red_style:str = '''
                color: rgb(255, 0, 4);
                background-color: rgb(255, 255, 255);
                border-radius: 20px;
                padding-left:10px
            '''
    dafault_style:str = '''
                background-color: rgb(255, 255, 255);
                border-radius: 20px;
                padding-left:10px
            '''


    def __init__(self, main_win):

        self.choose_answer_1 = main_win.ui.choose_answer_1
        self.choose_answer_2 = main_win.ui.choose_answer_2
        self.choose_answer_3 = main_win.ui.choose_answer_3
        self.choose_answer_4 = main_win.ui.choose_answer_4

        self.answer_var_1:QLabel = main_win.ui.answer_var_1
        self.answer_var_2:QLabel = main_win.ui.answer_var_2
        self.answer_var_3:QLabel = main_win.ui.answer_var_3
        self.answer_var_4:QLabel = main_win.ui.answer_var_4

        self.question_text = main_win.ui.question_text
        self.qty_question_label = main_win.ui.qty_question_label
        self.previous_question = main_win.ui.previous_question
        self.qty_question = main_win.qty_question
        self.question_pool = main_win.question_pool
        self.answer_var_list = [
                ['1',self.answer_var_1],
                ['2',self.answer_var_2],
                ['3',self.answer_var_3],
                ['4',self.answer_var_4],
            ]

    def get_actual_question(self): return self.actual_question

    def reset_actual_question(self): self.actual_question = 0

    def set_view_mode(self):
        self.choose_answer_1.setEnabled(False)
        self.choose_answer_2.setEnabled(False)
        self.choose_answer_3.setEnabled(False)
        self.choose_answer_4.setEnabled(False)
        self.previous_question.show()
        self.active = Status.view

    def set_hist_mode(self):
        self.choose_answer_1.setEnabled(False)
        self.choose_answer_2.setEnabled(False)
        self.choose_answer_3.setEnabled(False)
        self.choose_answer_4.setEnabled(False)
        self.previous_question.show()
        self.active = Status.hist

    def set_test_mode(self):
        self.choose_answer_1.setEnabled(True)
        self.choose_answer_2.setEnabled(True)
        self.choose_answer_3.setEnabled(True)
        self.choose_answer_4.setEnabled(True)
        self.previous_question.hide()
        self.active = Status.test

    def set_prev_quest(self):

        for itm in self.answer_var_list: itm[1].setStyleSheet("")

        if self.actual_question == 1:
            pass
        else:
            self.actual_question -= 1

            now_quest = self.question_pool[str(self.actual_question)]

            self.answer_var_1.setText(now_quest.answers['1'])
            self.answer_var_2.setText(now_quest.answers['2'])
            self.answer_var_3.setText(now_quest.answers['3'])
            self.answer_var_4.setText(now_quest.answers['4'])
            self.question_text.setText(now_quest.question)
            self.qty_question_label.setText(f'{self.actual_question}/{self.qty_question}')

            self.choose_answer_1.setCheckState('1' in now_quest.choosen_var and not self.active == Status.test)
            self.choose_answer_2.setCheckState('2' in now_quest.choosen_var and not self.active == Status.test)
            self.choose_answer_3.setCheckState('3' in now_quest.choosen_var and not self.active == Status.test)
            self.choose_answer_4.setCheckState('4' in now_quest.choosen_var and not self.active == Status.test)

            if self.active in [Status.view, Status.hist]:
                for itm in self.answer_var_list:
                    if itm[0] in now_quest.choosen_var and itm[0] not in now_quest.right_answers:
                        itm[1].setStyleSheet(self.red_style)
                    else:
                        itm[1].setStyleSheet(self.dafault_style)


    def set_next_quest(self):

        for itm in self.answer_var_list: itm[1].setStyleSheet("")

        self.actual_question +=1
        now_quest = self.question_pool[str(self.actual_question)]

        self.answer_var_1.setText(now_quest.answers['1'])
        self.answer_var_2.setText(now_quest.answers['2'])
        self.answer_var_3.setText(now_quest.answers['3'])
        self.answer_var_4.setText(now_quest.answers['4'])
        self.question_text.setText(now_quest.question)
        self.qty_question_label.setText(f'{self.actual_question}/{self.qty_question}')

        self.choose_answer_1.setCheckState('1' in now_quest.choosen_var and not self.active == Status.test)
        self.choose_answer_2.setCheckState('2' in now_quest.choosen_var and not self.active == Status.test)
        self.choose_answer_3.setCheckState('3' in now_quest.choosen_var and not self.active == Status.test)
        self.choose_answer_4.setCheckState('4' in now_quest.choosen_var and not self.active == Status.test)

        if self.active in [Status.view, Status.hist]:
            for itm in self.answer_var_list:
                if itm[0] in now_quest.choosen_var and itm[0] not in now_quest.right_answers:
                    itm[1].setStyleSheet(self.red_style)
                else:
                    itm[1].setStyleSheet(self.dafault_style)

    def get_answer(self):

        data = []
        if self.choose_answer_1.isChecked(): data.append('1')
        if self.choose_answer_2.isChecked(): data.append('2')
        if self.choose_answer_3.isChecked(): data.append('3')
        if self.choose_answer_4.isChecked(): data.append('4')

        return data


if __name__ == "__main__":
    import main
