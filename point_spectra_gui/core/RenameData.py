from PyQt5 import QtWidgets

from point_spectra_gui.ui.RenameData import Ui_Form
from point_spectra_gui.util.Modules import Modules


class RenameData(Ui_Form, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def rename_data(self):
        print('Called data')
        new_data_name = self.toDataLineEdit.text()
        old_data_name = self.renameDataComboBox.currentText()
        if new_data_name != '':
            self.datakeys.append(new_data_name)
            self.data[new_data_name] = self.data[old_data_name]
            for i in range(len(self.datakeys) - 1):
                if self.datakeys[i] == old_data_name:
                    del self.datakeys[i]

    def connectWidgets(self):
        self.setComboBox(self.renameDataComboBox, self.datakeys)
        self.toDataLineEdit.editingFinished.connect(lambda: self.rename_data())

    def run(self):
        print('Called run')
        self.rename_data()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = RenameData()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
