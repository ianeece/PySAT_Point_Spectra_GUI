from PyQt5.QtCore import QStringListModel
from PyQt5.QtWidgets import QCompleter
import numpy as np
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt

from point_spectra_gui.ui.Plot import Ui_Form
from point_spectra_gui.util.Modules import Modules
from point_spectra_gui.util.plots import make_plot

class Plot(Ui_Form, Modules):
    def setupUi(self, Form):
        super().setupUi(Form)
        Modules.setupUi(self, Form)

    def get_widget(self):
        return self.groupBox

    def connectWidgets(self):
        color_list = ["Red",
                      "Green",
                      "Blue",
                      "Cyan",
                      "Yellow",
                      "Magenta",
                      "Black"]
        line_list = ["No Line",
                     "Line",
                     "Dashed Line",
                     "Dotted Line"]
        marker_list = ["Circles",
                       "Squares",
                       "Diamonds",
                       "Triangle Up",
                       "Triangle Down",
                       "Triangle Left",
                       "Triangle Right",
                       "None"]
        completer = QCompleter()
        self.chooseXVariableComboBox.setMaximumWidth(200)
        self.chooseYVariableComboBox.setMaximumWidth(200)
        self.changeComboListVars(self.chooseXVariableComboBox, self.get_choices())
        self.figureNameLineEdit.setCompleter(completer)
        model = QStringListModel()
        completer.setModel(model)
        self.get_data(model)
        choices2 = ['None']
        datakey_choices = self.datakeys
        for choice in datakey_choices:
            choices2.append(choice)
        datakey_choices = choices2

        self.setComboBox(self.chooseDataComboBox, datakey_choices)
        self.changeComboListVars(self.chooseYVariableComboBox, self.get_choices())
        self.setComboBox(self.colorComboBox, color_list)
        self.changeComboListVars(self.comboBoxcolorvar, self.get_choices())

        self.setComboBox(self.lineComboBox, line_list)
        self.setComboBox(self.markerComboBox, marker_list)
        self.alphaDoubleSpinBox.setValue(0.25)
        self.alphaDoubleSpinBox.setSingleStep(0.1)
        self.alphaDoubleSpinBox.setMaximum(1)
        self.xMinDoubleSpinBox.setMaximum(110)
        self.xMaxDoubleSpinBox.setMaximum(110)
        self.yMinDoubleSpinBox.setMaximum(110)
        self.yMaxDoubleSpinBox.setMaximum(110)
        self.plotFilenamePushButton.clicked.connect(self.plotFilenamePushButton_clicked)
        self.chooseDataComboBox.activated[int].connect(
            lambda: self.changeComboListVars(self.chooseXVariableComboBox, self.get_choices()))
        self.chooseDataComboBox.activated[int].connect(
            lambda: self.changeComboListVars(self.chooseYVariableComboBox, self.get_choices()))
        self.chooseDataComboBox.activated[int].connect(
             lambda: self.changeComboListVars(self.comboBoxcolorvar, self.get_choices()))
        self.chooseDataComboBox.activated[int].connect(
            lambda: self.get_minmax(self.xMinDoubleSpinBox, self.xMaxDoubleSpinBox,
                                    self.chooseXVariableComboBox.currentText()))
        self.chooseDataComboBox.activated[int].connect(
            lambda: self.get_minmax(self.yMinDoubleSpinBox, self.yMaxDoubleSpinBox,
                                    self.chooseYVariableComboBox.currentText()))
        self.chooseXVariableComboBox.activated[int].connect(
            lambda: self.get_minmax(self.xMinDoubleSpinBox, self.xMaxDoubleSpinBox,
                                    self.chooseXVariableComboBox.currentText()))
        self.chooseYVariableComboBox.activated[int].connect(
            lambda: self.get_minmax(self.yMinDoubleSpinBox, self.yMaxDoubleSpinBox,
                                    self.chooseYVariableComboBox.currentText()))
        self.comboBoxcolorvar.currentIndexChanged[int].connect(self.disable_colors)

    def disable_colors(self):
          if self.comboBoxcolorvar.currentText() == 'None':
               self.colorComboBox.setDisabled(False)
               self.legendLineEdit.setDisabled(False)
          elif self.comboBoxcolorvar.currentText() != 'None':
              self.colorComboBox.setDisabled(True)
              self.legendLineEdit.setDisabled(True)

    def run(self):
        cmap = 'viridis'
        datakey = self.chooseDataComboBox.currentText()
