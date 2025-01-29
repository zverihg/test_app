Собрать приложение тестирования
pyinstaller --hidden-import PyQt5.QtCore --hidden-import PyQt5.QtGui --hidden-import PyQt5.QtWidgets --hidden-import Ui_testing_gui --hidden-import question_gui --hidden-import question_data --hidden-import PyQt5 --python=python3.12 -w  --onefile main.py

Собрать приложение конфигуратора теста
Собрать pyinstaller --hidden-import PyQt5.QtCore --hidden-import PyQt5.QtGui --hidden-import PyQt5.QtWidgets --hidden-import Ui_main --hidden-import PyQt5 --python=python3.12 -w  --onefile main.py
