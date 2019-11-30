from PyQt5 import QtCore, QtGui, QtWidgets
import ProxyCancleVerify
class myProxyCancleVerify(ProxyCancleVerify.Ui_ProxyCancleVerify):
    def __init__(self,ProxyCancleVerify):
        super().setupUi(ProxyCancleVerify)