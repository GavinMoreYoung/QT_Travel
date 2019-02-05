import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QDialog

from demoDB import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.creadteDatabase)
        self.show()
    def creadteDatabase(self):
        try:
            conn = sqlite3.connect(self.ui.lineEdit.text() + ".db")
            self.ui.label_2.setText("Database is created")
        except sqlite3.Error as e:
            self.ui.label_2.setText("Some error has occurred")
        finally:
            conn.close()
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
