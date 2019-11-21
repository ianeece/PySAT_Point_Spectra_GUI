from PyQt5 import QtWidgets
from libpyhat.transform.baseline_code.min_spline import minimum_interp
from point_spectra_gui.ui.MinInterp import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        self.checkMinAndMax()
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        pass


    def run(self):
        interpkind = self.interpcomboBox.currentText()

        if interpkind == 'Quadratic Spline':
            kind = 'quadratic'
        if interpkind == 'Cubic Spline':
            kind = 'cubic'
        if interpkind == 'Linear':
            kind = 'linear'
        methodParameters = {'window': self.winsizeSpin.value(),
                            'kind': kind}

        return methodParameters, self.getChangedValues(methodParameters, minimum_interp())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
