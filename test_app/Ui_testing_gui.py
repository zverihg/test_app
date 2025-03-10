# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\user\Desktop\testing_app\test_app\testing_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1154, 721)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("width:100%;")
        self.centralwidget.setObjectName("centralwidget")
        self.main_layout = QtWidgets.QGroupBox(self.centralwidget)
        self.main_layout.setEnabled(True)
        self.main_layout.setGeometry(QtCore.QRect(0, 0, 1171, 721))
        self.main_layout.setAutoFillBackground(False)
        self.main_layout.setStyleSheet("")
        self.main_layout.setTitle("")
        self.main_layout.setObjectName("main_layout")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.main_layout)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(250, 290, 651, 159))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fio_label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.fio_label.setFont(font)
        self.fio_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.fio_label.setObjectName("fio_label")
        self.horizontalLayout.addWidget(self.fio_label)
        self.fio_input = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fio_input.sizePolicy().hasHeightForWidth())
        self.fio_input.setSizePolicy(sizePolicy)
        self.fio_input.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.fio_input.setFont(font)
        self.fio_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.fio_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px;\n"
"font: 19pt \"MS Shell Dlg 2\";")
        self.fio_input.setEditable(True)
        self.fio_input.setObjectName("fio_input")
        self.horizontalLayout.addWidget(self.fio_input)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.test_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test_button.sizePolicy().hasHeightForWidth())
        self.test_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.test_button.setFont(font)
        self.test_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.test_button.setStyleSheet("    QPushButton {\n"
"        background-color: #0171CA;\n"
"        color: rgb(255, 255, 255);\n"
"        border-radius: 10px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: rgba(0,0,0,0);\n"
"        color: #3a7999;\n"
"         border : 2px solid ;\n"
"        border-color: #0171CA;\n"
"    }")
        self.test_button.setObjectName("test_button")
        self.verticalLayout_2.addWidget(self.test_button)
        self.result_button = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(19)
        self.result_button.setFont(font)
        self.result_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.result_button.setStyleSheet("    QPushButton {\n"
"        background-color: #0171CA;\n"
"        color: rgb(255, 255, 255);\n"
"        border-radius: 10px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: rgba(0,0,0,0);\n"
"        color: #3a7999;\n"
"         border : 2px solid ;\n"
"        border-color: #0171CA;\n"
"    }")
        self.result_button.setObjectName("result_button")
        self.verticalLayout_2.addWidget(self.result_button)
        self.test_menu = QtWidgets.QGroupBox(self.centralwidget)
        self.test_menu.setGeometry(QtCore.QRect(0, 0, 1171, 721))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test_menu.sizePolicy().hasHeightForWidth())
        self.test_menu.setSizePolicy(sizePolicy)
        self.test_menu.setMaximumSize(QtCore.QSize(999999, 99999))
        self.test_menu.setAutoFillBackground(False)
        self.test_menu.setStyleSheet("")
        self.test_menu.setTitle("")
        self.test_menu.setAlignment(QtCore.Qt.AlignCenter)
        self.test_menu.setObjectName("test_menu")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.test_menu)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(330, 150, 511, 301))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dezh_po_chasti = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.dezh_po_chasti.setMinimumSize(QtCore.QSize(309, 68))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.dezh_po_chasti.setFont(font)
        self.dezh_po_chasti.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dezh_po_chasti.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dezh_po_chasti.setStyleSheet("    QPushButton {\n"
"        background-color: #0171CA;\n"
"        color: rgb(255, 255, 255);\n"
"        border-radius: 10px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: rgba(0,0,0,0);\n"
"        color: #3a7999;\n"
"         border : 2px solid ;\n"
"        border-color: #0171CA;\n"
"    }")
        self.dezh_po_chasti.setFlat(False)
        self.dezh_po_chasti.setObjectName("dezh_po_chasti")
        self.verticalLayout.addWidget(self.dezh_po_chasti)
        self.pom_dezh_po_chasti = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pom_dezh_po_chasti.setMinimumSize(QtCore.QSize(0, 68))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pom_dezh_po_chasti.setFont(font)
        self.pom_dezh_po_chasti.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pom_dezh_po_chasti.setStyleSheet("    QPushButton {\n"
"        background-color: #0171CA;\n"
"        color: rgb(255, 255, 255);\n"
"        border-radius: 10px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: rgba(0,0,0,0);\n"
"        color: #3a7999;\n"
"         border : 2px solid ;\n"
"        border-color: #0171CA;\n"
"    }")
        self.pom_dezh_po_chasti.setObjectName("pom_dezh_po_chasti")
        self.verticalLayout.addWidget(self.pom_dezh_po_chasti)
        self.instructions_DPCH_PDT = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.instructions_DPCH_PDT.setMinimumSize(QtCore.QSize(0, 68))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.instructions_DPCH_PDT.setFont(font)
        self.instructions_DPCH_PDT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.instructions_DPCH_PDT.setStyleSheet("    QPushButton {\n"
"        background-color: #0171CA;\n"
"        color: rgb(255, 255, 255);\n"
"        border-radius: 10px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: rgba(0,0,0,0);\n"
"        color: #3a7999;\n"
"         border : 2px solid ;\n"
"        border-color: #0171CA;\n"
"    }")
        self.instructions_DPCH_PDT.setObjectName("instructions_DPCH_PDT")
        self.verticalLayout.addWidget(self.instructions_DPCH_PDT)
        self.back_to_main_window = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.back_to_main_window.setMinimumSize(QtCore.QSize(0, 68))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.back_to_main_window.setFont(font)
        self.back_to_main_window.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_to_main_window.setStyleSheet("    QPushButton {\n"
"        background-color: #0171CA;\n"
"        color: rgb(255, 255, 255);\n"
"        border-radius: 10px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: rgba(0,0,0,0);\n"
"        color: #3a7999;\n"
"         border : 2px solid ;\n"
"        border-color: #0171CA;\n"
"    }")
        self.back_to_main_window.setObjectName("back_to_main_window")
        self.verticalLayout.addWidget(self.back_to_main_window)
        self.test_box = QtWidgets.QGroupBox(self.centralwidget)
        self.test_box.setGeometry(QtCore.QRect(0, 0, 1171, 721))
        self.test_box.setStyleSheet("")
        self.test_box.setTitle("")
        self.test_box.setObjectName("test_box")
        self.question_text = QtWidgets.QLabel(self.test_box)
        self.question_text.setGeometry(QtCore.QRect(80, 40, 1061, 131))
        self.question_text.setMinimumSize(QtCore.QSize(1061, 0))
        self.question_text.setMaximumSize(QtCore.QSize(1061, 16777215))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.question_text.setFont(font)
        self.question_text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.question_text.setText("")
        self.question_text.setWordWrap(True)
        self.question_text.setObjectName("question_text")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.test_box)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(80, 190, 1071, 461))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.question_list_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.question_list_layout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.question_list_layout.setContentsMargins(0, 0, 0, 0)
        self.question_list_layout.setSpacing(6)
        self.question_list_layout.setObjectName("question_list_layout")
        self.question_box_1 = QtWidgets.QHBoxLayout()
        self.question_box_1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.question_box_1.setObjectName("question_box_1")
        self.answer_var_1 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer_var_1.sizePolicy().hasHeightForWidth())
        self.answer_var_1.setSizePolicy(sizePolicy)
        self.answer_var_1.setMinimumSize(QtCore.QSize(1040, 108))
        self.answer_var_1.setMaximumSize(QtCore.QSize(950, 16777215))
        self.answer_var_1.setMouseTracking(False)
        self.answer_var_1.setAutoFillBackground(False)
        self.answer_var_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.answer_var_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.answer_var_1.setText("")
        self.answer_var_1.setTextFormat(QtCore.Qt.AutoText)
        self.answer_var_1.setWordWrap(True)
        self.answer_var_1.setObjectName("answer_var_1")
        self.question_box_1.addWidget(self.answer_var_1)
        self.choose_answer_1 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_answer_1.sizePolicy().hasHeightForWidth())
        self.choose_answer_1.setSizePolicy(sizePolicy)
        self.choose_answer_1.setMaximumSize(QtCore.QSize(16, 16777215))
        self.choose_answer_1.setText("")
        self.choose_answer_1.setObjectName("choose_answer_1")
        self.question_box_1.addWidget(self.choose_answer_1)
        self.question_list_layout.addLayout(self.question_box_1)
        self.question_box_2 = QtWidgets.QHBoxLayout()
        self.question_box_2.setObjectName("question_box_2")
        self.answer_var_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer_var_2.sizePolicy().hasHeightForWidth())
        self.answer_var_2.setSizePolicy(sizePolicy)
        self.answer_var_2.setMinimumSize(QtCore.QSize(1040, 108))
        self.answer_var_2.setMaximumSize(QtCore.QSize(950, 16777215))
        self.answer_var_2.setMouseTracking(True)
        self.answer_var_2.setAutoFillBackground(False)
        self.answer_var_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.answer_var_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.answer_var_2.setText("")
        self.answer_var_2.setTextFormat(QtCore.Qt.AutoText)
        self.answer_var_2.setWordWrap(True)
        self.answer_var_2.setObjectName("answer_var_2")
        self.question_box_2.addWidget(self.answer_var_2)
        self.choose_answer_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_answer_2.sizePolicy().hasHeightForWidth())
        self.choose_answer_2.setSizePolicy(sizePolicy)
        self.choose_answer_2.setMaximumSize(QtCore.QSize(16, 16777215))
        self.choose_answer_2.setText("")
        self.choose_answer_2.setObjectName("choose_answer_2")
        self.question_box_2.addWidget(self.choose_answer_2)
        self.question_list_layout.addLayout(self.question_box_2)
        self.question_box_3 = QtWidgets.QHBoxLayout()
        self.question_box_3.setObjectName("question_box_3")
        self.answer_var_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer_var_3.sizePolicy().hasHeightForWidth())
        self.answer_var_3.setSizePolicy(sizePolicy)
        self.answer_var_3.setMinimumSize(QtCore.QSize(1040, 108))
        self.answer_var_3.setMaximumSize(QtCore.QSize(950, 16777215))
        self.answer_var_3.setAutoFillBackground(False)
        self.answer_var_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.answer_var_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.answer_var_3.setText("")
        self.answer_var_3.setTextFormat(QtCore.Qt.AutoText)
        self.answer_var_3.setWordWrap(True)
        self.answer_var_3.setObjectName("answer_var_3")
        self.question_box_3.addWidget(self.answer_var_3)
        self.choose_answer_3 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_answer_3.sizePolicy().hasHeightForWidth())
        self.choose_answer_3.setSizePolicy(sizePolicy)
        self.choose_answer_3.setMaximumSize(QtCore.QSize(16, 16777215))
        self.choose_answer_3.setText("")
        self.choose_answer_3.setObjectName("choose_answer_3")
        self.question_box_3.addWidget(self.choose_answer_3)
        self.question_list_layout.addLayout(self.question_box_3)
        self.question_box_4 = QtWidgets.QHBoxLayout()
        self.question_box_4.setObjectName("question_box_4")
        self.answer_var_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer_var_4.sizePolicy().hasHeightForWidth())
        self.answer_var_4.setSizePolicy(sizePolicy)
        self.answer_var_4.setMinimumSize(QtCore.QSize(1040, 108))
        self.answer_var_4.setMaximumSize(QtCore.QSize(950, 16777215))
        self.answer_var_4.setAutoFillBackground(False)
        self.answer_var_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.answer_var_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.answer_var_4.setText("")
        self.answer_var_4.setTextFormat(QtCore.Qt.AutoText)
        self.answer_var_4.setWordWrap(True)
        self.answer_var_4.setObjectName("answer_var_4")
        self.question_box_4.addWidget(self.answer_var_4)
        self.choose_answer_4 = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.choose_answer_4.sizePolicy().hasHeightForWidth())
        self.choose_answer_4.setSizePolicy(sizePolicy)
        self.choose_answer_4.setMaximumSize(QtCore.QSize(16, 16777215))
        self.choose_answer_4.setText("")
        self.choose_answer_4.setObjectName("choose_answer_4")
        self.question_box_4.addWidget(self.choose_answer_4)
        self.question_list_layout.addLayout(self.question_box_4)
        self.next_question = QtWidgets.QPushButton(self.test_box)
        self.next_question.setGeometry(QtCore.QRect(880, 660, 231, 41))
        self.next_question.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.next_question.setStyleSheet("    QPushButton {\n"
"        background-color: #0171CA;\n"
"        color: rgb(255, 255, 255);\n"
"        border-radius: 10px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: rgba(0,0,0,0);\n"
"        color: #3a7999;\n"
"         border : 2px solid ;\n"
"        border-color: #0171CA;\n"
"    }")
        self.next_question.setObjectName("next_question")
        self.qty_question_label = QtWidgets.QLabel(self.test_box)
        self.qty_question_label.setGeometry(QtCore.QRect(800, 670, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.qty_question_label.setFont(font)
        self.qty_question_label.setObjectName("qty_question_label")
        self.time_counter = QtWidgets.QLabel(self.test_box)
        self.time_counter.setGeometry(QtCore.QRect(440, 670, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.time_counter.setFont(font)
        self.time_counter.setText("")
        self.time_counter.setObjectName("time_counter")
        self.previous_question = QtWidgets.QPushButton(self.test_box)
        self.previous_question.setGeometry(QtCore.QRect(80, 660, 231, 41))
        self.previous_question.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.previous_question.setStyleSheet("    QPushButton {\n"
"        background-color: #0171CA;\n"
"        color: rgb(255, 255, 255);\n"
"        border-radius: 10px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: rgba(0,0,0,0);\n"
"        color: #3a7999;\n"
"         border : 2px solid ;\n"
"        border-color: #0171CA;\n"
"    }")
        self.previous_question.setObjectName("previous_question")
        self.test_result_box = QtWidgets.QGroupBox(self.centralwidget)
        self.test_result_box.setGeometry(QtCore.QRect(0, 0, 1171, 721))
        self.test_result_box.setStyleSheet("")
        self.test_result_box.setTitle("")
        self.test_result_box.setObjectName("test_result_box")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.test_result_box)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(250, 80, 681, 461))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.type_test_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.type_test_label.setFont(font)
        self.type_test_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.type_test_label.setObjectName("type_test_label")
        self.horizontalLayout_2.addWidget(self.type_test_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.time_wasted_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.time_wasted_label.setFont(font)
        self.time_wasted_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.time_wasted_label.setObjectName("time_wasted_label")
        self.horizontalLayout_6.addWidget(self.time_wasted_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.correct_answers_label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.correct_answers_label.setFont(font)
        self.correct_answers_label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.correct_answers_label.setObjectName("correct_answers_label")
        self.horizontalLayout_7.addWidget(self.correct_answers_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.get_export = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get_export.sizePolicy().hasHeightForWidth())
        self.get_export.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.get_export.setFont(font)
        self.get_export.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.get_export.setStyleSheet("    QPushButton {\n"
"        background-color: #0171CA;\n"
"        color: rgb(255, 255, 255);\n"
"        border-radius: 10px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: rgba(0,0,0,0);\n"
"        color: #3a7999;\n"
"         border : 2px solid ;\n"
"        border-color: #0171CA;\n"
"    }")
        self.get_export.setObjectName("get_export")
        self.verticalLayout_3.addWidget(self.get_export)
        self.get_result = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get_result.sizePolicy().hasHeightForWidth())
        self.get_result.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.get_result.setFont(font)
        self.get_result.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.get_result.setStyleSheet("    QPushButton {\n"
"        background-color: #0171CA;\n"
"        color: rgb(255, 255, 255);\n"
"        border-radius: 10px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: rgba(0,0,0,0);\n"
"        color: #3a7999;\n"
"         border : 2px solid ;\n"
"        border-color: #0171CA;\n"
"    }")
        self.get_result.setObjectName("get_result")
        self.verticalLayout_3.addWidget(self.get_result)
        self.back_main_menu = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.back_main_menu.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_main_menu.sizePolicy().hasHeightForWidth())
        self.back_main_menu.setSizePolicy(sizePolicy)
        self.back_main_menu.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.back_main_menu.setFont(font)
        self.back_main_menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_main_menu.setStyleSheet("    QPushButton {\n"
"        background-color: #0171CA;\n"
"        color: rgb(255, 255, 255);\n"
"        border-radius: 10px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: rgba(0,0,0,0);\n"
"        color: #3a7999;\n"
"         border : 2px solid ;\n"
"        border-color: #0171CA;\n"
"    }")
        self.back_main_menu.setObjectName("back_main_menu")
        self.verticalLayout_3.addWidget(self.back_main_menu)
        self.test_result_box_menue = QtWidgets.QGroupBox(self.centralwidget)
        self.test_result_box_menue.setGeometry(QtCore.QRect(0, 0, 1171, 721))
        self.test_result_box_menue.setStyleSheet("")
        self.test_result_box_menue.setTitle("")
        self.test_result_box_menue.setObjectName("test_result_box_menue")
        self.tests_list = QtWidgets.QListWidget(self.test_result_box_menue)
        self.tests_list.setGeometry(QtCore.QRect(30, 80, 371, 601))
        self.tests_list.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.tests_list.setObjectName("tests_list")
        self.folder_list = QtWidgets.QComboBox(self.test_result_box_menue)
        self.folder_list.setGeometry(QtCore.QRect(30, 20, 371, 41))
        self.folder_list.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.folder_list.setObjectName("folder_list")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.test_result_box_menue)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(430, 90, 681, 581))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.type_test_result = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.type_test_result.setFont(font)
        self.type_test_result.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.type_test_result.setText("")
        self.type_test_result.setObjectName("type_test_result")
        self.horizontalLayout_3.addWidget(self.type_test_result)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.time_wasted_result = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.time_wasted_result.setFont(font)
        self.time_wasted_result.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.time_wasted_result.setText("")
        self.time_wasted_result.setObjectName("time_wasted_result")
        self.horizontalLayout_8.addWidget(self.time_wasted_result)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.correct_answers_result = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.correct_answers_result.setFont(font)
        self.correct_answers_result.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"padding-left:10px")
        self.correct_answers_result.setText("")
        self.correct_answers_result.setObjectName("correct_answers_result")
        self.horizontalLayout_9.addWidget(self.correct_answers_result)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.get_export_result = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get_export_result.sizePolicy().hasHeightForWidth())
        self.get_export_result.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.get_export_result.setFont(font)
        self.get_export_result.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.get_export_result.setStyleSheet("    QPushButton {\n"
"        background-color: #0171CA;\n"
"        color: rgb(255, 255, 255);\n"
"        border-radius: 10px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: rgba(0,0,0,0);\n"
"        color: #3a7999;\n"
"         border : 2px solid ;\n"
"        border-color: #0171CA;\n"
"    }")
        self.get_export_result.setObjectName("get_export_result")
        self.verticalLayout_4.addWidget(self.get_export_result)
        self.get_result_from_result = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.get_result_from_result.sizePolicy().hasHeightForWidth())
        self.get_result_from_result.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.get_result_from_result.setFont(font)
        self.get_result_from_result.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.get_result_from_result.setStyleSheet("    QPushButton {\n"
"        background-color: #0171CA;\n"
"        color: rgb(255, 255, 255);\n"
"        border-radius: 10px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: rgba(0,0,0,0);\n"
"        color: #3a7999;\n"
"         border : 2px solid ;\n"
"        border-color: #0171CA;\n"
"    }")
        self.get_result_from_result.setObjectName("get_result_from_result")
        self.verticalLayout_4.addWidget(self.get_result_from_result)
        self.back_main_menu_result = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.back_main_menu_result.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_main_menu_result.sizePolicy().hasHeightForWidth())
        self.back_main_menu_result.setSizePolicy(sizePolicy)
        self.back_main_menu_result.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.back_main_menu_result.setFont(font)
        self.back_main_menu_result.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_main_menu_result.setStyleSheet("    QPushButton {\n"
"        background-color: #0171CA;\n"
"        color: rgb(255, 255, 255);\n"
"        border-radius: 10px;\n"
"    }\n"
"    QPushButton:hover {\n"
"        background: rgba(0,0,0,0);\n"
"        color: #3a7999;\n"
"         border : 2px solid ;\n"
"        border-color: #0171CA;\n"
"    }")
        self.back_main_menu_result.setObjectName("back_main_menu_result")
        self.verticalLayout_4.addWidget(self.back_main_menu_result)
        self.test_menu.raise_()
        self.test_result_box.raise_()
        self.test_result_box_menue.raise_()
        self.test_box.raise_()
        self.main_layout.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fio_label.setText(_translate("MainWindow", "Введите ФИО"))
        self.fio_input.setCurrentText(_translate("MainWindow", "Гость"))
        self.test_button.setText(_translate("MainWindow", "Тестирование"))
        self.result_button.setText(_translate("MainWindow", "Просмотр результатов"))
        self.dezh_po_chasti.setText(_translate("MainWindow", "Дежурный по части"))
        self.pom_dezh_po_chasti.setText(_translate("MainWindow", "Помошник дежурного"))
        self.instructions_DPCH_PDT.setText(_translate("MainWindow", "Инструкции ДПЧ и ПДТ"))
        self.back_to_main_window.setText(_translate("MainWindow", "Назад"))
        self.next_question.setText(_translate("MainWindow", "Следующий вопрос"))
        self.qty_question_label.setText(_translate("MainWindow", "0/0"))
        self.previous_question.setText(_translate("MainWindow", "Предыдущий вопрос"))
        self.label.setText(_translate("MainWindow", "Тип теста"))
        self.type_test_label.setText(_translate("MainWindow", "Тип теста"))
        self.label_2.setText(_translate("MainWindow", "Время"))
        self.time_wasted_label.setText(_translate("MainWindow", "Тип теста"))
        self.label_6.setText(_translate("MainWindow", "Правильных ответов"))
        self.correct_answers_label.setText(_translate("MainWindow", "Тип теста"))
        #self.get_export.setText(_translate("MainWindow", "Выгрузить Отчёт"))
        self.get_export.hide()
        self.get_result.setText(_translate("MainWindow", "Посмотреть результат"))
        self.back_main_menu.setText(_translate("MainWindow", "Вернуться в меню"))
        self.label_3.setText(_translate("MainWindow", "Тип теста"))
        self.label_4.setText(_translate("MainWindow", "Время"))
        self.label_7.setText(_translate("MainWindow", "Правильных ответов"))
        #self.get_export_result.setText(_translate("MainWindow", "Выгрузить Отчёт"))
        self.get_export_result.hide()
        self.get_result_from_result.setText(_translate("MainWindow", "Посмотреть результат"))
        self.back_main_menu_result.setText(_translate("MainWindow", "Вернуться в меню"))
