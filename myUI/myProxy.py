from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog

from myUI.myAcceptAgent import MyAcceptAgent
from uiFromQt.InfoNew import Ui_infonew
from uiFromQt.InfoVerify import Ui_infoverify
from uiFromQt.SignVerify import Ui_signverify
from uiFromQt.ProxyCancleVerify import Ui_ProxyCancleVerify
from uiFromQt.ProxyNewVerify import Ui_ProxyNewVerify
from uiFromQt.NewProxy import Ui_NewProxy
from uiFromQt.acceptAgent import Ui_AcceptAgent
from uiFromQt.NewProxyPasswd import Ui_NewProxyPasswd
from PyQt5.QtCore import QThread,pyqtSignal
import  time
import sys
import PyQt5.QtWidgets as PQW
import PyQt5.QtCore as PQC
import sys, os
from uiFromQt import Proxy
from psig.libPsig import *

class myProxy(Proxy.Ui_infoview):
    def __init__(self, proxy):
        super().setupUi(proxy)
        # 信号连接到指定槽
        self.btn_reset.clicked.connect(self.on_reset_btn_clicked)
        #self.btn_createUser.clicked.connect(self.on_new_btn_clicked)
        self.excu_btn.clicked.connect(self.on_excu_btn_clicked)
        self.btn_choosefile.clicked.connect(self.on_btn_choosefile_clicked)
        self.btn_verifyfile.clicked.connect(self.on_btn_verifyfile_clicked)
        self.btn_verifysign.clicked.connect(self.on_verifysign_btn_clicked)
        self.combo_authorizelist.currentIndexChanged.connect(self.on_select_auth)
        self.combo_clientlist.currentIndexChanged.connect(self.on_select_client)
        self.signfile_btn.clicked.connect(self.on_btn_signfile_clicked)
        self.btn_newproxy.clicked.connect(self.on_newproxy_btn_clicked)
        self.btn_cancleauthorize.clicked.connect(self.on_cancleauthorize_btn_clicked)

        t=ReadKey()
        if not t:
            # input
            Form_new = QtWidgets.QDialog()
            ui = Ui_infonew()
            ui.setupUi(Form_new)
            Form_new.show()
            Form_new.exec_()

            # gen key
            passwd = ui.input_infonew.text().encode()  # 口令
            self.key = Key(passwd=passwd)
            self.key.GenKey(passwd)
            self.text_UUID.setText(self.key.key['uuid'])
            self.text_infopublickey.setText(self.key.key['keypub'])
            self.text_workdirectory.setText(os.getcwd())
            self._loadUserList()

        else:
            self.key=Key(key=t)
        del t
        self.cl = ClientList(self.key)
        self.al = AgentList(self.key)

        self._loadUserList()  # 加载下拉选择框
        self.sock = Sock()
        self.sock.new_msg.connect(self._recieve_new_msg)
        self.ShowInfo()

    def __del__(self):
        self.sock.clear()
        print("exit")

    '''信息页面'''

    def on_reset_btn_clicked(self):  # --------------------重置密钥
        ''' 验证旧密钥，重新输入口令生成新密钥 '''
        Form_verify = QtWidgets.QDialog()
        ui = Ui_infoverify()
        ui.setupUi(Form_verify)
        Form_verify.show()
        Form_verify.exec_()

        oldpasswd = ui.input_infoverify.text().encode()
        newpasswd = ui.input_infoverify_2.text().encode()

        ret =  self.key.Reset(oldpasswd, newpasswd)
        if ret == False:
            MSGBOX("口令错误，验证失败！")
            return
        else:
            self.sock.NewUser()
            self.cl.AddUser(self.key.key['uuid'],self.key.key)
            self.al.AddUser(self.key.key['uuid'],{'uuid':self.key.key['uuid'],'keypub':self.key.key['keypub']})
            self.text_UUID.setText(self.key.key['uuid'])
            self.text_infopublickey.setText(self.key.key['keypub'])
            self._loadUserList()


    def on_btn_choosefile_clicked(self):
        '''选择需要签名的原文件'''
        filename = QFileDialog.getOpenFileName()[0]
        '''
        curdir = os.getcwd().replace("\\", "/")
        sigdir = f'{curdir}/'
        if not os.path.exists(sigdir):
            os.mkdir(sigdir)
        signame = f'{curdir}/{filename.split("/")[-1]}.psig'
        '''
        signame = filename+'.psig'
        self.text_choosefile.setText(filename)
        self.text_createfile.setText(signame)


    def on_excu_btn_clicked(self):  # --------------------执行签名验证
        Form_excu = QtWidgets.QDialog()
        ui = Ui_signverify()
        ui.setupUi(Form_excu)
        Form_excu.show()
        Form_excu.exec_()

        passwd = ui.input_signverify.text().encode()

        ret =  self.key.Dekey(passwd)
        if ret == None:
            MSGBOX("口令错误，验证失败！")
            return
        
        self.text_signerUuid_2.setText(self.combo_signer.currentText())
        self.text_agentUuid_2.setText(self.key.key['uuid'])
        self.text_time_2.setText(time.asctime())

        try:
            ret = self.key.Signature(self.text_choosefile.toPlainText(),
                                     self.text_createfile.toPlainText(),
                                     self.combo_signer.currentText(),
                                     self.cl,
                                     ui.input_signverify.text().encode())
        except:
            MSGBOX("签名程序执行异常！")
            self.text_signeffective_2.setText("签名异常")
            return
        status = '签名成功' if ret==0 else "签名失败"
        self.text_signeffective_2.setText(status)

    '''验证页面'''

    def on_btn_verifyfile_clicked(self):
        '''选择需要签名的原文件'''
        filename = QFileDialog.getOpenFileName()[0]
        curdir = os.getcwd().replace("\\", "/")
        sigdir = f'{curdir}/'
        if not os.path.exists(sigdir):
            os.mkdir(sigdir)
        self.text_verifyfile.setText(filename)
        
    def on_btn_signfile_clicked(self):
        '''选择需要验证的文件'''
        filename = QFileDialog.getOpenFileName()[0]
        curdir = os.getcwd().replace("\\", "/")
        sigdir = f'{curdir}/'
        if not os.path.exists(sigdir):
            os.mkdir(sigdir)      
        self.text_signfile.setText(filename)

    def on_verifysign_btn_clicked(self):
        Form_verifysign = QtWidgets.QDialog()
        ui = Ui_signverify()
        ui.setupUi(Form_verifysign)
        Form_verifysign.show()
        Form_verifysign.exec_()
        
        passwd = ui.input_signverify.text().encode()

        ret =  self.key.Dekey(passwd)
        if ret == None:
            MSGBOX("口令错误，验证失败！")
            return

        self.text_signerUuid.setText(self.combo_signer.currentText())
        self.text_agentUuid.setText(self.key.key['uuid'])
        self.text_time.setText(time.asctime())

        try:
            ret = self.key.Verify(self.text_verifyfile.text(),
                                  self.text_signfile.text(), None)
        except:
            MSGBOX("验证程序执行异常！")
            self.text_signeffective.setText("验证异常")
            return
        status = '验证成功' if ret==0 else "验证失败"
        self.text_signeffective.setText(status)

    '''代理页面'''

    def on_newproxy_btn_clicked(self):                                        #-----------------新建代理验证
        Form_newproxy = QtWidgets.QDialog()
        ui = Ui_ProxyNewVerify()
        ui.setupUi(Form_newproxy)
        Form_newproxy.show()
        Form_newproxy.exec_()

        passwd = ui.input_proxynewverify.text().encode()

        ret =  self.key.Dekey(passwd)
        if ret == None:
            MSGBOX("口令错误，验证失败！")
        else:
            Form_newproxyuuid = QtWidgets.QDialog()
            ui_2 = Ui_NewProxy()
            ui_2.setupUi(Form_newproxyuuid)
            Form_newproxyuuid.show()
            Form_newproxyuuid.exec_()
            NewAgent(self.key.key['uuid'],ui_2.input_newproxy.text(),self.al,self.sock)



    def on_select_client(self):
        self.text_uuid.setText(self.combo_clientlist.currentText())
        try:
            self.text_proxypublickey.setText(self.cl.user[self.combo_clientlist.currentText()]['keypub'])
        except BaseException:
            pass

   #待解决
    def on_select_auth(self):

        self.text_uuid.setText(self.combo_authorizelist.currentText())
        try:
            self.text_proxypublickey.setText(self.al.user[self.combo_authorizelist.currentText()]['keypub'])
        except BaseException:
            pass
       

    def on_cancleauthorize_btn_clicked(self):                                     #---------------------撤销授权验证
        Form_cancleauthorize= QtWidgets.QDialog()
        ui = Ui_ProxyCancleVerify()
        ui.setupUi(Form_cancleauthorize)
        Form_cancleauthorize.show()
        Form_cancleauthorize.exec_()

        passwd = ui.input_proxycancleverify.text().encode()

        ret =  self.key.Dekey(passwd)
        if ret == None:
            MSGBOX("口令错误，验证失败！")   
        else:
            DelAgent(self.key.key['uuid'],ui.input_proxycancleverify.text(),self.al,self.sock) 
            self._loadUserList()


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


    def _recieve_new_msg(self):
        if self.sock.agentreq:
            view = QtWidgets.QDialog()
            passwd_arg = ['...']
            ui = MyAcceptAgent(view, passwd_arg)
            ui.text_accagentuuid.setText(self.sock.agentreq['ouuid'])
            view.show()
            view.exec_()


            self.sock.agentreq = None
            k = Key(uuid='ouuid',key=None, passwd=passwd_arg[0])
            self._loadUserList()
           



def MSGBOX(msg: str):
    "弹出异常消息提示框"
    msgb = QtWidgets.QMessageBox()
    msgb.setText(msg)
    msgb.show()
    msgb.exec()






