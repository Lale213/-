from PyQt5 import QtWidgets
import Error_Massage
import Request1
import Area_Reg  # Это наш конвертированный файл дизайна
import goto_server
import First

class REG(QtWidgets.QMainWindow, Area_Reg.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.Bt_Register.clicked.connect(self.Regist)

    def Regist(self):
        Login = self.lineLogin.text()
        Password = self.linePassword.text()
        RPassword = self.lineRPassword.text()
        Class = self.lineClass.text()
        Level = '1'
        Exp = '0'
        Money = '0'
        Person = [Login, Password, Class, Level, Exp, Money]
        code = 0
        ip = Request1.Internet_ON()
        if (Class != "Var" and Class != "Archer" and Class != "Mage"):
            code = 3
        if (Password != RPassword):
            code=1
        if (Login == '' or Password == '' or RPassword == '' or Class == ''):
            code = 2
        if (ip == 0):
            code = 4
        if (code != 0):
            Error_Massage.ERROR(code)
        else:
            print(Person)
            result = goto_server.Reg(Person)
            if(result == 1):
                global window
                window = First.Start()
                window.show()
                self.close()
