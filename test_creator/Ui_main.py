# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\user\Desktop\testing_app\test_creator\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1329, 789)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 1331, 791))
        self.groupBox.setStyleSheet("background-color: #EFEFF2;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.list_questions = QtWidgets.QListWidget(self.groupBox)
        self.list_questions.setGeometry(QtCore.QRect(10, 50, 321, 611))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.list_questions.setFont(font)
        self.list_questions.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.list_questions.setObjectName("list_questions")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(350, 20, 961, 751))
        self.groupBox_2.setStyleSheet("border:none")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.test_question = QtWidgets.QLineEdit(self.groupBox_2)
        self.test_question.setGeometry(QtCore.QRect(0, 0, 951, 71))
        self.test_question.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.test_question.setInputMask("")
        self.test_question.setObjectName("test_question")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, 86, 951, 661))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.answer_1 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.answer_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.answer_1.setObjectName("answer_1")
        self.horizontalLayout.addWidget(self.answer_1)
        self.choose_1 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_1.sizePolicy().hasHeightForWidth())
        self.choose_1.setSizePolicy(sizePolicy)
        self.choose_1.setStyleSheet("")
        self.choose_1.setText("")
        self.choose_1.setObjectName("choose_1")
        self.horizontalLayout.addWidget(self.choose_1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.answer_2 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.answer_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.answer_2.setObjectName("answer_2")
        self.horizontalLayout_7.addWidget(self.answer_2)
        self.choose_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.choose_2.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(200)
        self.choose_2.setFont(font)
        self.choose_2.setStyleSheet("")
        self.choose_2.setText("")
        self.choose_2.setObjectName("choose_2")
        self.horizontalLayout_7.addWidget(self.choose_2)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.answer_3 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.answer_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.answer_3.setObjectName("answer_3")
        self.horizontalLayout_2.addWidget(self.answer_3)
        self.choose_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.choose_3.setStyleSheet("")
        self.choose_3.setText("")
        self.choose_3.setObjectName("choose_3")
        self.horizontalLayout_2.addWidget(self.choose_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.answer_4 = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.answer_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.answer_4.setObjectName("answer_4")
        self.horizontalLayout_3.addWidget(self.answer_4)
        self.choose_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.choose_4.setStyleSheet("")
        self.choose_4.setText("")
        self.choose_4.setObjectName("choose_4")
        self.horizontalLayout_3.addWidget(self.choose_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.add_new_question = QtWidgets.QPushButton(self.groupBox)
        self.add_new_question.setGeometry(QtCore.QRect(10, 680, 151, 41))
        self.add_new_question.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_new_question.setStyleSheet("background-color: #0171CA;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.add_new_question.setObjectName("add_new_question")
        self.delete_curent_question = QtWidgets.QPushButton(self.groupBox)
        self.delete_curent_question.setGeometry(QtCore.QRect(170, 680, 161, 41))
        self.delete_curent_question.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_curent_question.setStyleSheet("background-color: #0171CA;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.delete_curent_question.setObjectName("delete_curent_question")
        self.save_curent_question = QtWidgets.QPushButton(self.groupBox)
        self.save_curent_question.setGeometry(QtCore.QRect(10, 730, 321, 41))
        self.save_curent_question.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_curent_question.setStyleSheet("background-color: #0171CA;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.save_curent_question.setObjectName("save_curent_question")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(16, 23, 311, 21))
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("text-align: center;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.test_question.setPlaceholderText(_translate("MainWindow", "Введите вопрос"))
        self.answer_1.setPlaceholderText(_translate("MainWindow", "Введите ответ и выберите верные"))
        self.answer_2.setPlaceholderText(_translate("MainWindow", "Введите ответ и выберите верные"))
        self.answer_3.setPlaceholderText(_translate("MainWindow", "Введите ответ и выберите верные"))
        self.answer_4.setPlaceholderText(_translate("MainWindow", "Введите ответ и выберите верные"))
        self.add_new_question.setText(_translate("MainWindow", "новый вопрос"))
        self.delete_curent_question.setText(_translate("MainWindow", "удалить вопрос"))
        self.save_curent_question.setText(_translate("MainWindow", "сохранить вопрос"))
        self.label.setText(_translate("MainWindow", "Список вопросов"))
