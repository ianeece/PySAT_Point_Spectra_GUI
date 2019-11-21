import numpy as np
from PyQt5 import QtWidgets, QtCore

from point_spectra_gui.ui.caltran_cv_PDS_PLS import Ui_Form
from point_spectra_gui.util.Modules import Modules

class Ui_Form(Ui_Form, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def run(self):
        winsize_min = self.winsize_min_spinBox.value()
        winsize_max = self.winsize_max_spinBox.value()
        window_sizes = list(range(winsize_min,winsize_max+2,2))
        pls_nc = [int(i) for i in self.pls_nc_lineEdit.text().split(',')]
        params = {'method':['PDS-PLS - PDS using Partial Least Squares'],
                  'win_size': window_sizes,
                  'pls':[True],
                  'nc': pls_nc}
        return params

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
