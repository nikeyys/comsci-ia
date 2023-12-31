# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'managerAddNewMember.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(357, 315)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 341, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_addNewMember = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_addNewMember.sizePolicy().hasHeightForWidth())
        self.label_addNewMember.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_addNewMember.setFont(font)
        self.label_addNewMember.setAlignment(QtCore.Qt.AlignCenter)
        self.label_addNewMember.setObjectName("label_addNewMember")
        self.verticalLayout.addWidget(self.label_addNewMember)
        self.fLayout_addNewMember = QtWidgets.QFormLayout()
        self.fLayout_addNewMember.setObjectName("fLayout_addNewMember")
        self.label_firstName = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_firstName.setObjectName("label_firstName")
        self.fLayout_addNewMember.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_firstName)
        self.line_firstName = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_firstName.setObjectName("line_firstName")
        self.fLayout_addNewMember.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_firstName)
        self.label_surname = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_surname.setObjectName("label_surname")
        self.fLayout_addNewMember.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_surname)
        self.line_surname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_surname.setObjectName("line_surname")
        self.fLayout_addNewMember.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.line_surname)
        self.label_dob = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_dob.setObjectName("label_dob")
        self.fLayout_addNewMember.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_dob)
        self.date_dob = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.date_dob.setObjectName("date_dob")
        self.fLayout_addNewMember.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.date_dob)
        self.label_mobileNumber = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_mobileNumber.setObjectName("label_mobileNumber")
        self.fLayout_addNewMember.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_mobileNumber)
        self.line_mobileNumber = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_mobileNumber.setObjectName("line_mobileNumber")
        self.fLayout_addNewMember.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.line_mobileNumber)
        self.label_teamSelect = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_teamSelect.setObjectName("label_teamSelect")
        self.fLayout_addNewMember.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_teamSelect)
        self.combo_teamSelect = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.combo_teamSelect.setObjectName("combo_teamSelect")
        self.combo_teamSelect.addItem("")
        self.combo_teamSelect.addItem("")
        self.combo_teamSelect.addItem("")
        self.combo_teamSelect.addItem("")
        self.fLayout_addNewMember.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.combo_teamSelect)
        self.label_email = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_email.setObjectName("label_email")
        self.fLayout_addNewMember.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_email)
        self.line_email = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.line_email.setObjectName("line_email")
        self.fLayout_addNewMember.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.line_email)
        self.label_dLeader = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_dLeader.setObjectName("label_dLeader")
        self.fLayout_addNewMember.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_dLeader)
        self.combo_dLeader = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.combo_dLeader.setEditable(True)
        self.combo_dLeader.setObjectName("combo_dLeader")
        self.fLayout_addNewMember.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.combo_dLeader)
        self.verticalLayout.addLayout(self.fLayout_addNewMember)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_addNewMember = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_addNewMember.setObjectName("btn_addNewMember")
        self.horizontalLayout.addWidget(self.btn_addNewMember)
        self.btn_cancel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add New Member"))
        self.label_addNewMember.setText(_translate("MainWindow", "Add New Member"))
        self.label_firstName.setText(_translate("MainWindow", "First Name"))
        self.label_surname.setText(_translate("MainWindow", "Surname"))
        self.label_dob.setText(_translate("MainWindow", "Date of Birth"))
        self.label_mobileNumber.setText(_translate("MainWindow", "Mobile Number"))
        self.label_teamSelect.setText(_translate("MainWindow", "Team"))
        self.combo_teamSelect.setItemText(0, _translate("MainWindow", "Select Option"))
        self.combo_teamSelect.setItemText(1, _translate("MainWindow", "Camera & Graphics"))
        self.combo_teamSelect.setItemText(2, _translate("MainWindow", "Sounds & Lights"))
        self.combo_teamSelect.setItemText(3, _translate("MainWindow", "Stage Management"))
        self.label_email.setText(_translate("MainWindow", "Email (if applicable)"))
        self.label_dLeader.setText(_translate("MainWindow", "<html><head/><body><p>Name of DLeader (if applicable)</p></body></html>"))
        self.btn_addNewMember.setText(_translate("MainWindow", "Add New Member"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancel"))
