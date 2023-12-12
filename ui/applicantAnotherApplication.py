# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'applicantAnotherApplication.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(635, 715)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(10)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(-30, 10, 661, 641))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(17, 0, 611, 1401))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.layoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 0, 571, 1398))
        self.layoutWidget.setObjectName("layoutWidget")
        self.vLayout_questionnaire = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.vLayout_questionnaire.setContentsMargins(0, 0, 0, 0)
        self.vLayout_questionnaire.setObjectName("vLayout_questionnaire")
        self.lbl_volunteerApp = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_volunteerApp.setFont(font)
        self.lbl_volunteerApp.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_volunteerApp.setObjectName("lbl_volunteerApp")
        self.vLayout_questionnaire.addWidget(self.lbl_volunteerApp)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vLayout_questionnaire.addItem(spacerItem)
        self.vLayout_personalDetails = QtWidgets.QVBoxLayout()
        self.vLayout_personalDetails.setObjectName("vLayout_personalDetails")
        self.lbl_personalDetails = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_personalDetails.setFont(font)
        self.lbl_personalDetails.setObjectName("lbl_personalDetails")
        self.vLayout_personalDetails.addWidget(self.lbl_personalDetails)
        self.hLayout_teamSelect = QtWidgets.QHBoxLayout()
        self.hLayout_teamSelect.setObjectName("hLayout_teamSelect")
        self.vLayout_teamSelect = QtWidgets.QVBoxLayout()
        self.vLayout_teamSelect.setObjectName("vLayout_teamSelect")
        self.lbl_teamSelect = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_teamSelect.setObjectName("lbl_teamSelect")
        self.vLayout_teamSelect.addWidget(self.lbl_teamSelect)
        self.combo_teamSelect = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_teamSelect.setObjectName("combo_teamSelect")
        self.combo_teamSelect.addItem("")
        self.combo_teamSelect.addItem("")
        self.combo_teamSelect.addItem("")
        self.combo_teamSelect.addItem("")
        self.vLayout_teamSelect.addWidget(self.combo_teamSelect)
        self.hLayout_teamSelect.addLayout(self.vLayout_teamSelect)
        spacerItem1 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.hLayout_teamSelect.addItem(spacerItem1)
        self.vLayout_personalDetails.addLayout(self.hLayout_teamSelect)
        self.vLayout_questionnaire.addLayout(self.vLayout_personalDetails)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vLayout_questionnaire.addItem(spacerItem2)
        self.vLayour_spiritual = QtWidgets.QVBoxLayout()
        self.vLayour_spiritual.setObjectName("vLayour_spiritual")
        self.lbl_spiritualQuestions = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_spiritualQuestions.setFont(font)
        self.lbl_spiritualQuestions.setObjectName("lbl_spiritualQuestions")
        self.vLayour_spiritual.addWidget(self.lbl_spiritualQuestions)
        self.vLayout_dleaderSelect = QtWidgets.QVBoxLayout()
        self.vLayout_dleaderSelect.setObjectName("vLayout_dleaderSelect")
        self.lbl_dleader = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_dleader.setObjectName("lbl_dleader")
        self.vLayout_dleaderSelect.addWidget(self.lbl_dleader)
        self.combo_dleader = QtWidgets.QComboBox(self.layoutWidget)
        self.combo_dleader.setObjectName("combo_dleader")
        self.vLayout_dleaderSelect.addWidget(self.combo_dleader)
        self.lbl_notApplicableDLeader = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.lbl_notApplicableDLeader.setFont(font)
        self.lbl_notApplicableDLeader.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_notApplicableDLeader.setObjectName("lbl_notApplicableDLeader")
        self.vLayout_dleaderSelect.addWidget(self.lbl_notApplicableDLeader)
        self.vLayour_spiritual.addLayout(self.vLayout_dleaderSelect)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.vLayour_spiritual.addItem(spacerItem3)
        self.vLayout_whenJesusLord = QtWidgets.QVBoxLayout()
        self.vLayout_whenJesusLord.setObjectName("vLayout_whenJesusLord")
        self.lbl_whenJesusLord = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_whenJesusLord.setObjectName("lbl_whenJesusLord")
        self.vLayout_whenJesusLord.addWidget(self.lbl_whenJesusLord)
        self.text_whenJesusLord = QtWidgets.QTextEdit(self.layoutWidget)
        self.text_whenJesusLord.setObjectName("text_whenJesusLord")
        self.vLayout_whenJesusLord.addWidget(self.text_whenJesusLord)
        self.vLayour_spiritual.addLayout(self.vLayout_whenJesusLord)
        self.vLayout_howJesusLord = QtWidgets.QVBoxLayout()
        self.vLayout_howJesusLord.setObjectName("vLayout_howJesusLord")
        self.lbl_howJesusLord = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_howJesusLord.setObjectName("lbl_howJesusLord")
        self.vLayout_howJesusLord.addWidget(self.lbl_howJesusLord)
        self.text_howJesusLord = QtWidgets.QTextEdit(self.layoutWidget)
        self.text_howJesusLord.setObjectName("text_howJesusLord")
        self.vLayout_howJesusLord.addWidget(self.text_howJesusLord)
        self.vLayour_spiritual.addLayout(self.vLayout_howJesusLord)
        self.vLayout_loseSalvation = QtWidgets.QVBoxLayout()
        self.vLayout_loseSalvation.setObjectName("vLayout_loseSalvation")
        self.lbl_loseSalvation = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_loseSalvation.setObjectName("lbl_loseSalvation")
        self.vLayout_loseSalvation.addWidget(self.lbl_loseSalvation)
        self.text_loseSalvation = QtWidgets.QTextEdit(self.layoutWidget)
        self.text_loseSalvation.setObjectName("text_loseSalvation")
        self.vLayout_loseSalvation.addWidget(self.text_loseSalvation)
        self.vLayour_spiritual.addLayout(self.vLayout_loseSalvation)
        self.vLayout_ministryToSalvation = QtWidgets.QVBoxLayout()
        self.vLayout_ministryToSalvation.setObjectName("vLayout_ministryToSalvation")
        self.lbl_ministryToSalvation = QtWidgets.QLabel(self.layoutWidget)
        self.lbl_ministryToSalvation.setObjectName("lbl_ministryToSalvation")
        self.vLayout_ministryToSalvation.addWidget(self.lbl_ministryToSalvation)
        self.text_ministryToSalvation = QtWidgets.QTextEdit(self.layoutWidget)
        self.text_ministryToSalvation.setObjectName("text_ministryToSalvation")
        self.vLayout_ministryToSalvation.addWidget(self.text_ministryToSalvation)
        self.vLayour_spiritual.addLayout(self.vLayout_ministryToSalvation)
        self.vLayout_questionnaire.addLayout(self.vLayour_spiritual)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(410, 660, 203, 27))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.hLayout_buttons = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.hLayout_buttons.setContentsMargins(0, 0, 0, 0)
        self.hLayout_buttons.setObjectName("hLayout_buttons")
        self.btn_cancel = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_cancel.setObjectName("btn_cancel")
        self.hLayout_buttons.addWidget(self.btn_cancel)
        self.btn_submit = QtWidgets.QPushButton(self.layoutWidget1)
        self.btn_submit.setObjectName("btn_submit")
        self.hLayout_buttons.addWidget(self.btn_submit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "New Application "))
        self.lbl_volunteerApp.setText(_translate("MainWindow", "Volunteer Application"))
        self.lbl_personalDetails.setText(_translate("MainWindow", "Team Select"))
        self.lbl_teamSelect.setText(_translate("MainWindow", "Preferred Team"))
        self.combo_teamSelect.setItemText(0, _translate("MainWindow", "Select Option"))
        self.combo_teamSelect.setItemText(1, _translate("MainWindow", "Camera & Graphics"))
        self.combo_teamSelect.setItemText(2, _translate("MainWindow", "Sounds & Lights"))
        self.combo_teamSelect.setItemText(3, _translate("MainWindow", "Stage Management"))
        self.lbl_spiritualQuestions.setText(_translate("MainWindow", "Spiritual Questions"))
        self.lbl_dleader.setText(_translate("MainWindow", "DLeader"))
        self.lbl_notApplicableDLeader.setText(_translate("MainWindow", "If not applicable, please leave empty."))
        self.lbl_whenJesusLord.setText(_translate("MainWindow", "When did you accept Jesus as your Lord and Savior?"))
        self.lbl_howJesusLord.setText(_translate("MainWindow", "How did you know that you have accepted Jesus and your Lord and Savior?"))
        self.lbl_loseSalvation.setText(_translate("MainWindow", "Can you lose your salvation? Why or Why not?"))
        self.lbl_ministryToSalvation.setText(_translate("MainWindow", "How do you view ministry/service in relation to your salvation?"))
        self.btn_cancel.setText(_translate("MainWindow", "Cancel"))
        self.btn_submit.setText(_translate("MainWindow", "Submit Application"))