# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setTitle("")
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setObjectName("formLayout")
        self.rho_label = QtWidgets.QLabel(self.formGroupBox)
        self.rho_label.setObjectName("rho_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rho_label)
        self.beta_label = QtWidgets.QLabel(self.formGroupBox)
        self.beta_label.setObjectName("beta_label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.beta_label)
        self.rho_lineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.rho_lineEdit.setObjectName("rho_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rho_lineEdit)
        self.beta_lineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.beta_lineEdit.setObjectName("beta_lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.beta_lineEdit)
        self.niter_label = QtWidgets.QLabel(self.formGroupBox)
        self.niter_label.setObjectName("niter_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.niter_label)
        self.niter_spinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.niter_spinBox.setMinimum(1)
        self.niter_spinBox.setMaximum(1000)
        self.niter_spinBox.setProperty("value", 100)
        self.niter_spinBox.setObjectName("niter_spinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.niter_spinBox)
        self.epsilon_label = QtWidgets.QLabel(self.formGroupBox)
        self.epsilon_label.setObjectName("epsilon_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.epsilon_label)
        self.epsilon_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        self.epsilon_doubleSpinBox.setDecimals(8)
        self.epsilon_doubleSpinBox.setSingleStep(1e-06)
        self.epsilon_doubleSpinBox.setProperty("value", 1e-05)
        self.epsilon_doubleSpinBox.setObjectName("epsilon_doubleSpinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.epsilon_doubleSpinBox)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.rho_label.setText(("Rho"))
        self.beta_label.setText(("Beta"))
        self.rho_lineEdit.setText(("0.1,1,10"))
        self.beta_lineEdit.setText(("0.002,0.02,0.2,2"))
        self.niter_label.setText(("# of iterations"))
        self.epsilon_label.setText(("Epsilon"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

