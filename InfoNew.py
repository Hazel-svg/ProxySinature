# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InfoNew.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_infonew(object):
    def setupUi(self, infonew):
        infonew.setObjectName("infonew")
        infonew.resize(368, 268)
        self.btnbox_infonew = QtWidgets.QDialogButtonBox(infonew)
        self.btnbox_infonew.setGeometry(QtCore.QRect(-60, 140, 341, 32))
        self.btnbox_infonew.setOrientation(QtCore.Qt.Horizontal)
        self.btnbox_infonew.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btnbox_infonew.setObjectName("btnbox_infonew")
        self.label_infonew = QtWidgets.QLabel(infonew)
        self.label_infonew.setGeometry(QtCore.QRect(40, 50, 291, 21))
        self.label_infonew.setObjectName("label_infonew")
        self.input_infonew = QtWidgets.QLineEdit(infonew)
        self.input_infonew.setGeometry(QtCore.QRect(40, 70, 291, 31))
        self.input_infonew.setObjectName("input_infonew")

        self.retranslateUi(infonew)
        self.btnbox_infonew.accepted.connect(infonew.accept)
        self.btnbox_infonew.rejected.connect(infonew.reject)
        QtCore.QMetaObject.connectSlotsByName(infonew)

    def retranslateUi(self, infonew):
        _translate = QtCore.QCoreApplication.translate
        infonew.setWindowTitle(_translate("infonew", "Dialog"))
        self.label_infonew.setText(_translate("infonew", "请输入您的口令以新建一个属于您的密钥："))

