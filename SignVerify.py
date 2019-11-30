# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignVerify.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_signverify(object):
    def setupUi(self, signverify):
        signverify.setObjectName("signverify")
        signverify.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(signverify)
        self.buttonBox.setGeometry(QtCore.QRect(-60, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(signverify)
        self.label.setGeometry(QtCore.QRect(50, 50, 301, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(signverify)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 41, 21))
        self.label_2.setObjectName("label_2")
        self.SignVerifyInput = QtWidgets.QLineEdit(signverify)
        self.SignVerifyInput.setGeometry(QtCore.QRect(60, 80, 291, 31))
        self.SignVerifyInput.setObjectName("SignVerifyInput")

        self.retranslateUi(signverify)
        self.buttonBox.accepted.connect(signverify.accept)
        self.buttonBox.rejected.connect(signverify.reject)
        QtCore.QMetaObject.connectSlotsByName(signverify)

    def retranslateUi(self, signverify):
        _translate = QtCore.QCoreApplication.translate
        signverify.setWindowTitle(_translate("signverify", "Dialog"))
        self.label.setText(_translate("signverify", "请在下方输入您生成密钥时的口令以验证身份"))
        self.label_2.setText(_translate("signverify", "口令："))

