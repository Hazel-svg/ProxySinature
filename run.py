import sys

from PyQt5.QtWidgets import QApplication
from qtpy import QtWidgets

from myUI.myProxy import myProxy

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QtWidgets.QTabWidget()
    window = myProxy(Form)
    Form.show()
    tid = app.exec_()

    # 终止子线程，清理资源
    del window
    sys.exit(tid)
