#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
from PyQt5.QtWidgets import (QMainWindow, QHeaderView, QTabWidget, QAbstractItemView, QAction, qApp, QApplication, QTextEdit, QWidget, QFileDialog, QTableWidget,
                             QTableWidgetItem, QLabel, QGridLayout, QLineEdit, QTextEdit, QHBoxLayout, QVBoxLayout, QToolTip,
                             QPushButton, QDesktopWidget, QSplitter, QMessageBox,QSizePolicy, QSpacerItem, QDoubleSpinBox)

from PyQt5.QtGui import QIcon

class Main_Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI1()

    def initUI1(self):
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Main_Widget()
        self.setCentralWidget(self.ui)
        # tab = TabWidget()
        # self.initTabWidget(tab)
        self.initUI()

    def initUI(self):
        self.table_widget = TabWidget()
        self.setCentralWidget(self.table_widget)

        self.setGeometry(400, 50, 900, 750)
        self.setWindowTitle('Equal files')
        self.setWindowIcon(QIcon('window.ico'))
        self.show()

    # def initTabWidget(self, tabWidget):
    #     self.table_widget = tabWidget
    #     self.setCentralWidget(self.table_widget)
    #
    #     self.setGeometry(400, 50, 900, 750)
    #     self.setWindowTitle('Equal files')
    #     self.setWindowIcon(QIcon('window.ico'))
    #     self.show()

class TabWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.tablayout = QHBoxLayout(self)

# Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()

# Add tabs
        self.tabs.addTab(self.tab1, "int_cif")
        self.tabs.addTab(self.tab2, "int_peak")

# Create first tab
        self.tablen1 = MyTable(1,6)
        self.tablen2 = MyTable(2,6)
        self.tab1layout = QHBoxLayout(self)
        self.tab1layout.addWidget(self.tablen1)
        self.tab1layout.addWidget(self.tablen2)
        self.tab1t = QWidget()
        self.tab1t.setLayout(self.tab1layout)

        self.tab1btn1 = ButtonCreate(1, self.tablen1.getTableFromTableFunc())
        self.tab1btn2 = ButtonCreate(2, self.tablen2.getTableFromTableFunc())
        self.tab1btnLayaut = QHBoxLayout()
        self.tab1btnLayaut.addWidget(self.tab1btn1)
        self.tab1btnLayaut.addWidget(self.tab1btn2)
        self.tab1btn = QWidget()
        self.tab1btn.setLayout(self.tab1btnLayaut)
        self.tabbtn1 = QVBoxLayout(self)
        self.tabbtn1.addWidget(self.tab1t)
        self.tabbtn1.addWidget(self.tab1btn)
        self.tab1.setLayout(self.tabbtn1)

        self.tablen3 = MyTable(1,6)
        self.tablen4 = MyTable(1,6)
        self.tab2layout = QHBoxLayout(self)
        self.tab2layout.addWidget(self.tablen3)
        self.tab2layout.addWidget(self.tablen4)
        self.tab2t = QWidget()
        self.tab2t.setLayout(self.tab2layout)

        self.tab2btn1 = ButtonCreate(1, self.tablen3.getTableFromTableFunc())
        self.tab2btn2 = ButtonCreate(3, self.tablen4.getTableFromTableFunc())
        self.tab2btnLayaut = QHBoxLayout()
        self.tab2btnLayaut.addWidget(self.tab2btn1)
        self.tab2btnLayaut.addWidget(self.tab2btn2)
        self.tab2btn = QWidget()
        self.tab2btn.setLayout(self.tab2btnLayaut)
        self.tabbtn2 = QVBoxLayout(self)
        self.tabbtn2.addWidget(self.tab2t)
        self.tabbtn2.addWidget(self.tab2btn)
        self.tab2.setLayout(self.tabbtn2)

# Add tabs to widget
        self.tablayout.addWidget(self.tabs)
        self.setLayout(self.tablayout)

