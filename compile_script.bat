@echo off
cd ./test_app
pyinstaller --hidden-import PyQt5.QtCore  --hidden-import PyQt5.QtGui --hidden-import PyQt5.QtWidgets --hidden-import Ui_testing_gui --hidden-import question_gui --hidden-import question_data --hidden-import PyQt5 -w --onefile -i "i.png" --add-data "i.png:." --add-data "DejaVuSansCondensed.ttf:." main.py
copy dist\main.exe ..\compiled_apps\Test.exe

cd ../test_creator
pyinstaller --hidden-import PyQt5.QtCore --hidden-import PyQt5.QtGui --hidden-import PyQt5.QtWidgets --hidden-import Ui_main --hidden-import PyQt5 -w --onefile -i "i.png" --add-data "i.png:." main.py

copy dist\main.exe ..\compiled_apps\Cofigurator.exe
cd ..
pause
