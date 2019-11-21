from PyQt5 import QtWidgets
from sklearn.gaussian_process import GaussianProcessRegressor

from point_spectra_gui.ui.GP import Ui_Form
from point_spectra_gui.util.Modules import Modules


class Ui_Form(Ui_Form, GaussianProcessRegressor, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        # self.checkMinAndMax()
        self.connectWidgets()

    def get_widget(self):
        return self.formGroupBox

    def setHidden(self, bool):
        self.get_widget().setHidden(bool)

    def connectWidgets(self):
        # self.numOfComponenetsSpinBox.setValue(4)
        # self.setComboBox(self.regrComboBox, self._regression_types)
        # self.defaultComboItem(self.regrComboBox, self.regr)
        # self.setComboBox(self.corrComboBox, self._correlation_types)
        # self.defaultComboItem(self.corrComboBox, self.corr)
        # self.setComboBox(self.storageModeComboBox, ['light', 'full'])
        # self.defaultComboItem(self.storageModeComboBox, self.storage_mode)
        # self.verboseCheckBox.setChecked(self.verbose)
        # self.theta0DoubleSpinBox.setValue(self.theta0)
        # self.setComboBox(self.optimizerComboBox, self._optimizer_types)
        # self.defaultComboItem(self.optimizerComboBox, self.optimizer)
        # self.randomStartSpinBox.setValue(self.random_start)
        # self.normalizeCheckBox.setChecked(self.normalize)

        # self.numOfComponenetsSpinBox.setValue(4)
        # Kern
        self.setComboBox(self.kernComboBox, ['', 'ConstantKernel', 'RBF', 'Matern', 'RationalQuadratic', 'ExpSineSquared', 'DotProduct'])
        self.defaultComboItem(self.kernComboBox, '')

        # Alpha
        self.alphaSpinBox.setValue(self.alpha)

        # Optimizer
        self.setComboBox(self.optimizerComboBox, ['', 'fmin_l_bfgs_b'])
        self.defaultComboItem(self.optimizerComboBox, '')

        # n_restarts_optimizer
        self.restartsOptimizerSpinBox.setValue(self.n_restarts_optimizer)

        # normalize_y
        self.normalizeCheckBox.setChecked(self.normalize_y)

        # copy_X_train
        self.copyXCheckBox.setChecked(self.copy_X_train)
        # self.randomStartSpinBox.setValue(self.random_start)

        # random_state
        self.setComboBox(self.randomStateComboBox, ['', 'randomState()'])
        self.defaultComboItem(self.optimizerComboBox, '')

        # self.theta0DoubleSpinBox.setValue(self.n_restarts_optimizer)
        #
        # self.setComboBox(self.optimizerComboBox, self._optimizer_types)
        # self.defaultComboItem(self.optimizerComboBox, self.optimizer)
        #
        # self.randomStartSpinBox.setValue(self.random_start)
        # self.normalizeCheckBox.setChecked(self.normalize)

    def run(self):

        params = {
            'kernel' : self.kernComboBox.currentText(),
            'alpha' : self.alphaSpinBox.value(),
            'optimizer' : self.optimizerComboBox.currentText(),
            'n_restarts_optimizer' : self.restartsOptimizerSpinBox.value(),
            'normalize_y' : self.normalizeCheckBox.isChecked(),
            'copy_X_train' : self.copyXCheckBox.isChecked(),
            'random_state' : self.randomStateComboBox.currentText(),

        }
        #
        # params = {
        #     'reduce_dim': self.reductionMethodComboBox.currentText(),
        #     'n_components': self.numOfComponenetsSpinBox.value(),
        #     'regr': self.regrComboBox.currentText(),
        #     'corr': self.corrComboBox.currentText(),
        #     'storage_mode': self.storageModeComboBox.currentText(),
        #     'verbose': self.verboseCheckBox.isChecked(),
        #     'theta0': self.theta0DoubleSpinBox.value(),
        #     'normalize': self.normalizeCheckBox.isChecked(),
        #     'optimizer': self.optimizerComboBox.currentText(),
        #     'random_start': self.randomStartSpinBox.value(),
        # }

        return params, self.getChangedValues(params, GaussianProcessRegressor())


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
