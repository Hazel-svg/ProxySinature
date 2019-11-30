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
        self.buttonBox = QtWidgets.QDialogButtonBox(infonew)
        self.buttonBox.setGeometry(QtCore.QRect(-60, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(infonew)
        self.label.setGeometry(QtCore.QRect(40, 50, 291, 21))
        self.label.setObjectName("label")
        self.InfoNewInput = QtWidgets.QLineEdit(infonew)
        self.InfoNewInput.setGeometry(QtCore.QRect(40, 70, 291, 31))
        self.InfoNewInput.setObjectName("InfoNewInput")

        self.retranslateUi(infonew)
        self.buttonBox.accepted.connect(infonew.accept)
        self.buttonBox.rejected.connect(infonew.reject)
        QtCore.QMetaObject.connectSlotsByName(infonew)

    def retranslateUi(self, infonew):
        _translate = QtCore.QCoreApplication.translate
        infonew.setWindowTitle(_translate("infonew", "Dialog"))
        self.label.setText(_translate("infonew", "请输入您的口令以新建一个属于您的密钥："))

