from PyQt5 import QtCore, QtGui, QtWidgets
import ProxyNewVerify
class myProxyNewVerify(ProxyNewVerify.Ui_ProxyNewVerify):
    def __init__(self,ProxyNewVerify):
        super().setupUi(ProxyNewVerify)