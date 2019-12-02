from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from InfoNew import Ui_infonew
from InfoVerify import Ui_infoverify
from SignVerify import Ui_signverify
from ProxyCancleVerify import Ui_ProxyCancleVerify
from ProxyNewVerify import Ui_ProxyNewVerify
import Proxy, sys
class myProxy(Proxy.Ui_infoview):
    def __init__(self,proxy):
        super().setupUi(proxy)
        # 信号连接到指定槽
        self.btn_reset.clicked.connect(self.on_reset_btn_clicked)
        self.btn_createUser.clicked.connect(self.on_new_btn_clicked)
        self.excu_btn.clicked.connect(self.on_excu_btn_clicked)
        # self.newproxy_btn.clicked.connect(self.on_newproxy_btn_clicked)
        # self.cancleauthorize_btn.clicked.connect(self.on_cancleauthorize_btn_clicked)

    def on_reset_btn_clicked(self):                                          #--------------------重置密钥
        Form_verify = QtWidgets.QDialog()
        ui = Ui_infoverify()
        ui.setupUi(Form_verify)
        Form_verify.show()
        Form_verify.exec_()

    def on_new_btn_clicked(self):                                            #---------------------新建用户
        Form_new = QtWidgets.QDialog()
        ui = Ui_infonew()
        ui.setupUi(Form_new)
        Form_new.show()
        Form_new.exec_()

    def on_excu_btn_clicked(self):                                            #--------------------执行签名验证
        Form_excu = QtWidgets.QDialog()
        ui = Ui_signverify()
        ui.setupUi(Form_excu)
        Form_excu.show()
        Form_excu.exec_()

    def on_newproxy_btn_clicked(self):                                            #-----------------新建代理验证
        Form_newproxy = QtWidgets.QDialog()
        ui = Ui_ProxyNewVerify()
        ui.setupUi(Form_newproxy)
        Form_newproxy.show()
        Form_newproxy.exec_()

    def on_cancleauthorize_btn_clicked(self):                                     #---------------------撤销授权验证
        Form_cancleauthorize= QtWidgets.QDialog()
        ui = Ui_ProxyCancleVerify()
        ui.setupUi(Form_cancleauthorize)
        Form_cancleauthorize.show()
        Form_cancleauthorize.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QtWidgets.QTabWidget()
    window = myProxy(Form)
    # window.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())