#        datakey = datakey.append(['Choose Data'])
        xvar = self.chooseXVariableComboBox.currentText()
        yvar = self.chooseYVariableComboBox.currentText()
        colorvar = self.comboBoxcolorvar.currentText()
        # if colorvar != 'None':
        #    colorval = self.data[datakey].df[('comp', colorvar)]
        # elif colorvar == 'None':
        #    colorval = None
        if colorvar != 'None':
            try:
                colorval = self.data[datakey].df[('comp', colorvar)]
            except:
                try:
                    colorval = self.data[datakey].df[('meta', colorvar)]
                except:
                    try:
                        colorval = self.data[datakey].df[('K-means', colorvar)]
                    except:
                        try:
                            colorval = self.data[datakey].df[('Spectral', colorvar)]
                        except:
                            pass
        elif colorvar == 'None':
            colorval = None

        figname = self.figureNameLineEdit.text()
        title = self.plotTitleLineEdit.text()
        xrange = self.xMinDoubleSpinBox.value(), self.xMaxDoubleSpinBox.value()
        yrange = self.yMinDoubleSpinBox.value(), self.yMaxDoubleSpinBox.value()
        xtitle = self.xTitleLineEdit.text()
        ytitle = self.yTitleLineEdit.text()
        lbl = self.legendLineEdit.text()
        one_to_one = self.oneToOneCheckBox.isChecked()

        color = self.colorComboBox.currentText()
        #  if user chosen color var, color based on that
