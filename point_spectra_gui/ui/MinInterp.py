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
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.winsizeLabel = QtWidgets.QLabel(self.groupBox)
        self.winsizeLabel.setObjectName("winsizeLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.winsizeLabel)
        self.winsizeSpin = QtWidgets.QSpinBox(self.groupBox)
        self.winsizeSpin.setProperty("value", 50)
        self.winsizeSpin.setObjectName("winsizeSpin")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.winsizeSpin)
        self.interpLabel = QtWidgets.QLabel(self.groupBox)
        self.interpLabel.setObjectName("interpLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.interpLabel)
        self.interpcomboBox = QtWidgets.QComboBox(self.groupBox)
        self.interpcomboBox.setObjectName("interpcomboBox")
        self.interpcomboBox.addItem("")
        self.interpcomboBox.addItem("")
        self.interpcomboBox.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.interpcomboBox)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.winsizeLabel.setText(("Window size"))
        self.interpLabel.setText(("Interpolation type"))
        self.interpcomboBox.setItemText(0, ("Cubic Spline"))
        self.interpcomboBox.setItemText(1, ("Quadratic Spline"))
        self.interpcomboBox.setItemText(2, ("Linear"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

