from PyQt5 import QtWidgets, QtGui


def messageBox(windowTitle, message, boxType='normal', ynButtons=False):
    msgBox = QtWidgets.QMessageBox()
    if boxType is None:
        msgBox.setIcon(QtWidgets.QMessageBox.NoIcon)
    elif boxType.lower() == 'error':
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
    elif boxType.lower() == 'question':
        msgBox.setIcon(QtWidgets.QMessageBox.Question)
    elif boxType.lower() == 'warning':
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
    elif boxType.lower() == 'information':
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
    else:
        msgBox.setIcon(QtWidgets.QMessageBox.NoIcon)

    msgBox.setText(message)
    msgBox.setWindowTitle(windowTitle)

    if ynButtons:
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
        return msgBox.exec_()
    else:
        msgBox.exec_()