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
from time import sleep
from random import sample
from fpdf import FPDF
from enum import Enum

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
    dezh_po_chasti = "Дежурный по части"
    instructions_DPCH_PDT = "Инструкции по ДПЧ и ПДТ"

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
    start_test: dt = None
    screen_list:list = None
    result_data:dict = {}
    time_thread:Thread = None
    question_timeout_thread:Thread = None
    test_status:ThereadStatus = ThereadStatus.run

    last_fio:str=''
    last_file:str=''

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        os.makedirs('./result', exist_ok=True)
        os.makedirs('./export', exist_ok=True)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Приложение для администратора')
        self.setWindowIcon(QIcon(self._resource_path('i.png')))

        self.screen_list = [
            self.ui.test_menu,
            self.ui.test_box,
            self.ui.test_result_box,
            self.ui.main_layout,
            self.ui.test_result_box_menue
        ]

        self._connect_clicks()
        self._go_to_screen(self.ui.main_layout)

        self.ui.folder_list.currentTextChanged.connect(self.change_list_tests)
        self.ui.tests_list.currentItemChanged.connect(self.get_test_result)

        dirs = os.listdir(path='./result')
        self.ui.fio_input.addItems(dirs)

    def _resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def _onbin(self, a ): return ' '.join( format( ord(x), 'b') for x in ''.join( json.dumps( a ) ) )
    def _unbin(self, a ):	return json.loads( ''.join( chr( int( x, 2 ) ) for x in a.split(' ') ) )

    def _connect_clicks(self):

        self.ui.test_button.clicked.connect(lambda: self._go_to_screen(self.ui.test_menu))
        self.ui.back_to_main_window.clicked.connect(lambda: self._go_to_screen(self.ui.main_layout))
        self.ui.back_main_menu.clicked.connect(lambda: self._go_to_screen(self.ui.main_layout))
        self.ui.back_main_menu_result.clicked.connect(lambda: self._go_to_screen(self.ui.main_layout))
        self.ui.result_button.clicked.connect(self.init_result_menue)
        self.ui.next_question.clicked.connect(self._set_next_question)
        self.ui.previous_question.clicked.connect(self._set_prev_question)

        self.ui.pom_dezh_po_chasti.clicked.connect(self.run_test_pomdezh_po_chasti)
        self.ui.dezh_po_chasti.clicked.connect(self.run_test_dezh_po_chasti)
        self.ui.instructions_DPCH_PDT.clicked.connect(self.run_test_instructions_DPCH_PDT)

        self.ui.get_result.clicked.connect(self.get_result_window)
        self.ui.get_export_result.clicked.connect(lambda: self.get_report_preproc(True))
        self.ui.get_export.clicked.connect(lambda: self.get_report_preproc(False))
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

            with open(f'./result/{current_dir}/{curent_fil}', "r") as dta:
                question_bin_result_data = json.load(dta)
                question_result_data = self._unbin(question_bin_result_data)

            t = dt.strptime(question_result_data['total_time'],"%H:%M:%S.%f")

            total_time = f'{t.minute} Минут, {t.second} Секунд'
            self.ui.type_test_result.setText(question_result_data['description'])
            self.ui.time_wasted_result.setText(total_time)
            self.ui.correct_answers_result.setText(f"{question_result_data['right_ans_qty']}/{len(question_result_data['question_data'])}")

        except Exception as e:
            print(e)

    def change_list_tests(self):
        self.ui.tests_list.clear()
        dir = self.ui.folder_list.currentText()

        files = os.listdir(path=f'./result/{dir}')
        data_fil = [f for f in files if os.path.isfile(f'./result/{dir}/{f}')]
        self.ui.tests_list.addItems(data_fil)

        item = self.ui.tests_list.item(0)
        self.ui.tests_list.setCurrentItem(item)

    def init_result_menue(self):
        self.ui.folder_list.clear()
        self.result_data = {}
        self._go_to_screen(self.ui.test_result_box_menue)

        dirs = os.listdir(path='./result')

        self.ui.folder_list.addItems(dirs)

    def get_result_window(self, hist = False):

        if hist:
            test_path = f'./result/{self.ui.folder_list.currentText()}/{self.ui.tests_list.currentItem().text()}'
            with open(test_path, "r") as dta:
                question_bin_data = json.load(dta)
                question_data = self._unbin(question_bin_data)

            self.actual_test = question_data['actual_test']
            data = { self.actual_test: {} }

            for idx, data_quest in question_data['question_data'].items():
                self.question_pool[str(idx)] = QuestionPool(data_quest)

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
        self._go_to_screen(self.ui.test_result_box)
        self.question.reset_actual_question()

        if self.question.active == Status.test:

            end_test = dt.now()
            self.ui.type_test_label.setText(Actual_test[self.actual_test].value)

            total_time = end_test - self.start_test
            self.ui.time_wasted_label.setText(self._timedelta_formatter(total_time))
            right_ans_qty = 0
            for quest in self.question_pool.values():
                if quest.answer_result: right_ans_qty += 1
            self.ui.correct_answers_label.setText(f"{right_ans_qty}/{self.question.qty_question}")

            if self.ui.fio_input.currentText() == "":
                fio_dir = "Гость"
            else:
                fio_dir = self.ui.fio_input.currentText()

            os.makedirs(f'./result/{fio_dir}', exist_ok=True)

            question_data_dict = self.question_data_to_dict(self.question_pool)

            if right_ans_qty >=8:
                grade = 5
            elif right_ans_qty < 8 and right_ans_qty >= 6:
                grade = 4
            elif right_ans_qty < 6 and right_ans_qty >= 5:
                grade = 3
            else:
                grade = 2

            res = {
                "start_test":str(self.start_test),
                "end_test":str(end_test),
                "total_time":str(total_time),
                "actual_test":self.actual_test,
                "right_ans_qty": right_ans_qty,
                "question_data":question_data_dict,
                "fio": fio_dir,
                "grade": grade,
                "date": str(dt.now()),
                'description': Actual_test[self.actual_test].value
            }

            self.last_fio = fio_dir
            self.last_file = f'{Actual_test[self.actual_test].value}_{fio_dir}_{dt.now().strftime("%d_%M_%Y_%H_%M_%S")}.json'

            with open(f'./result/{self.last_fio}/{self.last_file}', 'w') as fp:
                json.dump(self._onbin(res),fp)

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
            if delta.seconds >= 30:
                if self.test_status == ThereadStatus.stop:
                    return 0
                else:
                    self.test_status = ThereadStatus.timeout
                    self._set_next_question()
                    return 0

            self.ui.time_counter.setText(f'На вопрос осталось {30 - delta.seconds} секунд')

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
            question:QuestionPool = self.question_pool[str(id_question)]
            question.choosen_var = answer
            question.answer_result = question.choosen_var == question.right_answers
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

        with open('./config.json', 'r') as fil:
            bin_data = json.load(fil)
            data = self._unbin(bin_data)

        if len(data.keys()) >= 10:
            choises = sample(list(data.keys()), 10)
        else:
            choises = sample(list(data.keys()), len(data.keys()))

        for idx, key in enumerate(choises,start=1):

            tmp = data[key]
            tmp['id_question'] = str(idx)
            self.question_pool[str(idx)] = QuestionPool(tmp)

        self.qty_question = len(self.question_pool)

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
        self.actual_test = "pomdezh_po_chasti"
        self._run_test()

    def run_test_dezh_po_chasti(self):
        self.actual_test = "dezh_po_chasti"
        self._run_test()

    def run_test_instructions_DPCH_PDT(self):
        self.actual_test = "instructions_DPCH_PDT"
        self._run_test()

    def _get_report(self):

        with open(f'./result/{self.last_fio}/{self.last_file}', 'r') as fil:
            bin_data = json.load(fil)
            question_data = self._unbin(bin_data)

        type_test =  Actual_test[question_data['actual_test']].value

        t = dt.strptime(question_data['total_time'],"%H:%M:%S.%f")
        total_time = f'{t.minute} Минут, {t.second} Секунд'

        test_date = dt.strptime(question_data['date'],"%Y-%m-%d %H:%M:%S.%f")
        test_date_str = test_date.strftime("%Y-%m-%d %H:%M:%S")
        pdf = FPDF()
        pdf.add_page()

        pdf.add_font('DejaVu', '', self._resource_path('DejaVuSansCondensed.ttf'), uni=True)
        pdf.set_font("DejaVu", size=14)
        pdf.cell(200, 10, txt="Отчёт по тесту", ln=1, align="C")
        pdf.set_font("DejaVu", size=12)
        pdf.cell(200, 10, txt=f"ФИО: {question_data['fio']}", ln=1, align="L")
        pdf.cell(200, 10, txt=f"Тип теста: {type_test}", ln=1, align="L")
        pdf.cell(200, 10, txt=f"Дата: {test_date_str}", ln=1, align="L")
        pdf.cell(200, 10, txt=f"Время теста: {total_time}", ln=1, align="L")
        pdf.cell(200, 10, txt=f"Количество правильных ответов: {question_data['right_ans_qty']}", ln=1, align="L")

        for idx, question in question_data['question_data'].items():

            if not question['answer_result']:
                pdf.set_text_color(255, 0, 0)
            else:
                pdf.set_text_color(0, 0, 0)

            pdf.set_font("DejaVu", size=14)

            pdf.cell(200, 10, txt="", ln=1, align="C")
            pdf.cell(200, 10, txt=f"Вопрос: {idx}", ln=1, align="C")
            pdf.cell(200, 10, txt=question['question'], ln=1, align="C")

            pdf.set_font("DejaVu", size=12)

            for ans_idx, ans_val in question['answers'].items():

                if ans_idx in question['choosen_var']:
                    if ans_idx not in question['right_answers']:
                        pdf.set_text_color(255, 0, 0)
                    else:
                        pdf.set_text_color(0, 0, 0)
                else:
                    pdf.set_text_color(0, 0, 0)

                pdf.multi_cell(0, 10, txt=f"{ans_val}", align="L")

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
