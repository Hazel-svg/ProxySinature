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
        self.btn_proxynewverify = QtWidgets.QDialogButtonBox(ProxyNewVerify)
        self.btn_proxynewverify.setGeometry(QtCore.QRect(-40, 160, 341, 32))
        self.btn_proxynewverify.setOrientation(QtCore.Qt.Horizontal)
        self.btn_proxynewverify.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn_proxynewverify.setObjectName("btn_proxynewverify")
        self.label_proxynewverify = QtWidgets.QLabel(ProxyNewVerify)
        self.label_proxynewverify.setGeometry(QtCore.QRect(60, 60, 301, 21))
        self.label_proxynewverify.setObjectName("label_proxynewverify")
        self.label_password = QtWidgets.QLabel(ProxyNewVerify)
        self.label_password.setGeometry(QtCore.QRect(10, 90, 41, 21))
        self.label_password.setObjectName("label_password")
        self.input_proxynewverify = QtWidgets.QLineEdit(ProxyNewVerify)
        self.input_proxynewverify.setGeometry(QtCore.QRect(60, 90, 291, 31))
        self.input_proxynewverify.setObjectName("input_proxynewverify")

        self.retranslateUi(ProxyNewVerify)
        self.btn_proxynewverify.accepted.connect(ProxyNewVerify.accept)
        self.btn_proxynewverify.rejected.connect(ProxyNewVerify.reject)
        QtCore.QMetaObject.connectSlotsByName(ProxyNewVerify)

    def retranslateUi(self, ProxyNewVerify):
        _translate = QtCore.QCoreApplication.translate
        ProxyNewVerify.setWindowTitle(_translate("ProxyNewVerify", "Dialog"))
        self.label_proxynewverify.setText(_translate("ProxyNewVerify", "新建代理需要口令以验证身份"))
        self.label_password.setText(_translate("ProxyNewVerify", "口令："))

