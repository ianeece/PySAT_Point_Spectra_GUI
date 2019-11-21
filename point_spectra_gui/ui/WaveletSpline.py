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
        self.MinLevelLabel = QtWidgets.QLabel(self.groupBox)
        self.MinLevelLabel.setObjectName("MinLevelLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.MinLevelLabel)
        self.MinLevelSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.MinLevelSpinBox.setProperty("value", 6)
        self.MinLevelSpinBox.setObjectName("MinLevelSpinBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.MinLevelSpinBox)
        self.MaxLevelLabel = QtWidgets.QLabel(self.groupBox)
        self.MaxLevelLabel.setObjectName("MaxLevelLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.MaxLevelLabel)
        self.MaxLevelSpinBox = QtWidgets.QSpinBox(self.groupBox)
        self.MaxLevelSpinBox.setProperty("value", 10)
        self.MaxLevelSpinBox.setObjectName("MaxLevelSpinBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.MaxLevelSpinBox)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.MinLevelLabel.setText(("Min Level"))
        self.MaxLevelLabel.setText(("Max Level"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

