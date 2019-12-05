from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog
from uiFromQt.InfoNew import Ui_infonew
from uiFromQt.InfoVerify import Ui_infoverify
from uiFromQt.SignVerify import Ui_signverify
from uiFromQt.ProxyCancleVerify import Ui_ProxyCancleVerify
from uiFromQt.ProxyNewVerify import Ui_ProxyNewVerify
import sys, os
from uiFromQt import Proxy
from psig.libKey import GenKey
from psig.libPsig import version


class myProxy(Proxy.Ui_infoview):
    def __init__(self,proxy):
        super().setupUi(proxy)
        # 信号连接到指定槽
        self.btn_reset.clicked.connect(self.on_reset_btn_clicked)
        self.btn_createUser.clicked.connect(self.on_new_btn_clicked)
        self.excu_btn.clicked.connect(self.on_excu_btn_clicked)
        self.btn_choosefile.clicked.connect(self.on_btn_choosefile_clicked)
        # self.btn_createfile.clicked.connect(self.on_btn_createfile_clicked)
        # self.newproxy_btn.clicked.connect(self.on_newproxy_btn_clicked)
        # self.cancleauthorize_btn.clicked.connect(self.on_cancleauthorize_btn_clicked)

        self._loadUserList()  # 加载下拉选择框


    def on_btn_choosefile_clicked(self):
        '''选择需要签名的原文件'''
        filename = QFileDialog.getOpenFileName()[0]
        curdir = os.getcwd().replace("\\", "/")
        signame = f'{curdir}/{filename.split("/")[-1]}.psig'
        self.text_choosefile.setText(filename)
        self.text_createfile.setText(signame)

        # TODO: Signature(filename,signame,ouuid)


    def on_reset_btn_clicked(self):                                         #--------------------重置密钥
        ''' 验证就密钥，重新输入口令生成新秘钥 '''
        Form_verify = QtWidgets.QDialog()
        ui = Ui_infoverify()
        ui.setupUi(Form_verify)
        Form_verify.show()
        Form_verify.exec_()

        old_passwd = ui.input_infoverify.text().encode()
        newPassUi = Ui_infonew()
        wgt = QtWidgets.QDialog()
        newPassUi.setupUi(wgt)
        wgt.show()
        wgt.exec_()
        new_passwd = newPassUi.input_infonew.text().encode()
        # TODO: ResetKey(oldPasswd, newPasswd)

    def on_new_btn_clicked(self):                                            #---------------------新建用户
        '''生成一个密钥并在客户端显示相关信息'''
        Form_new = QtWidgets.QDialog()
        ui = Ui_infonew()
        ui.setupUi(Form_new)
        Form_new.show()
        Form_new.exec_()

        # gen key
        passwd = ui.input_infonew.text().encode()  # 口令
        key_d = GenKey(passwd)

        # 客户端显示信息
        self.text_UUID.setText(key_d['uuid'])
        self.text_infopublickey.setText(key_d['keypub'])
        self.text_version.setText(version)
        self.text_author.setText("Huiyu Zhou, ***, ***")


    def on_excu_btn_clicked(self):                                            #--------------------执行签名验证
        Form_excu = QtWidgets.QDialog()
        ui = Ui_signverify()
        ui.setupUi(Form_excu)
        Form_excu.show()
        Form_excu.exec_()

        verifyfile = QFileDialog.getOpenFileName()[0]
        signfile = QFileDialog.getOpenFileName()[0]

        # TODO:
        # ret = Verify(filename,signame)
        # if not ret:
        #     MSGBOX("签名验证失败！")
        # else:
        #     MSGBOX("验证成功!")
        #     # 显示相关信息


    def on_newproxy_btn_clicked(self):                                        #-----------------新建代理验证
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

    def _loadUserList(self):
        # TODO users = GetUserList()
        users = ["111", '222']
        for i in range(len(users)):
            self.combo_signer.insertItem(i, users[i])
            self.combo_authorizelist.insertItem(i, users[i])
            self.combo_clientlist.insertItem(i, users[i])

def MSGBOX(msg: str):
    "弹出异常消息提示框"
    msgb = QtWidgets.QMessageBox()
    msgb.setText(msg)
    msgb.show()
    msgb.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QtWidgets.QTabWidget()
    window = myProxy(Form)
    # window.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
