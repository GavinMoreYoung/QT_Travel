import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QApplication

from untitledMC import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
    def mousePressEvent(self, event):
        if event.buttons() & QtCore.Qt.LeftButton:
            x = event.x()
            y = event.y()
            text = "x:{0}, y:{1}".format(x,y)
            self.ui.press.setText("Mouse button pressed at   "+text)
    def mouseReleaseEvent(self, event):
        x = event.x()
        y = event.y()
        text = "x:{0}, y{1}".format(x,y)
        self.ui.release.setText("mouse button released at   "+text)
        self.update()
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())