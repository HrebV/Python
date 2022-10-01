from PyQt5 import QtWidgets
from window import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot
import sys
# import func_but


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.main_function()

    def main_function(self):
       pass

    @pyqtSlot()
    def check_button(self):
        Oxide1 = self.ui.Oxide_1.text()
        Oxide2 = self.ui.Oxide_2.text()
        Oxide3 = self.ui.Oxide_3.text()
        Oxide4 = self.ui.Oxide_4.text()
        res = self.ui.Result.text()
        mass_of_mix = self.ui.mass_of_mixed_oxide.text()
        self.readoxide = []
        self.readoxide.append(Oxide1)
        self.readoxide.append(Oxide2)
        self.readoxide.append(Oxide3)
        self.readoxide.append(Oxide4)
        self.readoxide.append(res)
        self.oxide_list = list(func_but.comp_oxide.compare_oxide(self.readoxide))
        self.ui.Oxide_1.setReadOnly(True)
        self.ui.Oxide_2.setReadOnly(True)
        self.ui.Oxide_3.setReadOnly(True)
        self.ui.Oxide_4.setReadOnly(True)
        self.ui.Result.setReadOnly(True)
        self.ui.mass_of_mixed_oxide.setReadOnly(True)
        self.ui.Button_Edit.setEnabled(True)
        self.ui.Button_Clear.setEnabled(True)
        self.ui.Button_Calculate.setEnabled(True)
        self.ui.Button_Send_to_Report.setEnabled(True)

    def calc_button(self):
        calc = func_but.calc_oxide.calc_precorsors(self.oxide_list)
        self.molarmassoxide = calc[0]
        self.indexoxide = calc[1]
        self.indexper = calc[2]
        lmmo = len(self.molarmassoxide)
        self.Mper = float(self.molarmassoxide[lmmo-1])
        self.ui.amount_of_substance.setText(str(self.Mper))
        print('calc', self.molarmassoxide)

        self.mass = func_but.calc_oxide.mass_precursors(self.molarmassoxide, self.indexoxide, self.indexper, self.Mper)


    def edit_button(self):
        self.mass.clear()



    def write_button(self):
        self.Report_list.append(20*'#'+'SAMPLE CALCULATION'+20*'#')
        perovtext = '{:^35} {:^35} {:^35}'.format(self.oxide_list[len(self.oxide_list)-1], str(self.molarmassoxide[len(self.oxide_list)-1]), str(self.mper))
        self.Report_list.append(perovtext)
        self.Report_list.append('')
        self.Report_list.append(72*'*')
        text = '{:^30} {:^30} {:^30}'.format('oxide', 'M (g/mol)', 'm (g)')
        self.Report_list.append(text)
        self.Report_list.append(108*'-')
        for i in range(0, len(self.oxide_list)-1):

            oxidename = '{:^30}'.format(str(self.oxide_list[i]))
            mmass = '{:^30}'.format(str(self.molarmassoxide[i]))
            oxidemass = '{:^30}'.format(str(self.mass[i]))
            row = oxidename+mmass+oxidemass
            self.Report_list.append(row)

        self.Report_list.append(54*'#')
        self.Report_list.append('')

    def clear_button(self):
        pass

    def quit(self):
        exit(1)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())