class ButtonCreate(QWidget):
    def __init__(self, n, table):
        super().__init__()
        self.LayoutButton(n)
        self.table = table

    def LayoutButton(self, n):
        self.CreateB(n)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.buttom)
        self.setLayout(self.layout)


    def CreateB(self, n):
        if n==1:
            self.btn = QPushButton('Open int')
            self.btn.clicked.connect(self.readint)
            self.btn.resize(self.btn.sizeHint())

            self.btn1 = QPushButton('Edit int')
            self.btn1.clicked.connect(qApp.quit)
            self.btn1.resize(self.btn1.sizeHint())

            self.btn2 = QPushButton('Save int')
            self.btn2.clicked.connect(qApp.quit)
            self.btn2.resize(self.btn2.sizeHint())

            self.hboxint = QHBoxLayout(self)
            self.hboxint.addWidget(self.btn)
            self.hboxint.addWidget(self.btn1)
            self.hboxint.addWidget(self.btn2)
            self.buttom = QWidget()
            self.buttom.setLayout(self.hboxint)

        if n==2:
            self.btn3 = QPushButton('Open cif')
            self.btn3.clicked.connect(self.readcif)
            self.btn3.resize(self.btn3.sizeHint())

            self.btn4 = QPushButton('Edit cif')
            self.btn4.clicked.connect(qApp.quit)
            self.btn4.resize(self.btn4.sizeHint())

            self.btn5 = QPushButton('Save txt')
            self.btn5.clicked.connect(qApp.quit)
            self.btn5.resize(self.btn5.sizeHint())

            self.hboxcif = QHBoxLayout(self)
            self.hboxcif.addWidget(self.btn3)
            self.hboxcif.addWidget(self.btn4)
            self.hboxcif.addWidget(self.btn5)
            self.buttom = QWidget()
            self.buttom.setLayout(self.hboxcif)

        if n==3:
            self.btn6 = QPushButton('Open peak')
            self.btn6.clicked.connect(self.readpeak)
            self.btn6.resize(self.btn6.sizeHint())

            self.btn7 = QPushButton('Edit peak')
            self.btn7.clicked.connect(qApp.quit)
            self.btn7.resize(self.btn7.sizeHint())

            self.btn8 = QPushButton('Save peak')
            self.btn8.clicked.connect(qApp.quit)
            self.btn8.resize(self.btn8.sizeHint())

            self.hboxpeak = QHBoxLayout(self)
            self.hboxpeak.addWidget(self.btn6)
            self.hboxpeak.addWidget(self.btn7)
            self.hboxpeak.addWidget(self.btn8)
            self.buttom = QWidget()
            self.buttom.setLayout(self.hboxpeak)

    def readint(self):
        m=1
        rf = ReadFile(m)
        WritetoTable(rf.getText(), self.table)
    def readcif(self):
        m=2
        rf = ReadFile(m)
        WritetoTable(rf.getText(), self.table)
    def readpeak(self):
        m=3
        rf = ReadFile(m)
        WritetoTable(rf.getText(), self.table)

class MyTable(QWidget):
    def __init__(self, mod, nc):
        super().__init__()
        self.Table(mod, nc)

    def Table(self, mod,  nc):
        self.mytable(mod, nc)
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)
        # self.show()

    def mytable(self, mod, nc):
        self.table = QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(nc)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        if mod==1:
            name = ["2Theta", 'Int', 'h', 'k', 'l', 'Multi']
            self.table.setHorizontalHeaderLabels(name)

        if mod == 2:
            name = ["2Theta", 'Int', 'h', 'k', 'l', 'Match']
            self.table.setHorizontalHeaderLabels(name)

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.table.removeRow(self.table.currentRow())
        # self.table.selectedItems().clear()

        self.table.horizontalHeader().setStyleSheet("border-bottom: 1px; border-style: solid; border-color: black; font-size: 11pt;")
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.verticalHeader().setStyleSheet("border: 1px solid black; font-size: 11pt;")

    def getTableFromTableFunc(self):
        return self.table

class ReadFile(QMainWindow):
    def __init__(self, m):
        super().__init__()
        self.showDialogRead(m)

    def showDialogRead(self, m):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        if m==1:
            name = 'Open Int file'
            roz = '*.txt'
        if m==2:
            name = 'Open Cif file'
            roz = '*.cif'
        if m==3:
            name = 'Open Peak file'
            roz = '*.txt'
        fname, ok = QFileDialog.getOpenFileName(self, name, desktop, roz)
        if not ok:
            return None
        if fname != '':
            f = open(fname, 'r')
            with f:
                self.file_text = f.read()
            print(self.file_text)

    def getText(self):
        return self.file_text

class WritetoTable(QWidget):
    def __init__(self, file_text, table):
        super().__init__()
        self.WriteTable(file_text, table)

    def WriteTable(self, file_text, table):
        filetext = file_text.split('\n')
        lenght = len(filetext)
        for i in range(lenght):
            filetext[i] = filetext[i].split()
            table.insertRow(i)
            for k in range(5):
                table.setItem(i,k,QTableWidgetItem(str(filetext[i][k])))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main_Window()
    # tab = TabWidget()
    # tabl = tab.getTable1()
    # window.initTabWidget(tab)
    window.show()
    sys.exit(app.exec_())