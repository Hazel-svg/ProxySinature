# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acceptAgent.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AcceptAgent(object):
    def setupUi(self, AcceptAgent):
        AcceptAgent.setObjectName("AcceptAgent")
        AcceptAgent.resize(400, 300)
        self.btn_acceptagent = QtWidgets.QDialogButtonBox(AcceptAgent)
        self.btn_acceptagent.setGeometry(QtCore.QRect(-50, 140, 341, 32))
        self.btn_acceptagent.setOrientation(QtCore.Qt.Horizontal)
        self.btn_acceptagent.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btn_acceptagent.setObjectName("btn_acceptagent")
        self.label_accagentuuid = QtWidgets.QLabel(AcceptAgent)
        self.label_accagentuuid.setGeometry(QtCore.QRect(70, 60, 51, 21))
        self.label_accagentuuid.setObjectName("label_accagentuuid")
        self.text_accagentuuid = QtWidgets.QTextBrowser(AcceptAgent)
        self.text_accagentuuid.setGeometry(QtCore.QRect(110, 50, 211, 31))
        self.text_accagentuuid.setObjectName("text_accagentuuid")
        self.label_askagent = QtWidgets.QLabel(AcceptAgent)
        self.label_askagent.setGeometry(QtCore.QRect(70, 90, 251, 16))
        self.label_askagent.setObjectName("label_askagent")

        self.retranslateUi(AcceptAgent)
        self.btn_acceptagent.accepted.connect(AcceptAgent.accept)
        self.btn_acceptagent.rejected.connect(AcceptAgent.reject)
        QtCore.QMetaObject.connectSlotsByName(AcceptAgent)

    def retranslateUi(self, AcceptAgent):
        _translate = QtCore.QCoreApplication.translate
        AcceptAgent.setWindowTitle(_translate("AcceptAgent", "Dialog"))
        self.label_accagentuuid.setText(_translate("AcceptAgent", "uuid:"))
        self.label_askagent.setText(_translate("AcceptAgent", "请求代理，请问是否同意"))
