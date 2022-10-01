from PyQt5 import QtCore, QtGui, QtWidgets
import calculation_weight as cw
from fileworker import fileworker as fw


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(684, 821)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(1200, 1200))
        MainWindow.setSizeIncrement(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(170, 255, 127);\n"
"selection-color: rgb(255, 255, 0);\n"
"selection-background-color: rgb(255, 170, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(90, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sample_weight = QtWidgets.QLineEdit(self.centralwidget)
        self.sample_weight.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sample_weight.sizePolicy().hasHeightForWidth())
        self.sample_weight.setSizePolicy(sizePolicy)
        self.sample_weight.setMinimumSize(QtCore.QSize(150, 40))
        self.sample_weight.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.sample_weight.setObjectName("sample_weight")
        self.horizontalLayout_2.addWidget(self.sample_weight)
        self.sample_formula = QtWidgets.QLineEdit(self.centralwidget)
        self.sample_formula.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sample_formula.sizePolicy().hasHeightForWidth())
        self.sample_formula.setSizePolicy(sizePolicy)
        self.sample_formula.setMinimumSize(QtCore.QSize(200, 40))
        self.sample_formula.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.sample_formula.setObjectName("sample_formula")
        self.horizontalLayout_2.addWidget(self.sample_formula)
        self.Add_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Add_button.sizePolicy().hasHeightForWidth())
        self.Add_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Add_button.setFont(font)
        self.Add_button.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.Add_button.setObjectName("Add_button")
        self.horizontalLayout_2.addWidget(self.Add_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Open_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Open_button.sizePolicy().hasHeightForWidth())
        self.Open_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Open_button.setFont(font)
        self.Open_button.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.Open_button.setObjectName("Open_button")
        self.horizontalLayout_3.addWidget(self.Open_button)
        self.Calculate_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Calculate_button.sizePolicy().hasHeightForWidth())
        self.Calculate_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Calculate_button.setFont(font)
        self.Calculate_button.setStyleSheet("background-color: rgb(255, 255, 0);\n"
"alternate-background-color: rgb(85, 170, 255);")
        self.Calculate_button.setObjectName("Calculate_button")
        self.horizontalLayout_3.addWidget(self.Calculate_button)
        self.Clear_buttom = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Clear_buttom.sizePolicy().hasHeightForWidth())
        self.Clear_buttom.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Clear_buttom.setFont(font)
        self.Clear_buttom.setStyleSheet("\n"
"background-color: rgb(255, 170, 255);")
        self.Clear_buttom.setObjectName("Clear_buttom")
        self.horizontalLayout_3.addWidget(self.Clear_buttom)
        self.Save_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Save_button.sizePolicy().hasHeightForWidth())
        self.Save_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.Save_button.setFont(font)
        self.Save_button.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.Save_button.setObjectName("Save_button")
        self.horizontalLayout_3.addWidget(self.Save_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.report_list = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.report_list.sizePolicy().hasHeightForWidth())
        self.report_list.setSizePolicy(sizePolicy)
        self.report_list.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.report_list.setObjectName("report_list")
        self.verticalLayout_2.addWidget(self.report_list)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.Open_button.clicked.connect(self.OpenFile) # type: ignore
        self.Calculate_button.clicked.connect(self.Calculate) # type: ignore
        self.Clear_buttom.clicked.connect(self.Clear_all) # type: ignore
        self.Save_button.clicked.connect(self.SaveFile) # type: ignore
        self.Add_button.clicked.connect(self.Add_compounds) # type: ignore

    def OpenFile(self):
        self.im_data = fw.showDialogRead(fw)
        self.report_list.setText(str(self.im_data))

    def SaveFile(self, array):
        fw.showDialogWrite(fw, array)

    def Clear_all(self):
        self.report_list.clear()

    def Add_compounds(self):
        comp = self.sample_formula.text()
        self.report_list.append(comp)
        self.sample_formula.clear()

    def Calculate(self):
        mass = self.sample_weight.text()
        compounds_list = self.report_list.toPlainText()
        arr = cw.Calc_Molar_Mass.calc_molar_mass(cw, compounds_list)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MassCalculation"))
        self.label.setText(_translate("MainWindow", "sample weight, g"))
        self.label_2.setText(_translate("MainWindow", "Enter sample composition"))
        self.Add_button.setText(_translate("MainWindow", "Add "))
        self.Open_button.setText(_translate("MainWindow", "Open"))
        self.Calculate_button.setText(_translate("MainWindow", "Calculate"))
        self.Clear_buttom.setText(_translate("MainWindow", "Clear"))
        self.Save_button.setText(_translate("MainWindow", "Save"))
