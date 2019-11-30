from PyQt5 import QtCore, QtGui, QtWidgets
import InfoVerify
class myinfoVerify(InfoVerify.Ui_infoverify):
    def __init__(self,infoverify):
        super().setupUi(infoverify)