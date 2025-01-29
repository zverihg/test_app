
<h1 align="center">Приложение для тестирования</h1>
<h2> Приложение тестов</h2>

<p>Собрать приложение тестирования</p>

`pyinstaller --hidden-import PyQt5.QtCore --hidden-import PyQt5.QtGui --hidden-import PyQt5.QtWidgets --hidden-import Ui_testing_gui --hidden-import question_gui --hidden-import question_data --hidden-import PyQt5 --python=python3.12 -w  --onefile main.py"`
<h2> Приложение конфигуратора тестов</h2>
<p></p>Собрать приложение конфигуратора теста</p>

`pyinstaller --hidden-import PyQt5.QtCore --hidden-import PyQt5.QtGui --hidden-import PyQt5.QtWidgets --hidden-import Ui_main --hidden-import PyQt5 --python=python3.12 -w  --onefile main.py`
