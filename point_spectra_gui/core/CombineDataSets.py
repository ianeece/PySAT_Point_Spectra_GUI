import pandas as pd
from PyQt5 import QtWidgets

from point_spectra_gui.ui.CombineDataSets import Ui_Form
from point_spectra_gui.util.Modules import Modules
from point_spectra_gui.util.spectral_data import spectral_data

class CombineDataSets(Ui_Form, Modules):
    """
    Combine the various datasets into one bigger dataset
    This is still in Beta and needs to be improved.
    This is in part due to the fact that we are using multidimensional columns to reference data
    """

    def setupUi(self, Form):
        self.Form = Form
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self,setup=False):
        self.setComboBox(self.dataSet1ComboBox, self.datakeys)
        self.setComboBox(self.dataSet2ComboBox, self.datakeys)
        if setup == False:
            self.outputToDataSetLineEdit.editingFinished.connect(self.combine_data)

    def combine_data(self):
        dataSet1 = self.dataSet1ComboBox.currentText()
        dataSet2 = self.dataSet2ComboBox.currentText()
        newkey = self.outputToDataSetLineEdit.text()
        if newkey != '':
            self.datakeys.append(newkey)
            try:
                self.data[newkey] = spectral_data(pd.concat([self.data[dataSet1].df, self.data[dataSet2].df], ignore_index=True))
            except:
                pass

    def setup(self):
        self.connectWidgets(setup=True)

    def run(self):
        self.combine_data()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
