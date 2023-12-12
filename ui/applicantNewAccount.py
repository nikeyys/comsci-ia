# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'applicantNewAccount.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(280, 338)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 304))
        self.layoutWidget.setObjectName("layoutWidget")
        self.vLayout_newAcc = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.vLayout_newAcc.setContentsMargins(0, 0, 0, 0)
        self.vLayout_newAcc.setObjectName("vLayout_newAcc")
        self.lbl_accCreation = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_accCreation.setFont(font)
        self.lbl_accCreation.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_accCreation.setObjectName("lbl_accCreation")
        self.vLayout_newAcc.addWidget(self.lbl_accCreation)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vLayout_newAcc.addItem(spacerItem)
        self.vLayout_username = QtWidgets.QVBoxLayout()
        self.vLayout_username.setObjectName("vLayout_username")
        self.lbl_username = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_username.setObjectName("lbl_username")
        self.vLayout_username.addWidget(self.lbl_username)
        self.line_username = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_username.setObjectName("line_username")
        self.vLayout_username.addWidget(self.line_username)
        self.vLayout_newAcc.addLayout(self.vLayout_username)
        spacerItem1 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vLayout_newAcc.addItem(spacerItem1)
        self.vLayout_password = QtWidgets.QVBoxLayout()
        self.vLayout_password.setObjectName("vLayout_password")
        self.lbl_password = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_password.setObjectName("lbl_password")
        self.vLayout_password.addWidget(self.lbl_password)
        self.line_password = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password.setObjectName("line_password")
        self.vLayout_password.addWidget(self.line_password)
        self.vLayout_newAcc.addLayout(self.vLayout_password)
        self.vLayout_confirmPassword = QtWidgets.QVBoxLayout()
        self.vLayout_confirmPassword.setObjectName("vLayout_confirmPassword")
        self.lbl_confirmPassword = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_confirmPassword.setObjectName("lbl_confirmPassword")
        self.vLayout_confirmPassword.addWidget(self.lbl_confirmPassword)
        self.line_confirmPassword = QtWidgets.QLineEdit(self.layoutWidget)
        self.line_confirmPassword.setObjectName("line_confirmPassword")
        self.vLayout_confirmPassword.addWidget(self.line_confirmPassword)
        self.vLayout_newAcc.addLayout(self.vLayout_confirmPassword)
        self.checkbox_showPassword = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkbox_showPassword.setObjectName("checkbox_showPassword")
        self.vLayout_newAcc.addWidget(self.checkbox_showPassword)
        self.hLayout_buttons = QtWidgets.QHBoxLayout()
        self.hLayout_buttons.setObjectName("hLayout_buttons")
        self.btn_cancel = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_cancel.setObjectName("btn_cancel")
        self.hLayout_buttons.addWidget(self.btn_cancel)
        self.btn_createAcc = QtWidgets.QPushButton(self.layoutWidget)
        self.btn_createAcc.setObjectName("btn_createAcc")
        self.hLayout_buttons.addWidget(self.btn_createAcc)
        self.vLayout_newAcc.addLayout(self.hLayout_buttons)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Create a New Account"))
        self.lbl_accCreation.setText(_translate("MainWindow", "Account Creation"))
        self.lbl_username.setText(_translate("MainWindow", "Username"))
        self.lbl_password.setText(_translate("MainWindow", "Password"))
        self.lbl_confirmPassword.setText(_translate("MainWindow", "Confirm Password"))
        self.checkbox_showPassword.setText(_translate("MainWindow", "Show Password"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancel"))
        self.btn_createAcc.setText(_translate("MainWindow", "Create Account"))
