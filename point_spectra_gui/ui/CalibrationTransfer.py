# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formGroupBox = QtWidgets.QGroupBox(Form)
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setObjectName("formLayout")
        self.infolabel = QtWidgets.QLabel(self.formGroupBox)
        self.infolabel.setObjectName("infolabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.infolabel)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.DataA_HLayout = QtWidgets.QHBoxLayout()
        self.DataA_HLayout.setObjectName("DataA_HLayout")
        self.DataA_label = QtWidgets.QLabel(self.formGroupBox)
        self.DataA_label.setObjectName("DataA_label")
        self.DataA_HLayout.addWidget(self.DataA_label)
        self.chooseDataA = QtWidgets.QComboBox(self.formGroupBox)
        self.chooseDataA.setObjectName("chooseDataA")
        self.DataA_HLayout.addWidget(self.chooseDataA)
        self.DataAMatch_label = QtWidgets.QLabel(self.formGroupBox)
        self.DataAMatch_label.setObjectName("DataAMatch_label")
        self.DataA_HLayout.addWidget(self.DataAMatch_label)
        self.chooseDataAMatch = QtWidgets.QComboBox(self.formGroupBox)
        self.chooseDataAMatch.setObjectName("chooseDataAMatch")
        self.DataA_HLayout.addWidget(self.chooseDataAMatch)
        self.verticalLayout_2.addLayout(self.DataA_HLayout)
        self.DataB_HLayout = QtWidgets.QHBoxLayout()
        self.DataB_HLayout.setObjectName("DataB_HLayout")
        self.DataB_label = QtWidgets.QLabel(self.formGroupBox)
        self.DataB_label.setObjectName("DataB_label")
        self.DataB_HLayout.addWidget(self.DataB_label)
        self.chooseDataB = QtWidgets.QComboBox(self.formGroupBox)
        self.chooseDataB.setObjectName("chooseDataB")
        self.DataB_HLayout.addWidget(self.chooseDataB)
        self.DataBMatch_label = QtWidgets.QLabel(self.formGroupBox)
        self.DataBMatch_label.setObjectName("DataBMatch_label")
        self.DataB_HLayout.addWidget(self.DataBMatch_label)
        self.chooseDataBMatch = QtWidgets.QComboBox(self.formGroupBox)
        self.chooseDataBMatch.setObjectName("chooseDataBMatch")
        self.DataB_HLayout.addWidget(self.chooseDataBMatch)
        self.verticalLayout_2.addLayout(self.DataB_HLayout)
        self.Transform_HLayout = QtWidgets.QHBoxLayout()
        self.Transform_HLayout.setObjectName("Transform_HLayout")
        self.DatatoTransform_label = QtWidgets.QLabel(self.formGroupBox)
        self.DatatoTransform_label.setObjectName("DatatoTransform_label")
        self.Transform_HLayout.addWidget(self.DatatoTransform_label)
        self.chooseDatatoTransform = QtWidgets.QComboBox(self.formGroupBox)
        self.chooseDatatoTransform.setObjectName("chooseDatatoTransform")
        self.Transform_HLayout.addWidget(self.chooseDatatoTransform)
        self.verticalLayout_2.addLayout(self.Transform_HLayout)
        self.Method_HLayout = QtWidgets.QHBoxLayout()
        self.Method_HLayout.setObjectName("Method_HLayout")
        self.Method_label = QtWidgets.QLabel(self.formGroupBox)
        self.Method_label.setObjectName("Method_label")
        self.Method_HLayout.addWidget(self.Method_label)
        self.chooseMethod = QtWidgets.QComboBox(self.formGroupBox)
        self.chooseMethod.setMinimumSize(QtCore.QSize(300, 0))
        self.chooseMethod.setObjectName("chooseMethod")
        self.chooseMethod.addItem("")
        self.chooseMethod.addItem("")
        self.chooseMethod.addItem("")
        self.Method_HLayout.addWidget(self.chooseMethod)
        self.verticalLayout_2.addLayout(self.Method_HLayout)
        self.methodlayout = QtWidgets.QVBoxLayout()
        self.methodlayout.setObjectName("methodlayout")
        self.verticalLayout_2.addLayout(self.methodlayout)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.SpanningRole, self.verticalLayout_2)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.formGroupBox.setTitle(("Calibration Transfer"))
        self.infolabel.setText(("Transfer will be for A to B."))
        self.DataA_label.setText(("Data set A:"))
        self.DataAMatch_label.setText(("Column to match on:"))
        self.DataB_label.setText(("Data Set B:"))
        self.DataBMatch_label.setText(("Column to match on:"))
        self.DatatoTransform_label.setText(("Data set to transform:"))
        self.Method_label.setText(("Method:"))
        self.chooseMethod.setItemText(0, ("Choose a method"))
        self.chooseMethod.setItemText(1, ("PDS - Piecewise Direct Standardization"))
        self.chooseMethod.setItemText(2, ("Ratio"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

