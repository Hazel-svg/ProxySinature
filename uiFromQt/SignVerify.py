# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignVerify.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_signverify(object):
    def setupUi(self, signverify):
        signverify.setObjectName("signverify")
        signverify.resize(400, 300)
        self.btnbox_signverify = QtWidgets.QDialogButtonBox(signverify)
        self.btnbox_signverify.setGeometry(QtCore.QRect(-60, 170, 341, 32))
        self.btnbox_signverify.setOrientation(QtCore.Qt.Horizontal)
        self.btnbox_signverify.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btnbox_signverify.setObjectName("btnbox_signverify")
        self.label_signverify = QtWidgets.QLabel(signverify)
        self.label_signverify.setGeometry(QtCore.QRect(10, 50, 81, 21))
        self.label_signverify.setObjectName("label_signverify")
        self.input_signverify = QtWidgets.QLineEdit(signverify)
        self.input_signverify.setGeometry(QtCore.QRect(120, 80, 261, 31))
        self.input_signverify.setObjectName("input_signverify")
        self.text_clientuuid = QtWidgets.QTextBrowser(signverify)
        self.text_clientuuid.setGeometry(QtCore.QRect(90, 40, 301, 31))
        self.text_clientuuid.setObjectName("text_clientuuid")
        self.label_signverify_2 = QtWidgets.QLabel(signverify)
        self.label_signverify_2.setGeometry(QtCore.QRect(10, 90, 111, 21))
        self.label_signverify_2.setObjectName("label_signverify_2")

        self.retranslateUi(signverify)
        self.btnbox_signverify.accepted.connect(signverify.accept)
        self.btnbox_signverify.rejected.connect(signverify.reject)
        QtCore.QMetaObject.connectSlotsByName(signverify)

    def retranslateUi(self, signverify):
        _translate = QtCore.QCoreApplication.translate
        signverify.setWindowTitle(_translate("signverify", "Dialog"))
        self.label_signverify.setText(_translate("signverify", "请输入客户"))
        self.label_signverify_2.setText(_translate("signverify", "的代理密钥口令"))
