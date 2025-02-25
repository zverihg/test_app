@echo off
cd ./test_app
pyinstaller --hidden-import PyQt5.QtCore  --hidden-import PyQt5.QtGui --hidden-import PyQt5.QtWidgets --hidden-import Ui_testing_gui --hidden-import question_gui --hidden-import PyQt5 -w --onefile -i "i.png" --add-data "i.png:." main.py
copy dist\main.exe ..\compiled_apps\Test.exe

cd ../test_creator
pyinstaller --hidden-import PyQt5.QtCore --hidden-import PyQt5.QtGui --hidden-import PyQt5.QtWidgets --hidden-import Ui_main --hidden-import PyQt5 -w --onefile -i "i.png" --add-data "i.png:." main.py
copy dist\main.exe ..\compiled_apps\Cofigurator.exe

cd ../test_admin
pyinstaller --hidden-import PyQt5.QtCore --hidden-import PyQt5.QtGui --hidden-import PyQt5.QtWidgets --hidden-import Ui_admin --hidden-import PyQt5 --hidden-import question_gui --hidden-import fpdf -w --onefile -i "i.png" --add-data "i.png:." --add-data "DejaVuSansCondensed.ttf:." admin.py
copy dist\admin.exe ..\compiled_apps\Admin.exe

cd ..
pause
