# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pbarReport.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_pbarReport(object):
    def setupUi(self, pbarReport):
        pbarReport.setObjectName("pbarReport")
        pbarReport.resize(223, 125)
        pbarReport.setStyleSheet("QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: none;\n"
"    outline: none;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"QLabel\n"
"{\n"
"    font-size: 12px;\n"
"    font-weight: bold;    \n"
"}\n"
"QPushButton\n"
"{\n"
"    color: #d7801a;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}")
        self.pbarLoading = QtWidgets.QProgressBar(pbarReport)
        self.pbarLoading.setGeometry(QtCore.QRect(10, 50, 201, 23))
        self.pbarLoading.setStyleSheet("")
        self.pbarLoading.setProperty("value", 0)
        self.pbarLoading.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.pbarLoading.setTextVisible(True)
        self.pbarLoading.setOrientation(QtCore.Qt.Horizontal)
        self.pbarLoading.setInvertedAppearance(False)
        self.pbarLoading.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.pbarLoading.setObjectName("pbarLoading")
        self.lblLoading = QtWidgets.QLabel(pbarReport)
        self.lblLoading.setGeometry(QtCore.QRect(20, 10, 121, 16))
        self.lblLoading.setObjectName("lblLoading")
        self.btnCancel = QtWidgets.QPushButton(pbarReport)
        self.btnCancel.setGeometry(QtCore.QRect(130, 90, 75, 23))
        self.btnCancel.setObjectName("btnCancel")

        self.retranslateUi(pbarReport)
        QtCore.QMetaObject.connectSlotsByName(pbarReport)

    def retranslateUi(self, pbarReport):
        _translate = QtCore.QCoreApplication.translate
        pbarReport.setWindowTitle(_translate("pbarReport", "Loading Report"))
        self.lblLoading.setText(_translate("pbarReport", "Loading Report"))
        self.btnCancel.setText(_translate("pbarReport", "Cancel"))

import resources_rc
