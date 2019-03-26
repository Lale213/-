# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Area_Reg.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        MainWindow.setMinimumSize(QtCore.QSize(500, 600))
        MainWindow.setMaximumSize(QtCore.QSize(500, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(500, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(500, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.archer_img = QtWidgets.QLabel(self.centralwidget)
        self.archer_img.setText("")
        self.archer_img.setPixmap(QtGui.QPixmap("../../../MyGame/archer.png"))
        self.archer_img.setObjectName("archer_img")
        self.gridLayout.addWidget(self.archer_img, 0, 1, 1, 1)
        self.mage_ing = QtWidgets.QLabel(self.centralwidget)
        self.mage_ing.setText("")
        self.mage_ing.setPixmap(QtGui.QPixmap("../../../MyGame/magic.png"))
        self.mage_ing.setObjectName("mage_ing")
        self.gridLayout.addWidget(self.mage_ing, 0, 2, 1, 1)
        self.var_img = QtWidgets.QLabel(self.centralwidget)
        self.var_img.setText("")
        self.var_img.setPixmap(QtGui.QPixmap("../../../MyGame/var.png"))
        self.var_img.setObjectName("var_img")
        self.gridLayout.addWidget(self.var_img, 0, 0, 1, 1)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.gridLayout.addWidget(self.plainTextEdit_3, 1, 2, 1, 1)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 1, 1, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.labelLogin = QtWidgets.QLabel(self.centralwidget)
        self.labelLogin.setObjectName("labelLogin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelLogin)
        self.lineLogin = QtWidgets.QLineEdit(self.centralwidget)
        self.lineLogin.setText("")
        self.lineLogin.setObjectName("lineLogin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineLogin)
        self.labelPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelPassword.setObjectName("labelPassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelPassword)
        self.linePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.linePassword.setText("")
        self.linePassword.setObjectName("linePassword")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.linePassword)
        self.labelRPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelRPassword.setObjectName("labelRPassword")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelRPassword)
        self.lineRPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineRPassword.setObjectName("lineRPassword")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineRPassword)
        self.labelClass = QtWidgets.QLabel(self.centralwidget)
        self.labelClass.setObjectName("labelClass")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelClass)
        self.lineClass = QtWidgets.QLineEdit(self.centralwidget)
        self.lineClass.setObjectName("lineClass")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineClass)
        self.horizontalLayout.addLayout(self.formLayout)
        self.Bt_Register = QtWidgets.QPushButton(self.centralwidget)
        self.Bt_Register.setObjectName("Bt_Register")
        self.horizontalLayout.addWidget(self.Bt_Register)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Area Reg"))
        self.plainTextEdit_3.setPlainText(_translate("MainWindow", "Великий маг! Знает множество заклинаний и проклятий. Если тебе повезет, то в лягушку ты не превратишься.\n"
"+20% к разуму.\n"
"Class: Mage"))
        self.plainTextEdit_2.setPlainText(_translate("MainWindow", "Меткий лучник! Он способен научить тебя многому: от попадания в мишень в упор, до убийств на скаку лошади сразу 3 противников одной стрелой.\n"
"+20% к ловкости.\n"
"Class: Archer"))
        self.plainTextEdit.setPlainText(_translate("MainWindow", "Доблестный воин! Прошёл не один десяток битв. Он готов стать твоим наставником.\n"
"+20% к атаке.\n"
"Class: Var"))
        self.labelLogin.setText(_translate("MainWindow", "Login:"))
        self.labelPassword.setText(_translate("MainWindow", "Password:"))
        self.labelRPassword.setText(_translate("MainWindow", "repeat password"))
        self.labelClass.setText(_translate("MainWindow", "Class"))
        self.Bt_Register.setText(_translate("MainWindow", "Register"))

