from PyQt5 import QtWidgets
import pickle

from point_spectra_gui.ui.RestoreRegressionModel import Ui_loadData
from point_spectra_gui.util.Modules import Modules


class RestoreRegressionModel(Ui_loadData, Modules):
    """
    Restores a previously pickled Regression Model into the UI.
    The data needs to be a .pickle file in order for this widget to work
    """

    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        self.newFilePushButton.clicked.connect(lambda: self.getDataButton_clicked(self.fileNameLineEdit))

    def getDataButton_clicked(self, lineEdit):
        starting_path = self.outpath + "/saved_models"

        filename, _filter = QtWidgets.QFileDialog.getOpenFileName(None, "Select Regression Model File", starting_path, "(*.pickle)")
        lineEdit.setText(filename)
        if lineEdit.text() == "":
            lineEdit.setText("*.pickle")

    def run(self, filename = None, keyname = None):
        if filename == None:
            filename = self.fileNameLineEdit.text()
        print('Loading Regression Model From: ' + str(filename))

        pickle_file = open(filename, "rb")

        regression_model = pickle.load(pickle_file)
        restored_modelkey = regression_model.modelkey

        pickle_file.close()

        self.models[restored_modelkey] = regression_model
        self.modelkeys.append(restored_modelkey)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = RestoreRegressionModel()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
