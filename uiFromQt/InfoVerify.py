# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InfoVerify.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_infoverify(object):
    def setupUi(self, infoverify):
        infoverify.setObjectName("infoverify")
        infoverify.resize(400, 300)
        self.btnbox_infoverify = QtWidgets.QDialogButtonBox(infoverify)
        self.btnbox_infoverify.setGeometry(QtCore.QRect(-50, 240, 341, 32))
        self.btnbox_infoverify.setOrientation(QtCore.Qt.Horizontal)
        self.btnbox_infoverify.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btnbox_infoverify.setObjectName("btnbox_infoverify")
        self.label_infoverify = QtWidgets.QLabel(infoverify)
        self.label_infoverify.setGeometry(QtCore.QRect(40, 40, 301, 21))
        self.label_infoverify.setObjectName("label_infoverify")
        self.input_infoverify = QtWidgets.QLineEdit(infoverify)
        self.input_infoverify.setGeometry(QtCore.QRect(70, 70, 271, 31))
        self.input_infoverify.setObjectName("input_infoverify")
        self.label_password = QtWidgets.QLabel(infoverify)
        self.label_password.setGeometry(QtCore.QRect(10, 80, 61, 20))
        self.label_password.setObjectName("label_password")
        self.label_password_2 = QtWidgets.QLabel(infoverify)
        self.label_password_2.setGeometry(QtCore.QRect(10, 130, 61, 20))
        self.label_password_2.setObjectName("label_password_2")
        self.input_infoverify_2 = QtWidgets.QLineEdit(infoverify)
        self.input_infoverify_2.setGeometry(QtCore.QRect(70, 130, 271, 31))
        self.input_infoverify_2.setObjectName("input_infoverify_2")

        self.retranslateUi(infoverify)
        self.btnbox_infoverify.accepted.connect(infoverify.accept)
        self.btnbox_infoverify.rejected.connect(infoverify.reject)
        QtCore.QMetaObject.connectSlotsByName(infoverify)

    def retranslateUi(self, infoverify):
        _translate = QtCore.QCoreApplication.translate
        infoverify.setWindowTitle(_translate("infoverify", "Dialog"))
        self.label_infoverify.setText(_translate("infoverify", "请在下方输入您生成密钥时的口令以验证身份"))
        self.label_password.setText(_translate("infoverify", "原口令："))
        self.label_password_2.setText(_translate("infoverify", "新口令："))
