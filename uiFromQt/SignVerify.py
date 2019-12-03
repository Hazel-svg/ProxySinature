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
        self.btnbox_signverify = QtWidgets.QDialogButtonBox(signverify)
        self.btnbox_signverify.setGeometry(QtCore.QRect(-60, 140, 341, 32))
        self.btnbox_signverify.setOrientation(QtCore.Qt.Horizontal)
        self.btnbox_signverify.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btnbox_signverify.setObjectName("btnbox_signverify")
        self.label_signverify = QtWidgets.QLabel(signverify)
        self.label_signverify.setGeometry(QtCore.QRect(50, 50, 301, 21))
        self.label_signverify.setObjectName("label_signverify")
        self.label_password = QtWidgets.QLabel(signverify)
        self.label_password.setGeometry(QtCore.QRect(10, 80, 41, 21))
        self.label_password.setObjectName("label_password")
        self.input_signverify = QtWidgets.QLineEdit(signverify)
        self.input_signverify.setGeometry(QtCore.QRect(60, 80, 291, 31))
        self.input_signverify.setObjectName("input_signverify")

        self.retranslateUi(signverify)
        self.btnbox_signverify.accepted.connect(signverify.accept)
        self.btnbox_signverify.rejected.connect(signverify.reject)
        QtCore.QMetaObject.connectSlotsByName(signverify)

    def retranslateUi(self, signverify):
        _translate = QtCore.QCoreApplication.translate
        signverify.setWindowTitle(_translate("signverify", "Dialog"))
        self.label_signverify.setText(_translate("signverify", "请在下方输入您生成密钥时的口令以验证身份"))
        self.label_password.setText(_translate("signverify", "口令："))

