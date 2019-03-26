import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import REGIST
import Gladiat_Area
from PyQt5 import QtWidgets
import goto_server

import First_window  # Это наш конвертированный файл дизайна

class Start(QtWidgets.QMainWindow, First_window.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.Button_Enter.clicked.connect(self.Enter)  # Выполнить функцию browse_folder
                                                            # при нажатии кнопки
        self.Button_Reg.clicked.connect(self.Reg)
    ###############################################
    def Enter(self):
        Login = self.lineEdit_Login.text()
        Password = self.lineEdit_Password.text()
        User = [Login, Password]
        goto_server.Init(User)
        global window
        window = Gladiat_Area.INIT
##########################################################
    def Reg(self):
        global window
        window = REGIST.REG()  # Создаём объект класса ExampleApp
        window.show()  # Показываем окно
        self.close()