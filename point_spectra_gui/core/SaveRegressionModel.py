from PyQt5 import QtWidgets
import pickle

from point_spectra_gui.ui.SaveRegressionModel import Ui_Form
from point_spectra_gui.util.Modules import Modules


class SaveRegressionModel(Ui_Form, Modules):
    """
    Saves a previously generated Regression Model into a binary pickle file.
    Can be re-opened with the Restore Regression Model Widget.
    """
    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self, setup=False):
        self.setComboBox(self.chooseModelComboBox, self.modelkeys)
        self.chooseModelComboBox.currentIndexChanged.connect(self.on_combobox_changed, self.chooseModelComboBox.currentIndex())
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

        if self.chooseModelComboBox.count() > 0:
            self.specifyAFilenameLineEdit.setText(self.chooseModelComboBox.currentText() + ".pickle")

    def setup(self):
        self.connectWidgets(setup=True)

    def on_combobox_changed(self, value):
        self.specifyAFilenameLineEdit.setText(self.chooseModelComboBox.currentText() + ".pickle")

    def run(self):
        modelkey = self.chooseModelComboBox.currentText()

        filename = self.specifyAFilenameLineEdit.text()

        # If no filepath is specified, default the path to the saved_models
        # folder.
        if "/" not in filename:
            filename = self.outpath + "/saved_models/" + filename

        if modelkey != "":
            # Isolate the regression object
            regression_model = self.models[modelkey]
            regression_model.modelkey = modelkey

            # Pickle the object.
            pickle.dump(regression_model, open(filename, "wb"))
        else:
            print("Error: No Regression Model Selected!")


    def on_pushButton_clicked(self):
        defaultName = "saved_models/" + self.chooseModelComboBox.currentText()
        filename, _filter = QtWidgets.QFileDialog.getSaveFileName(None, "Save Regression Model",
        self.outpath + defaultName, "(*.pickle)")

        self.specifyAFilenameLineEdit.setText(filename + ".pickle")
        if self.specifyAFilenameLineEdit.text() == "":
            self.specifyAFilenameLineEdit.setText("output.pickle")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = SaveRegressionModel()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