#        else, use combobox

        alpha = self.alphaDoubleSpinBox.value()
        annot_mask = None
        colortitle = ''
        dpi = 1000

        if color == 'Red':
            color = [1, 0, 0, alpha]
        elif color == 'Green':
            color = [0, 1, 0, alpha]
        elif color == 'Blue':
            color = [0, 0, 1, alpha]
        elif color == 'Cyan':
            color = [0, 1, 1, alpha]
        elif color == 'Yellow':
            color = [1, 1, 0, alpha]
        elif color == 'Magenta':
            color = [1, 0, 1, alpha]
        elif color == 'Black':
            color = [0, 0, 0, alpha]

        marker = self.markerComboBox.currentText()
        if marker == 'Circles':
            marker = 'o'
        if marker == 'Squares':
            marker = 's'
        if marker == 'Diamonds':
            marker = 'D'
        if marker == 'Triangle Up':
            marker = '^'
        if marker == 'Triangle Down':
            marker = 'v'
        if marker == 'Triangle Right':
            marker = '>'
        if marker == 'Triangle Left':
            marker = '<'

        linestyle = self.lineComboBox.currentText()
        if linestyle == 'No Line':
            linestyle = 'None'
        if linestyle == 'Line':
            linestyle = '-'
        if linestyle == 'Dashed Line':
            linestyle = '--'
        if linestyle == 'Dotted Line':
            linestyle = ':'

        try:
            if self.data[datakey].df.columns.nlevels == 2:
                vars_level0 = self.data[datakey].df.columns.get_level_values(0)
                vars_level1 = self.data[datakey].df.columns.get_level_values(1)
                vars_level1 = list(vars_level1[vars_level0 != 'wvl'])
                vars_level0 = list(vars_level0[vars_level0 != 'wvl'])
                xvar = (vars_level0[vars_level1.index(xvar)], xvar)
                yvar = (vars_level0[vars_level1.index(yvar)], yvar)
        except AttributeError:  # df attribute doesn't exist.
            pass

        try:
            x = self.data[datakey].df[xvar]
            y = self.data[datakey].df[yvar]
        except:
            x = self.data[datakey]['cv'][xvar]
            y = self.data[datakey]['cv'][yvar]
        loadfig = None
        if not figname in self.figname:
            self.figname.append(figname)
        if figname in self.figs:
            loadfig = self.figs[figname]

        figpath = self.plotFilenameLineEdit.text()
        figpath, figfile = '/'.join(figpath.split('/')[:-1]), figpath.split('/')[-1]
        if self.plotFilenameLineEdit.text() == "" or self.plotFilenameLineEdit.text() == "*.png":
            figpath, figfile = self.outpath, figname
        self.figs[figname] = make_plot(x, y, figpath, figfile, xrange=xrange, yrange=yrange, xtitle=xtitle,
                                       ytitle=ytitle, title=title,
                                       lbl=lbl, one_to_one=one_to_one, dpi=dpi, colorvar=colorvar, colorval=colorval,
                                       annot_mask=annot_mask, cmap=cmap, color = color,
                                       colortitle=colortitle, loadfig=loadfig, marker=marker, linestyle=linestyle)

    def get_data_levels(self):
        self.vars_level0 = self.data[self.chooseDataComboBox.currentText()].df.columns.get_level_values(0)
        self.vars_level1 = self.data[self.chooseDataComboBox.currentText()].df.columns.get_level_values(1)
        self.vars_level1 = self.vars_level1[self.vars_level0 != 'wvl']
        self.vars_level0 = self.vars_level0[self.vars_level0 != 'wvl']
        self.vars_level1 = list(self.vars_level1[self.vars_level0 != 'masked'])
        self.vars_level0 = list(self.vars_level0[self.vars_level0 != 'masked'])
        try:
            unnamed_flag0 = []
            for i in self.vars_level0:
                flag_val = 'Unnamed' not in str(i)
                unnamed_flag0.append(flag_val)
            unnamed_flag1 = []
            for i in self.vars_level1:
                flag_val = 'Unnamed' not in str(i)
                unnamed_flag1.append(flag_val)

            #at some point, need to make this more elegant
            unnamed_flag = np.logical_and(unnamed_flag0, unnamed_flag1).tolist()
            self.vars_level0 = np.array(self.vars_level0)[unnamed_flag].tolist()
            self.vars_level1 = np.array(self.vars_level1)[unnamed_flag].tolist()

        except:
            pass

    def get_choices(self):
        try:
            self.get_data_levels()
            choices = self.vars_level1

        except:
            try:
                choices = self.data[self.chooseDataComboBox.currentText()].columns.values
            except:
                choices = ['No valid choices']
        choices2 = ['None']
        for choice in choices:
            choices2.append(choice)
        choices = choices2
        return choices

    def get_data(self, model):
        model.setStringList(self.figname)

    def get_minmax(self, objmin, objmax, var):
        try:
            self.get_data_levels()
            varind = self.vars_level1.index(var)
            vartuple = (self.vars_level0[varind], self.vars_level1[varind])
            vardata = self.data[self.chooseDataComboBox.currentText()].df[vartuple]
        except:
            try:
                vardata = self.data[self.chooseDataComboBox.currentText()]['cv'][var]
            except:
                vardata = [0, 0]
        try:
            varmin = float(np.min(vardata))
            varmax = float(np.max(vardata))
            objmin.setValue(varmin)
            objmax.setValue(varmax)
        except:
            objmin.setValue(0)
            objmax.setValue(1)

    def plotFilenamePushButton_clicked(self):
        filename, _filter = QtWidgets.QFileDialog.getSaveFileName(None, "Save Plot", self.outpath, "(*.png)")
        self.plotFilenameLineEdit.setText(filename)
        if self.plotFilenameLineEdit.text() == "":
            self.plotFilenameLineEdit.setText("*.png")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()
    ui = Plot()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
