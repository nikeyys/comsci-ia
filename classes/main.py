import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

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

        # calling other windows
        self.applicantDashboard = applicantDashboardWindow()
        self.managerDashboard = managerDashboardWindow()

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
        if verifyLogin(usernameEntered, passwordEntered, loginType):
            messageBox('Success', 'Logged in Successfully!', 'information')
            print('Login Successfully!')
            self.applicantDashboard.show()
            self.line_applicantUsername.clear()
            self.line_applicantPassword.clear()
            self.close()
        else:
            messageBox('Error', 'Invalid username or password! Please try again.', 'warning')
            self.line_applicantPassword.setFocus()

    def loginManager(self):
        loginType = 'manager'
        usernameEntered = self.line_managerUsername.text()
        passwordEntered = self.line_managerPassword.text()
        if verifyLogin(usernameEntered, passwordEntered, loginType):
            messageBox('Success', 'Logged in Successfully!', 'information')
            print('Login Successfully!')
            self.managerDashboard.show()
            self.line_managerUsername.clear()
            self.line_managerPassword.clear()
            self.close()
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

        # calling other windows
        # self.newApplication = newApplicationWindow()

    def previousApplications(self):
        header = ['Application ID', 'Date', 'Team', 'Status']
        data = getPreviousApplications()
        self.previousApplicationsTable = tableModel(self, data, header)
        self.tbl_prevApplications.setModel(self.previousApplicationsTable)
        self.tbl_prevApplications.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)

    def logout(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            self.close()
            login.show()
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

        # calling other windows
        self.managerPendingApplications = managerPendingApplicationsWindow()
        self.managerTeamMembers = managerTeamMembersWindow()
        self.adminManagerProfiles = adminManagerProfilesWindow()

    def pendingApplications(self):
        self.managerPendingApplications.show()
        self.managerPendingApplications.setFocus()

    def teamMembers(self):
        self.managerTeamMembers.show()
        self.managerTeamMembers.setFocus()

    def adminManagerProfiles(self):
        self.adminManagerProfiles.show()
        self.adminManagerProfiles.setFocus()

    def logout(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            self.close()
            login.show()
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

        # initializing managerDashboardWindow instance
        self.managerDashboard = None

    def pendingApplications(self, keyword=None):
        keyword = self.line_searchBar.text()
        header = ['Application ID', 'Applicant Name', 'Date', 'Team']
        data = getPendingApplications(keyword)

        if not data:
            data = ['', '', '', '']

        self.pendingApplicationsTable = tableModel(self, data, header)
        self.tbl_pendingApplications.setModel(self.pendingApplicationsTable)
        self.tbl_pendingApplications.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)

    def backToDashboard(self):
        if self.managerDashboard is None:
            self.managerDashboard = managerDashboardWindow()
        self.close()
        self.managerDashboard.setFocus()


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

        # initializing managerDashboardWindow instance
        self.managerDashboard = None

        # calling other windows
        self.managerAddNewMember = managerAddNewMemberWindow()

    def teamMembers(self, keyword=None):
        keyword = self.line_searchBar.text()
        header = ['Member ID', 'Member Name', 'Team']
        data = getTeamMembers(keyword)

        if not data:
            data = ['', '', '']

        self.teamMembersTable = tableModel(self, data, header)
        self.tbl_teamMembers.setModel(self.teamMembersTable)
        self.tbl_teamMembers.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)

    def applyFilters(self):
        teamFilter = self.combo_teamSelect.currentText()
        self.teamMembersTable.setTeamFilters(teamFilter)

    def backToDashboard(self):
        if self.managerDashboard is None:
            self.managerDashboard = managerDashboardWindow()
        self.close()
        self.managerDashboard.setFocus()

    def managerAddNewMember(self):
        self.managerAddNewMember.show()
        self.managerAddNewMember.setFocus()


