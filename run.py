import sys

from PyQt5.QtWidgets import QApplication
from qtpy import QtWidgets

from myUI.myProxy import myProxy

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QtWidgets.QTabWidget()
    window = myProxy(Form)
    # window.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
