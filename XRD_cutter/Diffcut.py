#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import numpy as np
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication, QTextEdit, QWidget, QFileDialog,
                             QLabel, QGridLayout, QLineEdit, QTextEdit, QHBoxLayout, QVBoxLayout, QToolTip,
                             QPushButton, QDesktopWidget, QSplitter, QMessageBox,QSizePolicy, QSpacerItem, QDoubleSpinBox)

from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

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
        self.initUI()

    def initUI(self):
        widget = QWidget(self)
        self.setCentralWidget(widget)

        #  створюємо грфік + тубар

        self.Open_Diff_Plot = PlotCanvas(self, width=10, height=8)
        self.tb = NavigationToolbar(self.Open_Diff_Plot, self)

        # створюємо кнопки і поля
        self.btn = QPushButton('Cut', widget)
        self.btn.clicked.connect(self.cut)
        self.btn.setEnabled(False)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(720, 40)
        if not self.btn.isEnabled():
           self.btn.setToolTip('Please, <b>download</b> *.pro file')

        self.Diff_step = QLabel('Define Step')
        self.Theta0 = QLabel('Start angle')
        self.Theta_Last = QLabel('End angle')
        self.Diff_step_line = QLineEdit('')
        self.Diff_step_line.setReadOnly(True)
        self.Theta0_line = QLineEdit()
        self.Theta0_line.setReadOnly(True)
        self.Theta_Last_line = QDoubleSpinBox()
        self.Theta_Last_line.move(720, 40)

        self.Open_Diff = QLabel('Opened file')
        self.Save_Diff = QLabel('Shortened file')
        self.Open_Diff_Box = QTextEdit('Initial diffraction pattern')
        self.Open_Diff_Box.setReadOnly(True)
        self.Save_Diff_Box = QTextEdit('Shortened diffraction pattern')
        self.Save_Diff_Box.setReadOnly(True)