class managerAddNewMemberWindow(managerAddNewMember.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # slots and signals

        # buttons
        # add new member btn
        self.btn_cancel.clicked.connect(self.cancel)
        self.combo_teamSelect.currentIndexChanged.connect(self.teamSelect)

        # line edits
        self.line_firstName.textChanged.connect(self.printFirstName)
        self.line_surname.textChanged.connect(self.printSurname)
        self.line_mobileNumber.textChanged.connect(self.printMobileNumber)
        self.line_email.textChanged.connect(self.printEmail)
        self.line_dLeader.textChanged.connect(self.printDLeader)

        # date entry
        self.date_dob.setCalendarPopup(True)
        self.date_dob.dateChanged.connect(self.printDob)

        # initializing managerTeamMembersWindow instance
        self.managerTeamMembers = None

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
        self.line_dLeader.setText(self.line_dLeader.text())

    def teamSelect(self):
        team = self.combo_teamSelect.currentText()
        self.combo_teamSelect.setCurrentText(team)

    def printDob(self):
        self.date_dob.setDate(self.date_dob.date())

    def cancel(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            if self.managerTeamMembers is None:
                self.managerTeamMembers = managerTeamMembersWindow()
            self.close()
            self.managerTeamMembers.setFocus()
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

        # initializing adminDashboardWindow instance
        self.managerDashboard = None

        # calling other windows
        self.adminRegisterManager = adminRegisterManagerWindow()

    def managerProfiles(self, keyword=None):
        keyword = self.line_searchBar.text()
        header = ['Manager ID', 'Manager Name', 'Manager Username']
        data = getManagerProfiles(keyword)

        if not data:
            data = ['', '', '']

        self.managerProfilesTable = tableModel(self, data, header)
        self.tbl_managerProfiles.setModel(self.managerProfilesTable)
        self.tbl_managerProfiles.horizontalHeader().resizeSections(QtWidgets.QHeaderView.ResizeToContents)

    def adminRegisterManager(self):
        self.adminRegisterManager.show()
        self.adminRegisterManager.setFocus()

    def backToDashboard(self):
        if self.managerDashboard is None:
            self.managerDashboard = managerDashboardWindow()
        self.close()
        self.managerDashboard.setFocus()


class adminRegisterManagerWindow(adminRegisterManager.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # slots and signals

        # buttons
        self.btn_registerManager.clicked.connect(self.registerNewManager)
        self.btn_cancel.clicked.connect(self.cancel)

        # text edits
        self.line_firstName.textChanged.connect(self.printFirstName)
        self.line_surname.textChanged.connect(self.printSurname)
        self.line_username.textChanged.connect(self.printUsername)
        self.line_password.textChanged.connect(self.printPassword)

        # initializing adminManagerProfilesWindow instance
        self.adminManagerProfiles = None

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

    def registerNewManager(self):
        firstName = self.line_firstName.text()
        surname = self.line_surname.text()
        username = self.line_username.text()
        password = self.line_password.text()

        if firstName and surname and username and password:
            if messageBox('Confirmation', 'Are you sure you want to register this manager?', 'question', True) == \
                    QtWidgets.QMessageBox.Ok:
                managers.add(firstName, surname, username, password)
                messageBox('Success', 'Manager successfully registered!', 'information', False)
                if self.adminManagerProfiles is None:
                    self.adminManagerProfiles = adminManagerProfilesWindow()
                self.close()
                self.adminManagerProfiles.setFocus()
            else:
                self.setFocus()
        else:
            messageBox('Error', 'Please fill in all the fields!', 'critical', False)
            self.setFocus()

    def cancel(self):
        if messageBox('Confirmation', 'Are you sure you want to exit?', 'question', True) == QtWidgets.QMessageBox.Ok:
            if self.adminManagerProfiles is None:
                self.adminManagerProfiles = adminManagerProfilesWindow()
            self.close()
            self.adminManagerProfiles.setFocus()
        else:
            self.setFocus()


if __name__ == '__main__':
    Database.initialize(database='ccf-volunteers', user='postgres', password='543738', host='localhost', port='5432')

    app = QApplication(sys.argv)
    login = loginWindow()
    login.show()
    sys.exit(app.exec_())
