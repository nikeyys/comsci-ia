# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adminRegisterManager.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 260)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 331, 223))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.vLayout_registerNewManager = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.vLayout_registerNewManager.setContentsMargins(0, 0, 0, 0)
        self.vLayout_registerNewManager.setObjectName("vLayout_registerNewManager")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.vLayout_registerNewManager.addWidget(self.label)
        self.fLayout_registerManager = QtWidgets.QFormLayout()
        self.fLayout_registerManager.setObjectName("fLayout_registerManager")
        self.label_firstName = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_firstName.setObjectName("label_firstName")
        self.fLayout_registerManager.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_firstName)
        self.line_firstName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_firstName.setObjectName("line_firstName")
        self.fLayout_registerManager.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_firstName)
        self.labe_surname = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.labe_surname.setObjectName("labe_surname")
        self.fLayout_registerManager.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labe_surname)
        self.line_surname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_surname.setObjectName("line_surname")
        self.fLayout_registerManager.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_surname)
        self.label_username = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_username.setObjectName("label_username")
        self.fLayout_registerManager.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_username)
        self.line_username = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_username.setObjectName("line_username")
        self.fLayout_registerManager.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_username)
        self.label_password = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_password.setObjectName("label_password")
        self.fLayout_registerManager.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_password)
        self.line_password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password.setObjectName("line_password")
        self.fLayout_registerManager.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line_password)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.fLayout_registerManager.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.combo_permission = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.combo_permission.setObjectName("combo_permission")
        self.combo_permission.addItem("")
        self.combo_permission.addItem("")
        self.combo_permission.addItem("")
        self.fLayout_registerManager.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.combo_permission)
        self.vLayout_registerNewManager.addLayout(self.fLayout_registerManager)
        self.hLayout_buttons = QtWidgets.QHBoxLayout()
        self.hLayout_buttons.setObjectName("hLayout_buttons")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hLayout_buttons.addItem(spacerItem)
        self.btn_registerManager = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_registerManager.setObjectName("btn_registerManager")
        self.hLayout_buttons.addWidget(self.btn_registerManager)
        self.btn_cancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_cancel.setObjectName("btn_cancel")
        self.hLayout_buttons.addWidget(self.btn_cancel)
        self.vLayout_registerNewManager.addLayout(self.hLayout_buttons)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Register New Manager"))
        self.label_firstName.setText(_translate("MainWindow", "First Name"))
        self.labe_surname.setText(_translate("MainWindow", "Surname"))
        self.label_username.setText(_translate("MainWindow", "Username"))
        self.label_password.setText(_translate("MainWindow", "Password"))
        self.label_2.setText(_translate("MainWindow", "Permission Level"))
        self.combo_permission.setItemText(0, _translate("MainWindow", "Select Option"))
        self.combo_permission.setItemText(1, _translate("MainWindow", "Manager"))
        self.combo_permission.setItemText(2, _translate("MainWindow", "Administrator"))
        self.btn_registerManager.setText(_translate("MainWindow", "Register New Manager"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancel"))
