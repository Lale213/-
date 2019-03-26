# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'First_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(275, 275))
        MainWindow.setMaximumSize(QtCore.QSize(275, 275))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.NAME_GAME = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.NAME_GAME.setFont(font)
        self.NAME_GAME.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.NAME_GAME.setTextFormat(QtCore.Qt.AutoText)
        self.NAME_GAME.setIndent(60)
        self.NAME_GAME.setObjectName("NAME_GAME")
        self.verticalLayout.addWidget(self.NAME_GAME)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Label_Login = QtWidgets.QLabel(self.centralwidget)
        self.Label_Login.setObjectName("Label_Login")
        self.horizontalLayout.addWidget(self.Label_Login)
        self.lineEdit_Login = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Login.setObjectName("lineEdit_Login")
        self.horizontalLayout.addWidget(self.lineEdit_Login)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Label_Password = QtWidgets.QLabel(self.centralwidget)
        self.Label_Password.setObjectName("Label_Password")
        self.horizontalLayout_2.addWidget(self.Label_Password)
        self.lineEdit_Password = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.horizontalLayout_2.addWidget(self.lineEdit_Password)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.Button_Enter = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Enter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Button_Enter.setObjectName("Button_Enter")
        self.verticalLayout.addWidget(self.Button_Enter)
        self.Button_Reg = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Reg.setObjectName("Button_Reg")
        self.verticalLayout.addWidget(self.Button_Reg)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gladiator Arena"))
        self.NAME_GAME.setText(_translate("MainWindow", "Gladiator Arena"))
        self.Label_Login.setText(_translate("MainWindow", "Login:      "))
        self.Label_Password.setText(_translate("MainWindow", "Password:"))
        self.Button_Enter.setText(_translate("MainWindow", "Enter"))
        self.Button_Reg.setText(_translate("MainWindow", "Reg"))

