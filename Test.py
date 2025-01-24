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







'''
    def ____init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        uic.loadUi('testing_gui.ui', self)

        layout = QGridLayout(self.groupBox_EQ)
        self.setLayout(layout)

        self.lst_flt.addItem('Полосовой 1')
        self.lst_flt.setFont(QFont('Times', 16)) 

        self.flt_add_pass.clicked.connect(self.add_flt_pass)
        self.flt_add_stop.clicked.connect(self.add_flt_stop)
        
        self.groupBox_COMP.hide()
        self.groupBox_EQ.hide()
        # self.groupBox_REV.hide()
        self.label.setFont(QFont('Times', 16)) 
        self.label.setText("ЧАСТОТА" )
        self.label_2.setFont(QFont('Times', 16)) 
        self.label_2.setText("ШИРИНА" )
        self.label_3.setFont(QFont('Times', 16)) 
        self.label_3.setText("ПОРЯДОК ФИЛЬТРА" )
        self.label_8.setFont(QFont('Times', 16)) 
        self.label_8.setText("ПОРОГ СРАБАОТЫВАНИЯ")
        self.label_9.setFont(QFont('Times', 16)) 
        self.label_9.setText("ПРОЦЕНТ ПРОПУСКАНИЯ")
        self.label_10.setFont(QFont('Times', 16)) 
        self.label_10.setText("УСИЛЕНИЕ")
              
        
        self.flt_del.setFont(QFont('Times', 16)) 
        self.flt_add_pass.setFont(QFont('Times', 16)) 
        self.flt_add_stop.setFont(QFont('Times', 16))
        self.pushButton_COMP.setFont(QFont('Times', 16))
        self.pushButton_EQ.setFont(QFont('Times', 16))
        self.pushButton.setFont(QFont('Times', 16))
        

        self.lst_flt.currentIndexChanged.connect(self.index_changed)
        self.checkBox_active.stateChanged.connect(self.set_active)
        self.pushButton_EQ.clicked.connect(self.POKAZHI)
        self.flt_del.clicked.connect(self.del_flt)
        
        self.pushButton_COMP.clicked.connect(self.COMP)
        self.dial_COMP_GAIN.valueChanged.connect(self.change)
        self.dial_COMP_LVL.valueChanged.connect(self.change)
        self.dial_COMP_PERC.valueChanged.connect(self.change)
        
        self.dialC.valueChanged.connect(self.change)
        self.dialW.valueChanged.connect(self.change)
        self.dialG.valueChanged.connect(self.set_gain)
       
        grid = QtWidgets.QGridLayout(self.centralwidget)
        self.GraphWidget.setYRange(0, 2 * np.pi * nFFT ** 2 / RATE * 10000)
        self.GraphWidget.setYRange(0, 70)
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.ris)
        self.timer.start()

    def COMP(self):
        if self.F_COMP:
            self.groupBox_COMP.hide()
            self.F_COMP=False
        else :
            self.groupBox_COMP.show()
            self.F_COMP=True

    def set_COMP(self,xx):
         
        b=max(xx)*(self.dial_COMP_LVL.value()/max(xx))/(self.dial_COMP_GAIN.value()*1000)
        
        self.label_COMP_GAIN.setText(f'{str(self.dial_COMP_GAIN.value())} db')
        self.label_COMP_GAIN.setFont(QFont('Times', 16))
        
        
        if max(xx)>=self.dial_COMP_LVL.value():  
            
            xx*=(self.dial_COMP_LVL.value()*self.dial_COMP_PERC.value()/100)/max(xx)
            
        self.label_COMP_LVL.setText(str((self.dial_COMP_LVL.value())))
        self.label_COMP_LVL.setFont(QFont('Times', 16))
        self.label_COMP_PERC.setText(f'{str(self.dial_COMP_PERC.value())} %')
        self.label_COMP_PERC.setFont(QFont('Times', 16))
            
        return xx

    def set_active(self): self.flt_dct[self.act_flt]['active'] = self.checkBox_active.isChecked()

    def del_flt(self):
        self.flt_dct.pop(self.act_flt)
        self.lst_flt.removeItem(self.act_flt)
        self.act_flt = self.lst_flt.currentIndex()
        # self.lst_flt.setCurrentIndex(self.flt_dct.keys()[-1])

    def index_changed(self, index):
        
        self.act_flt = index
        self.tpeflt = 1
        self.dialC.setValue(self.flt_dct[index]['C'])
        self.dialW.setValue(self.flt_dct[index]['W'])
        self.dialG.setValue(self.flt_dct[index]['gain'])
        self.checkBox_active.setChecked(self.flt_dct[self.act_flt]['active'])
        self.tpeflt = 0

    def set_gain(self):
        
        self.flt_dct[self.act_flt]['gain']=self.dialG.value()
        self.label_EQ_GAIN.setText(str(self.dialG.value()))
        self.label_EQ_GAIN.setFont(QFont('Times', 16))

    def add_flt_pass(self):
        
        self.act_flt+=1
        self.lst_flt.addItem(f'Полосовой {self.act_flt+ 1}')
        self.flt_dct[self.act_flt] ={ 'type': 'pass', 'R': 2250, 'L': 1750, 'C': 2000, 'W': 500, 'flt' : butter_bandpass_filter, 'gain':1,'active': True}
        self.lst_flt.setCurrentIndex(self.act_flt)
        self.checkBox_active.setChecked(True)

    def add_flt_stop(self):
        
        self.act_flt+=1
        self.lst_flt.addItem(f'Режекторный {self.act_flt + 1}')
        self.flt_dct[self.act_flt] ={ 'type': 'stop', 'R': 2250, 'L': 1750, 'C': 2000, 'W': 500, 'flt' : butter_bandstop_filter, 'gain':1,'active': True}
        self.lst_flt.setCurrentIndex(self.act_flt)
        self.checkBox_active.setChecked(True)

    def change(self):
        
        
        if self.tpeflt == 0:
            self.flt_dct[self.act_flt]['L']=self.dialC.value()-self.dialW.value()/2
            self.flt_dct[self.act_flt]['R']=self.dialC.value()+self.dialW.value()/2
            self.flt_dct[self.act_flt]['C']=self.dialC.value()
            self.flt_dct[self.act_flt]['W']=self.dialW.value()
            self.label_EQ_FREQ.setText(str(self.dialC.value()))
            self.label_EQ_FREQ.setFont(QFont('Times', 16))
            self.label_EQ_WIDE.setText(str(self.dialW.value()))
            self.label_EQ_WIDE.setFont(QFont('Times', 16))

    def EQ_PASS(self):
        self.SET_FLTR='pass_X'
        self.dialC.setValue(self.P_C)
        self.dialW.setValue(self.P_W) 
        self.SET_FLTR='pass'

    def EQ_STOP(self):
        self.SET_FLTR='stop_X'
        self.dialC.setValue(self.S_C)
        self.dialW.setValue(self.S_W)
        self.SET_FLTR='stop'

    def ris(self):
        y=self.animate_v2()
        dby = 10* np.log10(y/10)
        self.GraphWidget.clear()
        
        self.GraphWidget.plot(x_f,dby)
        
    def POKAZHI(self):
        if self.F_EQ:
            self.groupBox_EQ.hide()
            self.F_EQ=False
        else :
            self.groupBox_EQ.show()
            self.F_EQ=True

    def REV(self):
        if self.F_EQ:
            self.groupBox_REV.hide()
            self.F_EQ=False
        else :
            self.groupBox_REV.show()
            self.F_EQ=True

    def onStateChanged_PASS(self):  self.F_EQ_PASS=self.checkBox_PASS.isChecked()
   
    def onStateChanged_STOP(self):  self.F_EQ_STOP=self.checkBox_STOP.isChecked()

    def animate_v2(self):  
        N = int(max(stream.get_read_available() / nFFT, 1) * nFFT)
        data = stream.read(N)

        y = np.array(struct.unpack("%dh" % (N * CHANNELS), data)) / MAX_y*self.verticalSlider.value()
        
        y_L = y[::2]
        y_R = y[1::2]

        xx=np.array(y_L*MAX_y,"int16")

        xx = equalization_lowpass(xx, 15000)
        xx = equalization_highpass(xx, 100)
       

        if self.checkBox_COMP.isChecked():
                xx = self.set_COMP(xx)

        for idx, flt in self.flt_dct.items():
            if flt['active']: 
                xx = flt['flt'](xx,flt['L'] ,flt['R'] , RATE, 6, flt['gain']) 

        Y_L = np.fft.rfft(xx, nFFT)
        Y_R = np.fft.rfft(xx, nFFT)
    
        Y = abs(Y_R)[1::]
        
        YY=np.abs(np.fft.ifft(Y_R))*MAX_y
        
      
            
        stream_out.write(bytes(np.array(xx, 'int16')))
        
        return (Y)
'''

app = QtWidgets.QApplication(sys.argv)
graf = MainWindow()
graf.show()

sys.exit(app.exec_())