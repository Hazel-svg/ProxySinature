from uiFromQt.acceptAgent import Ui_AcceptAgent
from uiFromQt.NewProxyPasswd import Ui_NewProxyPasswd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog
from PyQt5.QtCore import QCoreApplication


class MyAcceptAgent(Ui_AcceptAgent):
    def __init__(self, view, passwd_arg):
        super().setupUi(view)
        self.btn_acceptagent.clicked.connect(self._on_btn_ok_clicked)
        self.btn_rejectagent.clicked.connect(self._on_btn_no_clicked)

        # 成员变量获取新口令, 使用list 为引用传值
        self.passwd_arg = passwd_arg
        self.view = view
        self.ret = None

    def _on_btn_ok_clicked(self):
        self._modifyPasswd()
        self.ret = True
        self.view.close()
        
    
    def _on_btn_no_clicked(self):
        self.view.close()
        self.ret = False

    


    def _modifyPasswd(self):
        '''修改口令'''

        # TODO:新建修改口令对话框
        Form_NewProxyPasswd= QtWidgets.QDialog()
        ui = Ui_NewProxyPasswd()
        ui.setupUi( Form_NewProxyPasswd)
        Form_NewProxyPasswd.show()
        Form_NewProxyPasswd.exec_()

        # TODO:text()获取编辑框口令内容
        pass
        new_passwd = ui.input_newproxypasswd.text().encode()

        self.passwd_arg[0] = new_passwd