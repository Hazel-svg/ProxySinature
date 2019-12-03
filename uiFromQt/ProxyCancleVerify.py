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
        self.btn_proxycancleverify = QtWidgets.QDialogButtonBox(ProxyCancleVerify)
        self.btn_proxycancleverify.setGeometry(QtCore.QRect(-50, 150, 341, 32))
        self.btn_proxycancleverify.setOrientation(QtCore.Qt.Horizontal)
        self.btn_proxycancleverify.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn_proxycancleverify.setObjectName("btn_proxycancleverify")
        self.label_proxycancleverify = QtWidgets.QLabel(ProxyCancleVerify)
        self.label_proxycancleverify.setGeometry(QtCore.QRect(50, 60, 301, 21))
        self.label_proxycancleverify.setObjectName("label_proxycancleverify")
        self.label_password = QtWidgets.QLabel(ProxyCancleVerify)
        self.label_password.setGeometry(QtCore.QRect(10, 90, 41, 21))
        self.label_password.setObjectName("label_password")
        self.input_proxycancleverify = QtWidgets.QLineEdit(ProxyCancleVerify)
        self.input_proxycancleverify.setGeometry(QtCore.QRect(50, 90, 291, 31))
        self.input_proxycancleverify.setObjectName("input_proxycancleverify")

        self.retranslateUi(ProxyCancleVerify)
        self.btn_proxycancleverify.accepted.connect(ProxyCancleVerify.accept)
        self.btn_proxycancleverify.rejected.connect(ProxyCancleVerify.reject)
        QtCore.QMetaObject.connectSlotsByName(ProxyCancleVerify)

    def retranslateUi(self, ProxyCancleVerify):
        _translate = QtCore.QCoreApplication.translate
        ProxyCancleVerify.setWindowTitle(_translate("ProxyCancleVerify", "Dialog"))
        self.label_proxycancleverify.setText(_translate("ProxyCancleVerify", "新建代理需要口令以验证身份"))
        self.label_password.setText(_translate("ProxyCancleVerify", "口令："))

