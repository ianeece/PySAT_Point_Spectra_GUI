# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.specifyAFilenameLabel = QtWidgets.QLabel(self.groupBox)
        self.specifyAFilenameLabel.setObjectName("specifyAFilenameLabel")
        self.gridLayout.addWidget(self.specifyAFilenameLabel, 2, 0, 1, 1)
        self.specifyAFilenameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.specifyAFilenameLineEdit.setObjectName("specifyAFilenameLineEdit")
        self.gridLayout.addWidget(self.specifyAFilenameLineEdit, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 1, 1, 1)
        self.chooseModelLabel = QtWidgets.QLabel(self.groupBox)
        self.chooseModelLabel.setObjectName("chooseModelLabel")
        self.gridLayout.addWidget(self.chooseModelLabel, 0, 0, 1, 2)
        self.chooseModelComboBox = QtWidgets.QComboBox(self.groupBox)
        self.chooseModelComboBox.setObjectName("chooseModelComboBox")
        self.gridLayout.addWidget(self.chooseModelComboBox, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.groupBox.setTitle(("Save Regression Model"))
        self.specifyAFilenameLabel.setText(("Specify a filename:"))
        self.specifyAFilenameLineEdit.setText(("output.pickle"))
        self.pushButton.setText(("..."))
        self.chooseModelLabel.setText(("Choose Regression Model to save:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

