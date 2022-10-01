from PyQt5.QtWidgets import QFileDialog
import os

class fileworker():

    def showDialogRead(self):
        desktop = os.path.join(os.path.join(os.environ['HOMEPATH']), '  ')
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        fname, ok = QFileDialog.getOpenFileName(dlg, 'Open file', desktop, '*.txt')
        if not ok:
            return None
        if fname:
            with open(fname, 'r') as f:
                im_data = f.read()

        return str(im_data)


    def showDialogWrite(self, array_1):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        desktop = os.path.join(os.path.join(os.environ['HOMEPATH'], 'Deformation_for_'))
        flname, ok = QFileDialog.getSaveFileName(dlg, 'Save file', desktop, '*.txt')
        if not ok:
            return None
        if flname != '':
            f = open(flname, 'w')
            with f:
                for i in range(len(array_1)):
                    f.write(str(array_1[i]) + '\n')
                f.close()
