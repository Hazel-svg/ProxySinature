from uiFromQt.acceptAgent import Ui_AcceptAgent


class MyAcceptAgent(Ui_AcceptAgent):
    def __init__(self, view):
        super().setupUi(view)
        self.btn_acceptagent.clicked.connect(self._on_btn_ok_clicked())

    def _on_btn_ok_clicked(self):
        self._modifyPasswd()

    def _modifyPasswd(self):
        '''修改口令'''
        pass

