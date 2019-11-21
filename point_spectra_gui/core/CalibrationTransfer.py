from PyQt5 import QtWidgets

from point_spectra_gui.ui.CalibrationTransfer import Ui_Form
from point_spectra_gui.util.Modules import Modules
from point_spectra_gui.core.caltranMethods import *
from libpyhat.transform import cal_tran
import pandas as pd
import numpy as np

class CalibrationTransfer(Ui_Form, Modules):

    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)
        self.caltranMethods()

    def get_widget(self):
        return self.formGroupBox

    def connectWidgets(self):
        self.methodlist = ['PDS - Piecewise Direct Standardization']
        self.setComboBox(self.chooseDataA, self.datakeys)
        self.setComboBox(self.chooseDataB, self.datakeys)
        self.setComboBox(self.chooseDatatoTransform,self.datakeys)
        try:
            self.setComboBox(self.chooseDataAMatch, self.data[self.chooseDataA.currentText()].df['meta'].columns.values)
            self.setComboBox(self.chooseDataBMatch, self.data[self.chooseDataB.currentText()].df['meta'].columns.values)
        except:
            pass

        self.chooseDataA.activated.connect(lambda: self.change_choices(self.chooseDataAMatch,self.chooseDataA))
        self.chooseDataB.activated.connect(lambda: self.change_choices(self.chooseDataBMatch, self.chooseDataB))
        self.chooseMethod.currentIndexChanged.connect(
            lambda: self.make_caltran_widget(self.chooseMethod.currentText()))

    def make_caltran_widget(self, alg, params=None):
        self.hideAll()
        print(alg)
        try:
            self.alg[alg].setHidden(False)
        except:
            pass

    def hideAll(self):
        for a in self.alg:
            self.alg[a].setHidden(True)

    def caltranMethods(self):
        self.alg = {'PDS - Piecewise Direct Standardization': caltran_PDS.Ui_Form(),
                    }

        for item in self.alg:
            self.alg[item].setupUi(self.Form)
            self.methodlayout.addWidget(self.alg[item].get_widget())
            self.alg[item].setHidden(True)

    def change_choices(self, combobox, datacombo):
        combobox.clear()
        try:
            choices = self.data[datacombo.currentText()].df['meta'].columns.values
        except:
            choices = ['No metadata columns!']

        combobox.addItems(choices)

    def run(self):
        datakeyA = self.chooseDataA.currentText()
        datakeyB = self.chooseDataB.currentText()
        datakeyC = self.chooseDatatoTransform.currentText()
        dataAmatchcol = self.chooseDataAMatch.currentText()
        dataBmatchcol = self.chooseDataBMatch.currentText()

        #get the data sets
        A = self.data[datakeyA].df
        B = self.data[datakeyB].df
        C = self.data[datakeyC].df

        assert (len(B['wvl'].columns) == len(C['wvl'].columns)),\
            'Data sets B and C have different numbers of spectral channels!'
        assert (B['wvl'].columns.values[-1] == C['wvl'].columns.values[-1]),\
            "Data set B and C wavelengths are not identical. Check rounding and/or resample one data set onto the other's wavelengths"
        A_mean, B_mean = caltran_prepare_data.prepare_data(A, B, dataAmatchcol, dataBmatchcol)

        method = self.chooseMethod.currentText()
        params = self.alg[method].run()

        ct_obj = cal_tran.cal_tran(method,params)
        ct_obj.derive_transform(A_mean['wvl'],B_mean['wvl'])


        pass

        # datakey_to_transform = self.CalTran_dataSetTransform.currentText()
        # datakey_ref = self.CalTran_dataSetRef.currentText()
        # match_on = self
        # print(self.data[datakey_ref].df.columns.levels[0])
        # self.data[datakey_to_interp].interp(self.data[datakey_ref].df['wvl'].columns)

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = CalibrationTransfer()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
