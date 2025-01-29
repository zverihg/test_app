#!/usr/bin/env python

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
import sys, os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import json
from datetime import datetime as dt
from Ui_testing_gui import Ui_MainWindow
from threading import Thread
from question_gui import Question_gui, Status
from question_data import Question_data
from time import sleep
from random import sample


class MainWindow(QtWidgets.QMainWindow):

    meta_data_test: dict = {}
    question_list:dict = {}
    question:Question_gui
    actual_test:str = ''
    start_test: dt = None
    screen_list:list = None
    result_data:dict = {}
    time_thread:Thread = None
    end_test:bool = False

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        os.makedirs('./result', exist_ok=True)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.screen_list = [
            self.ui.test_menu,
            self.ui.test_box,
            self.ui.test_result_box,
            self.ui.main_layout,
            self.ui.test_result_box_menue
        ]

        self._connect_clicks()
        self.question_data, self.meta_data_test = self.init_question_poll()
        self._go_to_screen(self.ui.main_layout)

        self.ui.folder_list.currentTextChanged.connect(self.change_list_tests)
        self.ui.tests_list.currentItemChanged.connect(self.get_test_result)

    def _connect_clicks(self):

        self.ui.test_button.clicked.connect(lambda: self._go_to_screen(self.ui.test_menu))
        self.ui.back_to_main_window.clicked.connect(lambda: self._go_to_screen(self.ui.main_layout))
        self.ui.back_main_menu.clicked.connect(lambda: self._go_to_screen(self.ui.main_layout))
        self.ui.back_main_menu_result.clicked.connect(lambda: self._go_to_screen(self.ui.main_layout))
        self.ui.result_button.clicked.connect(self.init_result_menue)

        self.ui.next_question.clicked.connect(self._set_next_question)
        self.ui.pom_dezh_po_chasti.clicked.connect(self.run_test_pomdezh_po_chasti)
        self.ui.get_result.clicked.connect(self.get_result_window)
        self.ui.get_result_from_result.clicked.connect(lambda: self.get_result_window(hist=True))

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

            with open(f'./result/{current_dir}/{curent_fil}', "r") as dta: question_result_data = json.load(dta)

            actual_test = question_result_data['actual_test']

            t = dt.strptime(question_result_data['total_time'],"%H:%M:%S.%f")

            total_time = f'{t.minute} Минут, {t.second} Секунд'
            self.ui.type_test_result.setText(self.meta_data_test[actual_test]['description'])
            self.ui.time_wasted_result.setText(total_time)
            self.ui.correct_answers_result.setText(f"{question_result_data['right_ans_qty']}/{len(question_result_data['question_data'])}")

        except: pass

    def change_list_tests(self):
        self.ui.tests_list.clear()
        dir = self.ui.folder_list.currentText()

        files = os.listdir(path=f'./result/{dir}')
        data_fil = [f for f in files if os.path.isfile(f'./result/{dir}/{f}')]
        self.ui.tests_list.addItems(data_fil)

    def init_result_menue(self):
        self.ui.folder_list.clear()
        self.result_data = {}
        self._go_to_screen(self.ui.test_result_box_menue)

        dirs = os.listdir(path='./result')

        self.ui.folder_list.addItems(dirs)

    def get_result_window(self, hist = False):

        if hist:
            test_path = f'./result/{self.ui.folder_list.currentText()}/{self.ui.tests_list.currentItem().text()}'
            with open(test_path, "r") as dta: question_data = json.load(dta)

            self.actual_test = question_data['actual_test']
            data = { self.actual_test: {} }

            for idx, data_quest in question_data['question_data'].items():
                data[self.actual_test][idx] = Question_data(idx, data_quest)

            self.question = Question_gui(self)
            self.question_data = data
            self.question.qty_question = len(self.question_data[self.actual_test])
            self.question.set_hist_mode()
        
        self._go_to_screen(self.ui.test_box)
        if not hist: self.question.set_view_mode()
        self.question.set_quest(data = self.question_data[self.actual_test])

    def _hide_all(self):
        for screen in self.screen_list: screen.hide()

    def _go_to_screen(self, screen):
        self._hide_all()
        screen.show()

    def question_data_to_dict(self, quests):

        data = {}

        for idx, quest in quests.items():
            data[idx] = {
                "id_question": quest.id_question,
                "question": quest.question,
                "answers": quest.answers,
                "right_answers": quest.right_answers,
                "choosen_var": quest.choosen_var,
                "answer_result": quest.answer_result,
            }
        return data

    def _end_test(self):
        self._go_to_screen(self.ui.test_result_box)
        self.question.reset_actual_question()

        if self.question.active == Status.test:

            end_test = dt.now()
            meta_quest = self.meta_data_test[self.actual_test]
            total_time = end_test - self.start_test
            self.ui.type_test_label.setText(meta_quest["description"])
            self.ui.time_wasted_label.setText(self._timedelta_formatter(total_time))
            right_ans_qty = 0
            for idx, quest in self.question_data[self.actual_test].items():
                if quest.answer_result: right_ans_qty += 1
            self.ui.correct_answers_label.setText(f"{right_ans_qty}/{self.question.qty_question}")

            if self.ui.fio_input.text() == "":  fio_dir = "Гость"
            else:                               fio_dir = self.ui.fio_input.text() 

            os.makedirs(f'./result/{fio_dir}', exist_ok=True)

            question_data_dict = self.question_data_to_dict(self.question_data[self.actual_test])

            res = {
                "start_test":str(self.start_test),
                "end_test":str(end_test),
                "total_time":str(total_time),
                "actual_test":self.actual_test,
                "right_ans_qty": right_ans_qty,
                "question_data":question_data_dict,
            }

            with open(f'./result/{fio_dir}/{self.actual_test}_{dt.now().strftime("%d_%M_%Y_%H_%M_%S")}.json', 'w') as fp:
                json.dump(res,fp)

        elif self.question.active == Status.hist:
            self._go_to_screen(self.ui.test_result_box_menue)

    def _set_next_question(self):

        id_question = self.question.get_actual_question()
        if self.question.active == Status.test:
            answer = self.question.get_answer()
            question = self.question_data[self.actual_test][str(id_question)]
            question.choosen_var = answer
            question.answer_result = question.choosen_var == question.right_answers

        if self.question.qty_question > id_question:
            self.question.set_quest(data = self.question_data[self.actual_test])
        else:
            self.end_test = True
            self._end_test()

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
            choises = sample(list(test['poll_questions'].keys()), 3)

            for idx, tst_key in enumerate(choises,start=1):
                data_quest = test['poll_questions'][tst_key]

                data[type_test][str(idx)] = Question_data(str(idx), data_quest)

        return data, meta_data_test

    def time_counter(self):
        self.end_test = False
        while True:
            sleep(1)
            tme = dt.now() - self.start_test
            self.ui.time_counter.setText(self._timedelta_formatter(tme))
            if tme.seconds >= self.meta_data_test[self.actual_test]['time']:
                self.end_test = False
                self._end_test()
                return 0
            if self.end_test: return 0 

    def run_test_pomdezh_po_chasti(self):

        self._go_to_screen(self.ui.test_box)

        self.question = Question_gui(self)
        self.question.set_test_mode()
        self.actual_test = "pomdezh_po_chasti"
        self.question.qty_question = len(self.question_data[self.actual_test])
        self.question.set_quest(self.question_data[self.actual_test])
        self.start_test = dt.now()
        self.time_thread = Thread(target=self.time_counter)
        self.time_thread.start()

app = QtWidgets.QApplication(sys.argv)
graf = MainWindow()
graf.show()

sys.exit(app.exec_())