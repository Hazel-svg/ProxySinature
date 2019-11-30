from PyQt5 import QtCore, QtGui, QtWidgets
import SignVerify
class mySignVerify(SignVerify.Ui_signverify):
    def __init__(self, signverify):
        super().setupUi(signverify)