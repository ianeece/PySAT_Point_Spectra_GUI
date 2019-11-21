# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_loadData(object):
    def setupUi(self, loadData):
        loadData.setObjectName("loadData")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(loadData.sizePolicy().hasHeightForWidth())
        loadData.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(loadData)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(loadData)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.fileNameLabel = QtWidgets.QLabel(self.groupBox)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.gridLayout.addWidget(self.fileNameLabel, 0, 0, 1, 1)
        self.fileNameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.fileNameLineEdit.setObjectName("fileNameLineEdit")
        self.gridLayout.addWidget(self.fileNameLineEdit, 0, 1, 1, 1)
        self.newFilePushButton = QtWidgets.QPushButton(self.groupBox)
        self.newFilePushButton.setMaximumSize(QtCore.QSize(30, 16777215))
        self.newFilePushButton.setObjectName("newFilePushButton")
        self.gridLayout.addWidget(self.newFilePushButton, 0, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(loadData)
        QtCore.QMetaObject.connectSlotsByName(loadData)

    def retranslateUi(self, loadData):
        _translate = QtCore.QCoreApplication.translate
        loadData.setWindowTitle(("Form"))
        self.groupBox.setTitle(("Restore Regression Model"))
        self.fileNameLabel.setText(("Regression Model"))
        self.fileNameLineEdit.setText(("*.pickle"))
        self.newFilePushButton.setToolTip(("<html><head/><body><p>Press this to select a file</p></body></html>"))
        self.newFilePushButton.setText(("..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    loadData = QtWidgets.QWidget()
    ui = Ui_loadData()
    ui.setupUi(loadData)
    loadData.show()
    sys.exit(app.exec_())