# розмітка (шар поміщаємо у віджет)
        self.box1 = QHBoxLayout(widget)
        self.box1.addWidget(self.Diff_step)
        self.box1.addWidget(self.Diff_step_line)
        self.box1.addWidget(self.Theta0)
        self.box1.addWidget(self.Theta0_line)
        self.box1.addWidget(self.Theta_Last)
        self.box1.addWidget(self.Theta_Last_line)
        self.box1.addWidget(self.btn)
        self.box1.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.top_widget = QWidget()
        self.top_widget.setLayout(self.box1)

        self.box2 = QVBoxLayout(widget)
        self.box2.addWidget(self.Open_Diff)
        self.box2.addWidget(self.Open_Diff_Box)
        self.box2.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.left_widget = QWidget()
        self.left_widget.setLayout(self.box2)

        self.box3 = QVBoxLayout(widget)
        self.box3.addWidget(self.Save_Diff)
        self.box3.addWidget(self.Save_Diff_Box)
        self.box3.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.right_widget = QWidget()
        self.right_widget.setLayout(self.box3)

        self.box4 = QHBoxLayout(widget)
        self.box4.addWidget(self.left_widget)
        self.box4.addWidget(self.right_widget)
        self.bottom_widget = QWidget()
        self.bottom_widget.setLayout(self.box4)

        self.box5 = QVBoxLayout(widget)
        self.box5.addWidget(self.Open_Diff_Plot)
        self.box5.addWidget(self.tb)
        self.box5.addItem(QSpacerItem(0, 0,  QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.plot_widget = QWidget()
        self.plot_widget.setLayout(self.box5)

        self.box6 = QVBoxLayout(widget)
        self.box6.addWidget(self.top_widget)
        self.box6.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.box6.addWidget(self.bottom_widget)
        self.box6.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.box6.addWidget(self.plot_widget)
        self.box6.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.all_widget = QWidget()
        self.all_widget.setLayout(self.box6)

        # vbox = QVBoxLayout(widget)
        # vbox.addWidget(self.all_widget)
        # vbox.addItem(QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding))
        # self.setLayout(vbox)

# статут бар
        self.statusBar()

# відкрити файл меню
        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialogRead)
        self.toolbar = self.addToolBar('Open File')
        self.toolbar.addAction(openFile)

# зберегти файл меню
        saveFile = QAction(QIcon('save.png'), 'Save', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save new File')
        saveFile.triggered.connect(self.showDialogSave)
        self.toolbar1 = self.addToolBar('Save File')
        self.toolbar1.addAction(saveFile)
# очистити всі поля
        clearW = QAction(QIcon('clear.png'), 'Clear', self)
        clearW.setShortcut('Ctrl+N')
        clearW.setStatusTip('Clear workspace')
        clearW.triggered.connect(self.clearws)
        self.toolbar2 = self.addToolBar('Clear workspace')
        self.toolbar2.addAction(clearW)

# закрити програму

        exitProg = QAction(QIcon('exit.png'), 'Exit', self)
        exitProg.setShortcut('Ctrl+Q')
        exitProg.setStatusTip('Close Program')
        exitProg.triggered.connect(qApp.quit)
        self.toolbar3= self.addToolBar('Close Program')
        self.toolbar3.addAction(exitProg)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)
        fileMenu.addAction(saveFile)
        fileMenu.addAction(clearW)
        fileMenu.addAction(exitProg)

        self.setGeometry(400, 50, 700, 680)
        self.setWindowTitle('DiffCut')
        self.setWindowIcon(QIcon('window.ico'))
        self.show()

    def clearws(self):
        self.Theta0_line.clear()
        self.Diff_step_line.clear()
        self.Open_Diff_Box.clear()
        self.Save_Diff_Box.clear()

    def winitial(self):
        # отримуємо початкову  дифрактограму і розбиваємо її поелементно
        sttext = self.Open_Diff_Box.toPlainText()
        sttext = sttext.split('\n')
        fline = sttext[0].split(' ')
        # рахуємо мінімальний кут обрізання 1 рядка і записуємо у поле
        a = self.Theta0_line.text()
        if a == '':
            stspin = round(float(fline[2]) * 10, 3)
            c = round(float(fline[1]) + float(fline[2]) * 10, 3)
            self.Theta0_line.setText(fline[1])
            self.Diff_step_line.setText(fline[2])
            self.Theta_Last_line.setDecimals(3)
            self.Theta_Last_line.setValue(float(c))
            self.Theta_Last_line.setSingleStep(float(stspin))

        res = ''
        for par in sttext:
            res += '' + ''.join(par)
        res = res.split(' ')
        res.remove('')
        lend = len(res)

        x = list()
        y = list()
        for i in range(round(lend) - 2):  # -2 бо символ E і пустий рядок у сомому файлі *.pro
            xf = float(fline[1]) + int(i) * float(fline[2])
            yf = res[i + 2]
            x.append(str(round(xf, 3)))
            y.append(str(yf))

        self.Open_Diff_Plot.plot([x, y])

    def showDialogRead(self):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        fname, ok = QFileDialog.getOpenFileName(self, 'Open file', desktop, '*.pro')
        if not ok:
            return None
        if fname:
            with open(fname, 'r') as f:
                file_text = f.read()
                self.Open_Diff_Box.setText(file_text)
            self.btn.setEnabled(True)
            self.btn.setToolTip('Press <b>Сut</b> and cut off diffraction pattern')
        self.winitial()

    def showDialogSave(self):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        flname, ok = QFileDialog.getSaveFileName(self, 'Save file', desktop, '*.pro')
        if not ok:
            return None
        if flname != '':
            f = open(flname, 'w')
            with f:
                my_text = self.Save_Diff_Box.toPlainText()
                f.write(my_text)

# Qtextedit  отримати змінну за допомогою метода toPlainText(),  вставити текс setText()
# Qlineedit  отримати змінну за допомогою метода text(), вставити текс setText(),   ** setReadOnly(True)

    def cut(self):
        stext = self.Open_Diff_Box.toPlainText()
        stext = stext.split('\n')
        lenght = len(stext)
        fine = stext[0].split(' ')
        t0 = fine[1]
        step = fine[2]
        tend = round(self.Theta_Last_line.value(),3)
        count_line = (float(tend)-float(t0))/(float(step)*10)
        stext[0] = ' {} {}'.format(tend, step)

        self.Save_Diff_Box.clear()

        for i in range(lenght):
            if i == 0 or round(count_line) < int(i):
                self.Save_Diff_Box.append(str(stext[i]))

        temp = self.Open_Diff_Box.toPlainText()
        newOp = self.Save_Diff_Box.toPlainText()
        self.Open_Diff_Box.setText(newOp)
        self.winitial()
        self.Open_Diff_Box.setText(temp)
        del temp
        del newOp

class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=10, height=8, dpi=120):
        fig = Figure(figsize=(width, height), dpi=dpi)
        # self.axes = fig.add_subplot(111)

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)

        FigureCanvas.updateGeometry(self)
        dp = list()
        self.plot(dp)

    def plot(self, dp):
        if len(dp) == 0:
            return
        xdata = dp[0].copy()
        ydata = dp[1].copy()
        del ydata[-1]
        del xdata[-1]
        nxdata = [float(i) for i in xdata]
        nydata = [float(i) for i in ydata]
        ax = self.figure.add_subplot(111)
        self.figure.subplots_adjust(bottom=0.25, left=0.2)
        ax.clear()
        ax.plot(nxdata, nydata, 'r-')
        ax.set_title('Diffraction pattern', fontsize=12, fontname='Times New Roman')
        ax.set_xlabel('2Theta', fontsize=14, fontname='Times New Roman')
        ax.set_ylabel('Intensity', fontsize=16, fontname='Times New Roman')
        ax.tick_params(axis='both', rotation=45, labelsize=8)
        ax.set_facecolor('lightgoldenrodyellow')
        ax.autoscale(enable=True, axis='x', tight=True)
        ax.autoscale(enable=True, axis='y', tight=True)
        self.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main_Window()
    window.show()
    sys.exit(app.exec_())