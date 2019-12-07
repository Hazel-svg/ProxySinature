from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog
from uiFromQt.InfoNew import Ui_infonew
from uiFromQt.InfoVerify import Ui_infoverify
from uiFromQt.SignVerify import Ui_signverify
from uiFromQt.ProxyCancleVerify import Ui_ProxyCancleVerify
from uiFromQt.ProxyNewVerify import Ui_ProxyNewVerify
import sys, os
from uiFromQt import Proxy
from psig.libPsig import *


class myProxy(Proxy.Ui_infoview):
    def __init__(self,proxy):
        super().setupUi(proxy)
        # 信号连接到指定槽
        self.btn_reset.clicked.connect(self.on_reset_btn_clicked)
        self.btn_createUser.clicked.connect(self.on_new_btn_clicked)
        self.excu_btn.clicked.connect(self.on_excu_btn_clicked)
        self.btn_choosefile.clicked.connect(self.on_btn_choosefile_clicked)
        self.btn_verifyfile.clicked.connect(self.on_btn_verifyfile_clicked)
        self.btn_verifysign.clicked.connect(self.on_verifysign_btn_clicked)
        self.combo_authorizelist.currentIndexChanged.connect(self.on_select_auth)
        self.combo_clientlist.currentIndexChanged.connect(self.on_select_client)
        # self.btn_createfile.clicked.connect(self.on_btn_createfile_clicked)
        # self.newproxy_btn.clicked.connect(self.on_newproxy_btn_clicked)
        # self.cancleauthorize_btn.clicked.connect(self.on_cancleauthorize_btn_clicked)

        self.key = Key()
        self._loadUserList()  # 加载下拉选择框
        self.ShowInfo()

    '''信息页面'''

    def on_reset_btn_clicked(self):  # --------------------重置密钥
        ''' 验证就密钥，重新输入口令生成新秘钥 '''
        Form_verify = QtWidgets.QDialog()
        ui = Ui_infoverify()
        ui.setupUi(Form_verify)
        Form_verify.show()
        Form_verify.exec_()

        oldpasswd = ui.input_infoverify.text().encode()
        if not self.key.VerifyPasswd(oldpasswd):
            MSGBOX("口令错误，验证失败！")
            return
        newPassUi = Ui_infonew()
        wgt = QtWidgets.QDialog()
        newPassUi.setupUi(wgt)
        wgt.show()
        wgt.exec_()
        newpasswd = newPassUi.input_infonew.text().encode()
        self.key.Reset(oldpasswd, newpasswd)

    def on_new_btn_clicked(self):  # ---------------------新建用户
        '''生成一个密钥并在客户端显示相关信息'''
        Form_new = QtWidgets.QDialog()
        ui = Ui_infonew()
        ui.setupUi(Form_new)
        Form_new.show()
        Form_new.exec_()

        # gen key
        passwd = ui.input_infonew.text().encode()  # 口令
        key_d = self.key.GenKey(passwd)

        # 客户端显示信息
        self.text_UUID.setText(key_d['uuid'])
        self.text_infopublickey.setText(key_d['keypub'])
        self.text_workdirectory.setText(os.getcwd())
        self._loadUserList()

    '''签名页面'''

    def on_btn_choosefile_clicked(self):
        '''选择需要签名的原文件'''
        filename = QFileDialog.getOpenFileName()[0]
        curdir = os.getcwd().replace("\\", "/")
        sigdir = f'{curdir}/sig/'
        if not os.path.exists(sigdir):
            os.mkdir(sigdir)
        signame = f'{curdir}/sig/{filename.split("/")[-1]}.psig'
        self.text_choosefile.setText(filename)
        self.text_createfile.setText(signame)

    def on_excu_btn_clicked(self):  # --------------------执行签名验证
        Form_excu = QtWidgets.QDialog()
        ui = Ui_signverify()
        ui.setupUi(Form_excu)
        Form_excu.show()
        Form_excu.exec_()

        self.text_signerUuid_2.setText(self.combo_signer.currentText())
        self.text_agentUuid_2.setText('default agent')
        self.text_time_2.setText(time.asctime())

        try:
            ret = self.key.Signature(self.text_choosefile.text(),
                                     self.text_createfile.text(),
                                     self.combo_signer.currentText())
        except:
            MSGBOX("签名程序执行异常！")
            self.text_signeffective_2.setText("签名异常")
            return
        status = '签名成功' if ret else "签名失败"
        self.text_signeffective_2.setText(status)

    '''验证页面'''

    def on_btn_verifyfile_clicked(self):
        '''选择需要签名的原文件'''
        filename = QFileDialog.getOpenFileName()[0]
        curdir = os.getcwd().replace("\\", "/")
        sigdir = f'{curdir}/sig/'
        if not os.path.exists(sigdir):
            os.mkdir(sigdir)
        signame = f'{curdir}/sig/{filename.split("/")[-1]}.psig'
        self.text_verifyfile.setText(filename)
        self.text_signfile.setText(signame)

    def on_verifysign_btn_clicked(self):
        Form_verifysign = QtWidgets.QDialog()
        ui = Ui_signverify()
        ui.setupUi(Form_verifysign)
        Form_verifysign.show()
        Form_verifysign.exec_()

        self.text_signerUuid.setText(self.combo_signer.currentText())
        self.text_agentUuid.setText('default agent')
        self.text_time.setText(time.asctime())

        try:
            ret = self.key.Verify(self.text_verifyfile.text(),
                                  self.text_signfile.text(), None)
        except:
            MSGBOX("验证程序执行异常！")
            self.text_signeffective.setText("验证异常")
            return
        status = '验证成功' if ret else "验证失败"
        self.text_signeffective.setText(status)

    '''代理页面'''

    def on_newproxy_btn_clicked(self):                                        #-----------------新建代理验证
        Form_newproxy = QtWidgets.QDialog()
        ui = Ui_ProxyNewVerify()
        ui.setupUi(Form_newproxy)
        Form_newproxy.show()
        Form_newproxy.exec_()

    def on_select_auth(self):
        self.text_uuid.setText(self.combo_authorizelist.currentText())
       # self.text_proxypublickey

    def on_select_client(self):
        self.text_uuid.setText(self.combo_clientlist.currentText())

    def on_cancleauthorize_btn_clicked(self):                                     #---------------------撤销授权验证
        Form_cancleauthorize= QtWidgets.QDialog()
        ui = Ui_ProxyCancleVerify()
        ui.setupUi(Form_cancleauthorize)
        Form_cancleauthorize.show()
        Form_cancleauthorize.exec_()

    def _loadUserList(self):
        t = ReadKey()
        if not t:
            key = Key()
        else:
            key = Key(uuid=None, key=t)
        users = ClientList(key)
        users = list(users.user.keys())
        self.combo_authorizelist.clear()
        self.combo_clientlist.clear()
        self.combo_signer.clear()
        # users = ["111", '222']
        for i in range(len(users)):
            self.combo_signer.insertItem(i, users[i])
            self.combo_authorizelist.insertItem(i, users[i])
            self.combo_clientlist.insertItem(i, users[i])

    def ShowInfo(self):
        # 客户端显示信息
        key_d = ReadKey()
        self.text_UUID.setText(key_d['uuid'])
        self.text_infopublickey.setText(key_d['keypub'])
        self.text_version.setText("v1.2.0")
        self.text_author.setText("Huiyu Zhou, Peidong Jiang, Yijie Tu")
        self.text_workdirectory.setText(os.getcwd())


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
