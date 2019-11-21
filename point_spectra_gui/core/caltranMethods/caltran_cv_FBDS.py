import numpy as np
from PyQt5 import QtWidgets, QtCore

from point_spectra_gui.ui.caltran_cv_ForwardBackward_DS import Ui_Form
from point_spectra_gui.util.Modules import Modules

class Ui_Form(Ui_Form, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        pass

    def run(self):

        params = {'method':['Forward Backward DS'],
                  't': [float(i) for i in self.t_lineEdit.text().split(',')],
                  'svt':[float(i) for i in self.svt_lineEdit.text().split(',')],
                  'l1': [float(i) for i in self.L1_lineEdit.text().split(',')],
                  'epsilon': [float(i) for i in self.epsilon_lineEdit.text().split(',')],
                  'max_iter': [self.niter_spinBox.value()]
                  }

        return params


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
