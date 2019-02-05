import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QGraphicsScene, QGraphicsPixmapItem, QApplication

from untitledGV import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.scene = QGraphicsScene(self)
        pixmap = QtGui.QPixmap()
        pixmap.load("scene.jpg")
        item = QGraphicsPixmapItem(pixmap)
        self.scene.addItem(item)
        self.ui.graphicsView.setScene(self.scene)
if __name__=="__main__":
    app = QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())