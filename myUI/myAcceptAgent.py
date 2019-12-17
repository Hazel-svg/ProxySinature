from uiFromQt.acceptAgent import Ui_AcceptAgent


class MyAcceptAgent(Ui_AcceptAgent):
    def __init__(self, view, passwd_arg):
        super().setupUi(view)
        self.btn_acceptagent.clicked.connect(self._on_btn_ok_clicked)

        # 成员变量获取新口令, 使用list 为引用传值
        self.passwd_arg = passwd_arg

    def _on_btn_ok_clicked(self):
        self._modifyPasswd()


    def _modifyPasswd(self):
        '''修改口令'''

        # TODO:新建修改口令对话框
        pass

        # TODO:text()获取编辑框口令内容
        pass
        new_passwd = None

        self.passwd_arg[0] = new_passwd