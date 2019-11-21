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
        self.formGroupBox.setObjectName("formGroupBox")
        self.formLayout = QtWidgets.QFormLayout(self.formGroupBox)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")

        # Kern
        self.kernLabel = QtWidgets.QLabel(self.formGroupBox)
        self.kernLabel.setObjectName("kernLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.kernLabel)
        self.kernComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.kernComboBox.setObjectName("kernComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.kernComboBox)

        # Alpha
        self.alphaLabel = QtWidgets.QLabel(self.formGroupBox)
        self.alphaLabel.setObjectName("alphaLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.alphaLabel)
        self.alphaSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.alphaSpinBox.setObjectName("alphaSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.alphaSpinBox)

        # Optimizer
        self.optimizerLabel = QtWidgets.QLabel(self.formGroupBox)
        self.optimizerLabel.setObjectName("optimizerLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.optimizerLabel)
        self.optimizerComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.optimizerComboBox.setObjectName("optimizerComboBox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.optimizerComboBox)

        # N-Restarts
        self.restartsOptimizerLabel = QtWidgets.QLabel(self.formGroupBox)
        self.restartsOptimizerLabel.setObjectName("restartsOptimizerLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.restartsOptimizerLabel)
        self.restartsOptimizerSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        self.restartsOptimizerSpinBox.setObjectName("restartsOptimizerSpinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.restartsOptimizerSpinBox)
        #
        # self.restartsOptimizerLabel = QtWidgets.QLabel(self.formGroupBox)
        # self.restartsOptimizerLabel.setObjectName("restartsOptimizerLabel")
        # self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.restartsOptimizerLabel)
        # self.restartsOptimizerCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        # self.restartsOptimizerCheckBox.setObjectName("restartsOptimizerCheckBox")
        # self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.restartsOptimizerCheckBox)

        # Normalize
        self.normalizeLabel = QtWidgets.QLabel(self.formGroupBox)
        self.normalizeLabel.setObjectName("normalizeLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.normalizeLabel)
        self.normalizeCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.normalizeCheckBox.setObjectName("normalizeCheckBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.normalizeCheckBox)

        # Copy X Train
        self.copyXLabel = QtWidgets.QLabel(self.formGroupBox)
        self.copyXLabel.setObjectName("copyXLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.copyXLabel)
        self.copyXCheckBox = QtWidgets.QCheckBox(self.formGroupBox)
        self.copyXCheckBox.setObjectName("copyXCheckBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.copyXCheckBox)

        # random_state
        self.randomStateLabel = QtWidgets.QLabel(self.formGroupBox)
        self.randomStateLabel.setObjectName("randomStateLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.randomStateLabel)
        self.randomStateComboBox = QtWidgets.QComboBox(self.formGroupBox)
        self.randomStateComboBox.setObjectName("randomStateComboBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.randomStateComboBox)

        # self.randomStartLabel = QtWidgets.QLabel(self.formGroupBox)
        # self.randomStartLabel.setObjectName("randomStartLabel")
        # self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.randomStartLabel)
        # self.randomStartSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        # self.randomStartSpinBox.setObjectName("randomStartSpinBox")
        # self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.randomStartSpinBox)

        # self.theta0DoubleSpinBox = QtWidgets.QDoubleSpinBox(self.formGroupBox)
        # self.theta0DoubleSpinBox.setObjectName("theta0DoubleSpinBox")
        # self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.theta0DoubleSpinBox)
        # self.reductionMethodComboBox = QtWidgets.QComboBox(self.formGroupBox)
        # self.reductionMethodComboBox.setObjectName("reductionMethodComboBox")
        # self.reductionMethodComboBox.addItem("")
        # self.reductionMethodComboBox.addItem("")
        # self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.reductionMethodComboBox)
        # self.reductionMethodLabel = QtWidgets.QLabel(self.formGroupBox)
        # self.reductionMethodLabel.setObjectName("reductionMethodLabel")
        # self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.reductionMethodLabel)
        # self.numOfComponenetsLabel = QtWidgets.QLabel(self.formGroupBox)
        # self.numOfComponenetsLabel.setObjectName("numOfComponenetsLabel")
        # self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.numOfComponenetsLabel)
        # self.numOfComponenetsSpinBox = QtWidgets.QSpinBox(self.formGroupBox)
        # self.numOfComponenetsSpinBox.setObjectName("numOfComponenetsSpinBox")
        # self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.numOfComponenetsSpinBox)
        self.verticalLayout.addWidget(self.formGroupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(("Form"))
        self.formGroupBox.setTitle(("Gaussian Process"))
        self.kernLabel.setText(("Kernel Types"))
        self.alphaLabel.setText(("Alpha"))
        self.optimizerLabel.setText(("Optimizer"))
        self.restartsOptimizerLabel.setText(("N Restarts Optimizer"))
        self.normalizeLabel.setText(("Normalize Y"))
        self.copyXLabel.setText(("Copy X Train"))
        self.randomStateLabel.setText(("Random State"))

        # self.normalizeLabel.setText(("Normalize"))
        # self.reductionMethodComboBox.setItemText(0, ("PCA"))
        # self.reductionMethodComboBox.setItemText(1, ("ICA"))
        # self.reductionMethodLabel.setText(("Choose dimensionality reduction method:"))
        # self.numOfComponenetsLabel.setText(("Number of Components"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
