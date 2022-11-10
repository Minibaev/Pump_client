# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autherization.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(658, 493)
        Login.setStyleSheet("background-color: rgb(164, 254, 255);")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Login)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 410, 641, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.Create = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Create.setFont(font)
        self.Create.setStyleSheet("background-color: rgb(29, 255, 44);")
        self.Create.setObjectName("Create")
        self.horizontalLayout_1.addWidget(self.Create)
        self.Cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Cancel.setFont(font)
        self.Cancel.setStyleSheet("background-color: rgb(255, 33, 55);")
        self.Cancel.setObjectName("Cancel")
        self.horizontalLayout_1.addWidget(self.Cancel)
        self.gridLayoutWidget = QtWidgets.QWidget(Login)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 641, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_1 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_1.setObjectName("gridLayout_1")
        self.horizontalLayout_email = QtWidgets.QHBoxLayout()
        self.horizontalLayout_email.setObjectName("horizontalLayout_email")
        self.email = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.email.setFont(font)
        self.email.setObjectName("email")
        self.horizontalLayout_email.addWidget(self.email)
        self.textBrowser_email = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_email.setObjectName("textBrowser_email")
        self.horizontalLayout_email.addWidget(self.textBrowser_email)
        self.gridLayout_1.addLayout(self.horizontalLayout_email, 3, 0, 1, 1)
        self.horizontalLayout_name = QtWidgets.QHBoxLayout()
        self.horizontalLayout_name.setObjectName("horizontalLayout_name")
        self.Name = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Name.setFont(font)
        self.Name.setObjectName("Name")
        self.horizontalLayout_name.addWidget(self.Name)
        self.textBrowser_name = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.textBrowser_name.setFont(font)
        self.textBrowser_name.setObjectName("textBrowser_name")
        self.horizontalLayout_name.addWidget(self.textBrowser_name)
        self.gridLayout_1.addLayout(self.horizontalLayout_name, 0, 0, 1, 1)
        self.horizontalLayout_nickname = QtWidgets.QHBoxLayout()
        self.horizontalLayout_nickname.setObjectName("horizontalLayout_nickname")
        self.Nickname = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Nickname.setFont(font)
        self.Nickname.setObjectName("Nickname")
        self.horizontalLayout_nickname.addWidget(self.Nickname)
        self.textBrowser_nickname = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_nickname.setObjectName("textBrowser_nickname")
        self.horizontalLayout_nickname.addWidget(self.textBrowser_nickname)
        self.gridLayout_1.addLayout(self.horizontalLayout_nickname, 2, 0, 1, 1)
        self.horizontalLayout_surname = QtWidgets.QHBoxLayout()
        self.horizontalLayout_surname.setObjectName("horizontalLayout_surname")
        self.surname = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.surname.setFont(font)
        self.surname.setObjectName("surname")
        self.horizontalLayout_surname.addWidget(self.surname)
        self.textBrowser_surname = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser_surname.setObjectName("textBrowser_surname")
        self.horizontalLayout_surname.addWidget(self.textBrowser_surname)
        self.gridLayout_1.addLayout(self.horizontalLayout_surname, 1, 0, 1, 1)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.Create.setText(_translate("Login", "Создать"))
        self.Cancel.setText(_translate("Login", "Отменить"))
        self.email.setText(_translate("Login", "Эл.почта:   "))
        self.Name.setText(_translate("Login", "Имя:           "))
        self.Nickname.setText(_translate("Login", "Прозвище:"))
        self.surname.setText(_translate("Login", "Фамилия: "))
