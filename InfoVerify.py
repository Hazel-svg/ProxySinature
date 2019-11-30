# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InfoVerify.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_infoverify(object):
    def setupUi(self, infoverify):
        infoverify.setObjectName("infoverify")
        infoverify.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(infoverify)
        self.buttonBox.setGeometry(QtCore.QRect(-60, 150, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(infoverify)
        self.label.setGeometry(QtCore.QRect(40, 40, 301, 21))
        self.label.setObjectName("label")
        self.InfoVerifyInput = QtWidgets.QLineEdit(infoverify)
        self.InfoVerifyInput.setGeometry(QtCore.QRect(70, 70, 271, 31))
        self.InfoVerifyInput.setObjectName("InfoVerifyInput")
        self.label_2 = QtWidgets.QLabel(infoverify)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 61, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(infoverify)
        self.buttonBox.accepted.connect(infoverify.accept)
        self.buttonBox.rejected.connect(infoverify.reject)
        QtCore.QMetaObject.connectSlotsByName(infoverify)

    def retranslateUi(self, infoverify):
        _translate = QtCore.QCoreApplication.translate
        infoverify.setWindowTitle(_translate("infoverify", "Dialog"))
        self.label.setText(_translate("infoverify", "请在下方输入您生成密钥时的口令以验证身份"))
        self.label_2.setText(_translate("infoverify", "原口令："))

