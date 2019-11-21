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
        self.t_label = QtWidgets.QLabel(self.formGroupBox)
        self.t_label.setObjectName("t_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.t_label)
        self.t_lineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.t_lineEdit.setObjectName("t_lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.t_lineEdit)
        self.svt_label = QtWidgets.QLabel(self.formGroupBox)
        self.svt_label.setObjectName("svt_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.svt_label)
        self.svt_lineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.svt_lineEdit.setObjectName("svt_lineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.svt_lineEdit)
        self.L1_label = QtWidgets.QLabel(self.formGroupBox)
        self.L1_label.setObjectName("L1_label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.L1_label)
        self.L1_lineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.L1_lineEdit.setObjectName("L1_lineEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.L1_lineEdit)
        self.epsilon_label = QtWidgets.QLabel(self.formGroupBox)
        self.epsilon_label.setObjectName("epsilon_label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.epsilon_label)
        self.epsilon_lineEdit = QtWidgets.QLineEdit(self.formGroupBox)
        self.epsilon_lineEdit.setObjectName("epsilon_lineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.epsilon_lineEdit)
        self.niter_spinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.niter_spinBox.setMinimum(1)
        self.niter_spinBox.setProperty("value", 20)
        self.niter_spinBox.setObjectName("niter_spinBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.niter_spinBox)
        self.niter_label = QtWidgets.QLabel(self.formGroupBox)
        self.niter_label.setObjectName("niter_label")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.niter_label)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.t_label.setText(("t"))
        self.t_lineEdit.setText(("0.001"))
        self.svt_label.setText(("svt"))
        self.svt_lineEdit.setText(("1"))
        self.L1_label.setText(("L1"))
        self.L1_lineEdit.setText(("1"))
        self.epsilon_label.setText(("Epsilon"))
        self.epsilon_lineEdit.setText(("0.00001"))
        self.niter_label.setText(("# of iterations"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

