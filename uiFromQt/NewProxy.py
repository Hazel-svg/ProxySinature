# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewProxy.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewProxy(object):
    def setupUi(self, NewProxy):
        NewProxy.setObjectName("NewProxy")
        NewProxy.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewProxy)
        self.buttonBox.setGeometry(QtCore.QRect(-60, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_newproxy = QtWidgets.QLabel(NewProxy)
        self.label_newproxy.setGeometry(QtCore.QRect(60, 60, 301, 21))
        self.label_newproxy.setObjectName("label_newproxy")
        self.label_newproxyuuid = QtWidgets.QLabel(NewProxy)
        self.label_newproxyuuid.setGeometry(QtCore.QRect(20, 90, 41, 21))
        self.label_newproxyuuid.setObjectName("label_newproxyuuid")
        self.input_newproxy = QtWidgets.QLineEdit(NewProxy)
        self.input_newproxy.setGeometry(QtCore.QRect(60, 80, 291, 31))
        self.input_newproxy.setObjectName("input_newproxy")

        self.retranslateUi(NewProxy)
        self.buttonBox.accepted.connect(NewProxy.accept)
        self.buttonBox.rejected.connect(NewProxy.reject)
        QtCore.QMetaObject.connectSlotsByName(NewProxy)

    def retranslateUi(self, NewProxy):
        _translate = QtCore.QCoreApplication.translate
        NewProxy.setWindowTitle(_translate("NewProxy", "Dialog"))
        self.label_newproxy.setText(_translate("NewProxy", "输入新建代理的uuid"))
        self.label_newproxyuuid.setText(_translate("NewProxy", "uuid:"))
