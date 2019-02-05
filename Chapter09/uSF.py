import sqlite3
import sys

from PyQt5.QtWidgets import QDialog, QApplication

from untitledSF import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.SearchRows)
        self.show()
    def SearchRows(self):
        sql = "select * from user where address like '"+self.ui.email.text()+ "' and password like '"+self.ui.password.text()+"'"
        try:
            conn = sqlite3.connect("_Database.db")
            cur = conn.cursor()
            cur.execute(sql)
            row = cur.fetchone()
            if row == None:
                self.ui.message.setText("sorry,Incorrect email or password")
            else:
                self.ui.message.setText("You are welcome")
        except sqlite3.Error as e:
            self.ui.message.setText("error in accessing row")
        finally:
            conn.close()
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())