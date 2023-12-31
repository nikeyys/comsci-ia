from PyQt5 import QtCore
from operator import itemgetter
from datetime import datetime
from decimal import Decimal


class tableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, myList, header, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.myList = myList
        self.header = header
        self.sortColumn = None
        self.sortOrder = QtCore.Qt.AscendingOrder
        self._filteredData = self.myList.copy()

    def rowCount(self, parent):
        return len(self._filteredData)

    def columnCount(self, parent):
        try:
            return len(self.myList[0])
        except IndexError:
            pass

    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != QtCore.Qt.DisplayRole:
            return None

        value = self._filteredData[index.row()][index.column()]

        # format decimal value to float
        if isinstance(value, Decimal):
            return float(value)

        # format date value to string
        if isinstance(value, datetime):
            return value.strftime("%Y-%m-%d")

        return str(value)

    def sort(self, col, order):
        if self.sortColumn is not None:
            self.beginResetModel()
            self.myList = sorted(self.myList, key=itemgetter(col))
            if order == QtCore.Qt.DescendingOrder:
                self.myList.reverse()
            self.endResetModel()

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.header[col].title()
        return None

    def sort(self, col, order):
        self.layoutAboutToBeChanged.emit()
        self._filteredData = sorted(self._filteredData, key=itemgetter(col))
        if order == QtCore.Qt.DescendingOrder:
            self._filteredData.reverse()
        self.layoutChanged.emit()

    def updateData(self, updatedData):
        self.beginResetModel()
        self.myList = updatedData
        self.endResetModel()

    def headerClicked(self, col):
        if col == self.sortColumn:
            self.sortOrder = QtCore.Qt.DescendingOrder if self.sortOrder == QtCore.Qt.AscendingOrder else QtCore.Qt.AscendingOrder
        else:
            self.sortColumn = col
            self.sort(col, self.sortOrder)

    def setTeamFilters(self, teamFilter):
        if teamFilter == 'No Selection':
            self._filteredData = self.myList.copy()  # no filter applied
        else:
            teamName = None
            if teamFilter == 'Camera & Graphics':
                teamName = 'Camera & Graphics'
            elif teamFilter == 'Sounds & Lights':
                teamName = 'Sounds & Lights'
            elif teamFilter == 'Stage Management':
                teamName = 'Stage Management'

            self._filteredData = [row for row in self.myList if row[2] == teamName]

        self.layoutChanged.emit()