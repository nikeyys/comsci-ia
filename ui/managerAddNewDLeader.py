# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'managerAddNewDLeader.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(293, 240)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 271, 201))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_addNewDLeader = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_addNewDLeader.setFont(font)
        self.label_addNewDLeader.setAlignment(QtCore.Qt.AlignCenter)
        self.label_addNewDLeader.setObjectName("label_addNewDLeader")
        self.verticalLayout.addWidget(self.label_addNewDLeader)
        self.fLayout_dLeaderInfo = QtWidgets.QFormLayout()
        self.fLayout_dLeaderInfo.setObjectName("fLayout_dLeaderInfo")
        self.label_firstName = QtWidgets.QLabel(self.widget)
        self.label_firstName.setObjectName("label_firstName")
        self.fLayout_dLeaderInfo.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_firstName)
        self.line_firstName = QtWidgets.QLineEdit(self.widget)
        self.line_firstName.setObjectName("line_firstName")
        self.fLayout_dLeaderInfo.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_firstName)
        self.label_surname = QtWidgets.QLabel(self.widget)
        self.label_surname.setObjectName("label_surname")
        self.fLayout_dLeaderInfo.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_surname)
        self.line_surname = QtWidgets.QLineEdit(self.widget)
        self.line_surname.setObjectName("line_surname")
        self.fLayout_dLeaderInfo.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_surname)
        self.label_mobileNumber = QtWidgets.QLabel(self.widget)
        self.label_mobileNumber.setObjectName("label_mobileNumber")
        self.fLayout_dLeaderInfo.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_mobileNumber)
        self.line_mobileNumber = QtWidgets.QLineEdit(self.widget)
        self.line_mobileNumber.setObjectName("line_mobileNumber")
        self.fLayout_dLeaderInfo.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_mobileNumber)
        self.label_email = QtWidgets.QLabel(self.widget)
        self.label_email.setObjectName("label_email")
        self.fLayout_dLeaderInfo.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_email)
        self.line_email = QtWidgets.QLineEdit(self.widget)
        self.line_email.setObjectName("line_email")
        self.fLayout_dLeaderInfo.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line_email)
        self.verticalLayout.addLayout(self.fLayout_dLeaderInfo)
        self.hLayout_buttons = QtWidgets.QHBoxLayout()
        self.hLayout_buttons.setObjectName("hLayout_buttons")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.hLayout_buttons.addItem(spacerItem)
        self.btn_addNewDLeader = QtWidgets.QPushButton(self.widget)
        self.btn_addNewDLeader.setObjectName("btn_addNewDLeader")
        self.hLayout_buttons.addWidget(self.btn_addNewDLeader)
        self.btn_cancel = QtWidgets.QPushButton(self.widget)
        self.btn_cancel.setObjectName("btn_cancel")
        self.hLayout_buttons.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.hLayout_buttons)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_addNewDLeader.setText(_translate("MainWindow", "Add New DLeader"))
        self.label_firstName.setText(_translate("MainWindow", "First Name"))
        self.label_surname.setText(_translate("MainWindow", "Surname"))
        self.label_mobileNumber.setText(_translate("MainWindow", "Mobile Number"))
        self.label_email.setText(_translate("MainWindow", "Email Address"))
        self.btn_addNewDLeader.setText(_translate("MainWindow", "Add New DLeader"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancel"))
