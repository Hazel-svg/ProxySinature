# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProxyCancleVerify.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProxyCancleVerify(object):
    def setupUi(self, ProxyCancleVerify):
        ProxyCancleVerify.setObjectName("ProxyCancleVerify")
        ProxyCancleVerify.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(ProxyCancleVerify)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(ProxyCancleVerify)
        self.label.setGeometry(QtCore.QRect(50, 60, 301, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ProxyCancleVerify)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 41, 21))
        self.label_2.setObjectName("label_2")
        self.SignVerifyInput = QtWidgets.QLineEdit(ProxyCancleVerify)
        self.SignVerifyInput.setGeometry(QtCore.QRect(50, 90, 291, 31))
        self.SignVerifyInput.setObjectName("SignVerifyInput")

        self.retranslateUi(ProxyCancleVerify)
        self.buttonBox.accepted.connect(ProxyCancleVerify.accept)
        self.buttonBox.rejected.connect(ProxyCancleVerify.reject)
        QtCore.QMetaObject.connectSlotsByName(ProxyCancleVerify)

    def retranslateUi(self, ProxyCancleVerify):
        _translate = QtCore.QCoreApplication.translate
        ProxyCancleVerify.setWindowTitle(_translate("ProxyCancleVerify", "Dialog"))
        self.label.setText(_translate("ProxyCancleVerify", "新建代理需要口令以验证身份"))
        self.label_2.setText(_translate("ProxyCancleVerify", "口令："))

