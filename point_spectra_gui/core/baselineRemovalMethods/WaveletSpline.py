from PyQt5 import QtWidgets
from libpyhat.transform.baseline_code.wavelet_spline import wavelet_spline
from point_spectra_gui.ui.WaveletSpline import Ui_Form
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
        self.MinLevelSpinBox.valueChanged.connect(lambda: self.setLimits())
        self.MaxLevelSpinBox.valueChanged.connect(lambda: self.setLimits())

    def setLimits(self):
        try:
            self.MaxLevelSpinBox.setMinimum(self.MinLevelSpinBox.value())
            self.MinLevelSpinBox.setMaximum(self.MaxLevelSpinBox.value())
        except:
            pass

    def run(self):
        methodParameters = {'level': self.MaxLevelSpinBox.value(),
                            'levelmin': self.MinLevelSpinBox.value()}

        return methodParameters, self.getChangedValues(methodParameters, wavelet_spline())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
