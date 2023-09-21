import sys

from PyQt5 import QtWidgets, QtCore, QtChart
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QBarSeries, QBarSet, QBarCategoryAxis, QChartView, QCategoryAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

import keyboard
import re

from ui import login, applicantDashboard, managerDashboard, managerPendingApplications, managerTeamMembers, \
    managerAddNewMember, adminManagerProfiles, adminRegisterManager

from classes.object import *
from classes.dialogBoxes import *
from classes.tableModel import *


def verifyUsername(username):
    userPattern = r"^[a-zA-Z][a-zA-Z0-9_]*$"
    return re.match(userPattern, username)


class loginWindow(login.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # slots and signals

        # buttons
        # applicant
        self.btn_applicantLogin.clicked.connect(self.loginApplicant)
        self.btn_applicantCancel.clicked.connect(self.cancel)

        # manager
        self.btn_managerLogin.clicked.connect(self.loginManager)
        self.btn_managerCancel.clicked.connect(self.cancel)

        # line edits
        # applicant
        self.line_applicantUsername.textChanged.connect(self.printApplicantUsername)
        self.line_applicantUsername.returnPressed.connect(self.enterPressed)
        self.line_applicantPassword.textChanged.connect(self.printPassword)
        self.line_applicantPassword.returnPressed.connect(self.loginApplicant)

        # manager
        self.line_managerUsername.textChanged.connect(self.printManagerUsername)
        self.line_managerUsername.returnPressed.connect(self.enterPressed)
        self.line_managerPassword.textChanged.connect(self.printPassword)
        self.line_managerPassword.returnPressed.connect(self.loginManager)

    def printApplicantUsername(self):
        usernameEntered = self.line_applicantUsername.text()
        filteredUser = verifyUsername(usernameEntered)
        if filteredUser:
            self.line_applicantUsername.setText(filteredUser.group())
        else:
            cursor = self.line_applicantUsername.cursorPosition()
            self.line_applicantUsername.setText(usernameEntered[:cursor - 1] + usernameEntered[cursor:])
            self.line_applicantUsername.setCursorPosition(cursor - 1)

    def printManagerUsername(self):
        usernameEntered = self.line_managerUsername.text()
        filteredUser = verifyUsername(usernameEntered)
        if filteredUser:
            self.line_managerUsername.setText(filteredUser.group())
        else:
            cursor = self.line_managerUsername.cursorPosition()
            self.line_managerUsername.setText(usernameEntered[:cursor - 1] + usernameEntered[cursor:])
            self.line_managerUsername.setCursorPosition(cursor - 1)

    def printPassword(self):
        self.line_applicantPassword.setText(self.line_applicantPassword.text())
        self.line_managerPassword.setText(self.line_managerPassword.text())

    def enterPressed(self):
        self.line_applicantPassword.setFocus()
        self.line_managerPassword.setFocus()

    def loginApplicant(self):
        loginType = 'applicant'
        usernameEntered = self.line_applicantUsername.text()
        passwordEntered = self.line_applicantPassword.text()
        if general.verifyLogin(usernameEntered, passwordEntered, loginType):
            messageBox('Success', 'Logged in Successfully!', 'information')
            print('Login Successfully!')
            self.close()
            applicantDashboardWindow.show()
            self.line_applicantPassword.clear()
        else:
            messageBox('Error', 'Invalid username or password! Please try again.', 'warning')
            self.line_applicantPassword.setFocus()

    def loginManager(self):
        loginType = 'manager'
        usernameEntered = self.line_managerUsername.text()
        passwordEntered = self.line_managerPassword.text()
        if general.verifyLogin(usernameEntered, passwordEntered, loginType):
            messageBox('Success', 'Logged in Successfully!', 'information')
            print('Login Successfully!')
            self.close()
            managerDashboardWindow.show()
            self.line_managerPassword.clear()
        else:
            messageBox('Error', 'Invalid username or password! Please try again.', 'warning')
            self.line_managerPassword.setFocus()

    def cancel(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            self.close()
        else:
            self.line_applicantPassword.setFocus()
            self.line_managerPassword.setFocus()


class applicantDashboardWindow(applicantDashboard.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tbl_prevApplications.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.previousApplications()

        # slots and signals

        # buttons
        self.btn_logout.clicked.connect(self.logout)
        # self.btn_newApplication.clicked.connect(self.newApplication)

    def previousApplications(self):
        header = ['Application ID', 'Date', 'Team', 'Status']
        data = managers.getPreviousApplications()
        self.previousApplicationsTable = tableModel(self, data, header)
        self.tbl_prevApplications.setModel(self.previousApplicationsTable)
        self.tbl_prevApplications.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)

    def logout(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            self.close()
            loginWindow.show()
        else:
            self.setFocus()


class managerDashboardWindow(managerDashboard.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # slots and signals

        # buttons
        self.btn_pendingApps.clicked.connect(self.pendingApplications)
        self.btn_teamMembers.clicked.connect(self.teamMembers)
        self.btn_adminManagerProfile.clicked.connect(self.adminManagerProfiles)
        self.btn_logout.clicked.connect(self.logout)

        # tables
        self.chart_memberStats = QChartView(self.chart_memberStats)
        self.chart_memberStats.setGeometry(self.chart_memberStats.rect())
        self.chart_memberStats.resize(380, 246)

        # show tables
        self.showMemberStats()

    def pendingApplications(self):
        managerPendingApplicationsWindow.show()
        managerPendingApplicationsWindow.setFocus()

    def teamMembers(self):
        managerTeamMembersWindow.show()
        managerTeamMembersWindow.setFocus()

    def adminManagerProfiles(self):
        adminManagerProfilesWindow.show()
        adminManagerProfilesWindow.setFocus()

    def showMemberStats(self):
        teams, memberCounts = managers.getMemberStats()

        barSeries = QBarSeries()

        set1 = QBarSet('Member Count')
        set1.append(memberCounts)
        barSeries.append(set1)

        chart = QChart()
        chart.addSeries(barSeries)

        chart.setTitle('Member Statistics')
        chart.setAnimationOptions(QChart.SeriesAnimations)

        categories = [str(team) for team in teams]
        axisX = QBarCategoryAxis()
        axisX.append(categories)
        axisX.setLabelsAngle(45)  # rotates labels 45 degrees
        chart.addAxis(axisX, QtCore.Qt.AlignBottom)
        barSeries.attachAxis(axisX)

        self.chart_memberStats.setChart(chart)
        self.chart_memberStats.setRenderHint(QtGui.QPainter.Antialiasing)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(QtCore.Qt.AlignBottom)

        self.chart_memberStats.show()

    def logout(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            self.close()
            loginWindow.show()
        else:
            self.setFocus()


class managerPendingApplicationsWindow(managerPendingApplications.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tbl_pendingApplications.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.pendingApplications()

        # slots and signals

        # buttons
        self.btn_backToDashboard.clicked.connect(self.backToDashboard)

        # line edits
        self.line_searchBar.textChanged.connect(self.pendingApplications)

    def pendingApplications(self, keyword=None):
        keyword = self.line_searchBar.text()
        header = ['Application ID', 'Applicant Name', 'Date', 'Team']
        data = managers.getPendingApplications(keyword)

        if not data:
            data = ['', '', '', '']

        self.pendingApplicationsTable = tableModel(self, data, header)
        self.tbl_pendingApplications.setModel(self.pendingApplicationsTable)
        self.tbl_pendingApplications.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)

    def backToDashboard(self):
        self.close()
        managerDashboardWindow.setFocus()


class managerTeamMembersWindow(managerTeamMembers.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tbl_teamMembers.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.teamMembers()

        # slots and signals

        # buttons
        self.btn_backToDashboard.clicked.connect(self.backToDashboard)
        self.combo_teamSelect.currentIndexChanged.connect(self.applyFilters)
        self.btn_addNewMember.clicked.connect(self.managerAddNewMember)

        # line edits
        self.line_searchBar.textChanged.connect(self.teamMembers)

    def teamMembers(self, keyword=None):
        keyword = self.line_searchBar.text()
        header = ['Member ID', 'Member Name', 'Team']
        data = managers.getTeamMembers(keyword)

        if not data:
            data = ['', '', '']

        self.teamMembersTable = tableModel(self, data, header)
        self.tbl_teamMembers.setModel(self.teamMembersTable)
        self.tbl_teamMembers.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)

    def applyFilters(self):
        teamFilter = self.combo_teamSelect.currentText()
        self.teamMembersTable.setTeamFilters(teamFilter)

    def backToDashboard(self):
        managerDashboardWindow.show()
        self.close()
        managerDashboardWindow.setFocus()

    def managerAddNewMember(self):
        managerAddNewMemberWindow.show()
        managerAddNewMemberWindow.setFocus()


class managerAddNewMemberWindow(managerAddNewMember.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # slots and signals

        # buttons
        self.btn_addNewMember.clicked.connect(self.addMember)
        self.btn_cancel.clicked.connect(self.cancel)
        self.combo_teamSelect.currentIndexChanged.connect(self.teamSelect)
        self.combo_dLeader.currentIndexChanged.connect(self.printDLeader)

        # line edits
        self.line_firstName.textChanged.connect(self.printFirstName)
        self.line_surname.textChanged.connect(self.printSurname)
        self.line_mobileNumber.textChanged.connect(self.printMobileNumber)
        self.line_email.textChanged.connect(self.printEmail)

        # date entry
        self.date_dob.setCalendarPopup(True)
        self.date_dob.dateChanged.connect(self.printDob)

        # validators
        self.line_mobileNumber.setValidator(QtGui.QIntValidator())

    def printFirstName(self):
        self.line_firstName.setText(self.line_firstName.text())

    def printSurname(self):
        self.line_surname.setText(self.line_surname.text())

    def printMobileNumber(self):
        self.line_mobileNumber.setText(self.line_mobileNumber.text())

    def printEmail(self):
        self.line_email.setText(self.line_email.text())

    def printDLeader(self):
        dLeader = self.combo_dLeader.currentText()
        self.combo_dLeader.setCurrentText(dLeader)

    def teamSelect(self):
        team = self.combo_teamSelect.currentText()
        self.combo_teamSelect.setCurrentText(team)

    def printDob(self):
        self.date_dob.setDate(self.date_dob.date())

    def addMember(self):
        firstName = self.line_firstName.text()
        surname = self.line_surname.text()
        dob = self.date_dob.text()
        mobileNumber = self.line_mobileNumber.text()
        team = self.combo_teamSelect.currentText()
        email = self.line_email.text()
        dleaderIndex = self.combo_dLeader.currentText()

        if team != 'Select Option':
            if team == 'Camera & Graphics':
                teamIndex = '1'
            elif team == 'Sounds & Lights':
                teamIndex = '2'
            elif team == 'Stage Management':
                teamIndex = '3'
        else:
            teamIndex = ''

        if email == '':
            email = None

        if dleaderIndex == '':
            dleaderIndex = None

        if firstName and surname and dob and mobileNumber and teamIndex != '':
            if messageBox('Confirmation', 'Are you sure you want to register this member?', 'question', True) == \
                    QtWidgets.QMessageBox.Ok:
                managers.addNewMember(firstName, surname, dob, mobileNumber, teamIndex, email, dleaderIndex)
                messageBox('Success', 'Member successfully registered!', 'information', False)

                managerTeamMembersWindow.show()
                self.close()
                managerTeamMembersWindow.setFocus()
            else:
                self.setFocus()
        else:
            messageBox('Error', 'Please fill in all the fields!', 'critical', False)
            self.setFocus()

    def cancel(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            managerTeamMembersWindow.show()
            self.close()
            managerTeamMembersWindow.setFocus()
        else:
            self.setFocus()


class adminManagerProfilesWindow(adminManagerProfiles.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tbl_managerProfiles.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.managerProfiles()

        # slots and signals

        # buttons
        self.btn_backToDashboard.clicked.connect(self.backToDashboard)
        self.btn_registerManager.clicked.connect(self.adminRegisterManager)
        # self.btn_removeManager.clicked.connect(self.removeManager)

        # line edits
        self.line_searchBar.textChanged.connect(self.managerProfiles)

    def managerProfiles(self, keyword=None):
        keyword = self.line_searchBar.text()
        header = ['Manager ID', 'Manager Name', 'Manager Username']
        data = administrators.getManagerProfiles(keyword)

        if not data:
            data = ['', '', '']

        self.managerProfilesTable = tableModel(self, data, header)
        self.tbl_managerProfiles.setModel(self.managerProfilesTable)
        self.tbl_managerProfiles.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)

    def adminRegisterManager(self):
        adminRegisterManagerWindow.show()
        adminRegisterManagerWindow.setFocus()

    def backToDashboard(self):
        managerDashboardWindow.show()
        self.close()
        managerDashboardWindow.setFocus()


class adminRegisterManagerWindow(adminRegisterManager.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # slots and signals

        # buttons
        # self.btn_addNewMember.clicked.connect(self.addNewMember)
        self.btn_cancel.clicked.connect(self.cancel)

        # text edits
        self.line_firstName.textChanged.connect(self.printFirstName)
        self.line_surname.textChanged.connect(self.printSurname)
        self.line_username.textChanged.connect(self.printUsername)
        self.line_password.textChanged.connect(self.printPassword)

    def printFirstName(self):
        self.line_firstName.setText(self.line_firstName.text())

    def printSurname(self):
        self.line_surname.setText(self.line_surname.text())

    def printUsername(self):
        usernameEntered = self.line_username.text()
        filteredUser = verifyUsername(usernameEntered)
        if filteredUser:
            self.line_username.setText(filteredUser.group())
        else:
            cursor = self.line_username.cursorPosition()
            self.line_username.setText(usernameEntered[:cursor - 1] + usernameEntered[cursor:])
            self.line_username.setCursorPosition(cursor - 1)

    def printPassword(self):
        self.line_password.setText(self.line_password.text())

    def cancel(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            adminManagerProfilesWindow.show()
            self.close()
            adminManagerProfilesWindow.setFocus()
        else:
            self.setFocus()


if __name__ == '__main__':
    Database.initialize(database='ccf-volunteers', user='postgres', password='543738', host='localhost', port='5432')

    app = QApplication(sys.argv)

    loginWindow = loginWindow()
    applicantDashboardWindow = applicantDashboardWindow()
    managerDashboardWindow = managerDashboardWindow()
    managerPendingApplicationsWindow = managerPendingApplicationsWindow()
    managerTeamMembersWindow = managerTeamMembersWindow()
    managerAddNewMemberWindow = managerAddNewMemberWindow()
    adminManagerProfilesWindow = adminManagerProfilesWindow()
    adminRegisterManagerWindow = adminRegisterManagerWindow()

    loginWindow.show()
    sys.exit(app.exec_())
