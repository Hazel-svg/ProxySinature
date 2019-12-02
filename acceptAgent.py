# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acceptAgent.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.btn_acceptagent = QtWidgets.QDialogButtonBox(Dialog)
        self.btn_acceptagent.setGeometry(QtCore.QRect(-50, 140, 341, 32))
        self.btn_acceptagent.setOrientation(QtCore.Qt.Horizontal)
        self.btn_acceptagent.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn_acceptagent.setObjectName("btn_acceptagent")
        self.label_uuid = QtWidgets.QLabel(Dialog)
        self.label_uuid.setGeometry(QtCore.QRect(70, 60, 51, 21))
        self.label_uuid.setObjectName("label_uuid")
        self.text_uuid = QtWidgets.QTextBrowser(Dialog)
        self.text_uuid.setGeometry(QtCore.QRect(110, 50, 211, 31))
        self.text_uuid.setObjectName("text_uuid")
        self.label_askagent = QtWidgets.QLabel(Dialog)
        self.label_askagent.setGeometry(QtCore.QRect(70, 90, 251, 16))
        self.label_askagent.setObjectName("label_askagent")

        self.retranslateUi(Dialog)
        self.btn_acceptagent.accepted.connect(Dialog.accept)
        self.btn_acceptagent.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_uuid.setText(_translate("Dialog", "uuid:"))
        self.label_askagent.setText(_translate("Dialog", "请求代理，请问是否同意"))

