# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProxyNewVerify.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProxyNewVerify(object):
    def setupUi(self, ProxyNewVerify):
        ProxyNewVerify.setObjectName("ProxyNewVerify")
        ProxyNewVerify.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(ProxyNewVerify)
        self.buttonBox.setGeometry(QtCore.QRect(-40, 160, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(ProxyNewVerify)
        self.label.setGeometry(QtCore.QRect(60, 60, 301, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ProxyNewVerify)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 41, 21))
        self.label_2.setObjectName("label_2")
        self.SignVerifyInput = QtWidgets.QLineEdit(ProxyNewVerify)
        self.SignVerifyInput.setGeometry(QtCore.QRect(60, 90, 291, 31))
        self.SignVerifyInput.setObjectName("SignVerifyInput")

        self.retranslateUi(ProxyNewVerify)
        self.buttonBox.accepted.connect(ProxyNewVerify.accept)
        self.buttonBox.rejected.connect(ProxyNewVerify.reject)
        QtCore.QMetaObject.connectSlotsByName(ProxyNewVerify)

    def retranslateUi(self, ProxyNewVerify):
        _translate = QtCore.QCoreApplication.translate
        ProxyNewVerify.setWindowTitle(_translate("ProxyNewVerify", "Dialog"))
        self.label.setText(_translate("ProxyNewVerify", "新建代理需要口令以验证身份"))
        self.label_2.setText(_translate("ProxyNewVerify", "口令："))

