
<h1 align="center">Приложение для тестирования</h1>
<h2> Приложение тестов</h2>

<p>Собрать приложение тестирования</p>

<p>Перейти в test_app директорию</p>

`cd test_app`

<p>Далее выполнить</p>

`pyinstaller --hidden-import PyQt5.QtCore --hidden-import PyQt5.QtGui --hidden-import PyQt5.QtWidgets --hidden-import Ui_testing_gui --hidden-import question_gui --hidden-import question_data --hidden-import PyQt5 --python=python3.12 -w  --onefile -i "i.png" --add-data "i.png:." main.py`

<p>В директории test_app/dist появится main.exe</p>
<p>main.exe можно назвать по своему</p>
<h2> Приложение конфигуратора тестов</h2>
<p></p>Собрать приложение конфигуратора теста</p>
<p>Перейти в test_creator директорию</p>

`cd test_creator`

<p>Далее выполнить</p>

`pyinstaller --hidden-import PyQt5.QtCore --hidden-import PyQt5.QtGui --hidden-import PyQt5.QtWidgets --hidden-import Ui_main --hidden-import PyQt5 -w  --onefile -i "i.png" --add-data "i.png:." main.py`

<p>В директории test_creator/dist появится main.exe</p>
<p>main.exe можно назвать по своему</p>

<h2>!!! Важно  !!!</h2>

<h3>Зависимости</h3>

    -python 3.8
    -pyinstaller
    -PyQt5

<p>Установка библиотек</p>

`pip install PyQt5 pyinstaller`

<h3>Струткура файлов</h3>

<p>Рядом с приложением тестирования должен находиться json файл с конфигурацией тестов</p>

<p>при прохождении тестов будет появляться директория result</p>

<p>В этой директории будут директории и тестируемыми. Если не ввели ФИО будет просто Гость</p>

<p>В этих директориях будут данные о пройденых тестах</p>


<p>TODO разобраться с border-radius combobox. Проверить все ещё раз. Убрать лишние файлы как шрифты</p>
