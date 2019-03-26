from PyQt5 import QtWidgets
import Error

def ERROR(code):
    if (code == 1):
        global window
        window = Error_1()  # пароли не совпадают
        window.show()  # Показываем окно
    if (code == 2):
        window = Error_2()  # пароли не совпадают
        window.show()
    if (code == 3):
        window = Error_3()  # неверно введен класс
        window.show()

    if (code == 4):
        window = Error_4()  # Нет подключения к сети
        window.show()
    if (code == 5):
        window = Error_5()  # Ошибка на сервере
        window.show()
    if (code == 6):
        window = Error_6()  # Пользователь с таким логином уже зарегистрирован
        window.show()

class Error_1(QtWidgets.QMainWindow, Error.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.OK.clicked.connect(self.close)
        self.labelErrorMassage.setText('Ошибка!\n\nВведены разные пароли.')

class Error_2(QtWidgets.QMainWindow, Error.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.OK.clicked.connect(self.close)
        self.labelErrorMassage.setText('Ошибка!\n\nНе все данные введены!')

class Error_3(QtWidgets.QMainWindow, Error.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.OK.clicked.connect(self.close)
        self.labelErrorMassage.setText('Ошибка!\n\nНеверно введен класс!')

class Error_4(QtWidgets.QMainWindow, Error.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.OK.clicked.connect(self.close)
        self.labelErrorMassage.setText('Ошибка!\n\nНет подключения к сети!')

class Error_5(QtWidgets.QMainWindow, Error.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.OK.clicked.connect(self.close)
        self.labelErrorMassage.setText('Ошибка!\n\nОшибка на сервере!')

class Error_6(QtWidgets.QMainWindow, Error.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.OK.clicked.connect(self.close)
        self.labelErrorMassage.setText('Ошибка!\n\nПользователь с таким логином уже зарегистрирован!')
