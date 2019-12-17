# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewProxyPasswd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewProxyPasswd(object):
    def setupUi(self, NewProxyPasswd):
        NewProxyPasswd.setObjectName("NewProxyPasswd")
        NewProxyPasswd.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewProxyPasswd)
        self.buttonBox.setGeometry(QtCore.QRect(-50, 160, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.lable_newproxypasswd = QtWidgets.QLabel(NewProxyPasswd)
        self.lable_newproxypasswd.setGeometry(QtCore.QRect(70, 60, 301, 21))
        self.lable_newproxypasswd.setObjectName("lable_newproxypasswd")
        self.label_password = QtWidgets.QLabel(NewProxyPasswd)
        self.label_password.setGeometry(QtCore.QRect(20, 100, 41, 21))
        self.label_password.setObjectName("label_password")
        self.input_newproxypasswd = QtWidgets.QLineEdit(NewProxyPasswd)
        self.input_newproxypasswd.setGeometry(QtCore.QRect(60, 90, 291, 31))
        self.input_newproxypasswd.setObjectName("input_newproxypasswd")

        self.retranslateUi(NewProxyPasswd)
        self.buttonBox.accepted.connect(NewProxyPasswd.accept)
        self.buttonBox.rejected.connect(NewProxyPasswd.reject)
        QtCore.QMetaObject.connectSlotsByName(NewProxyPasswd)

    def retranslateUi(self, NewProxyPasswd):
        _translate = QtCore.QCoreApplication.translate
        NewProxyPasswd.setWindowTitle(_translate("NewProxyPasswd", "Dialog"))
        self.lable_newproxypasswd.setText(_translate("NewProxyPasswd", "请为新建的代理输入新的口令"))
        self.label_password.setText(_translate("NewProxyPasswd", "口令："))
