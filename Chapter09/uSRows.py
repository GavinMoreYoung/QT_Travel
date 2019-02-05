import sqlite3
import sys

from PyQt5.QtWidgets import QDialog, QApplication

from untitledSRows import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.SearchRows)
        self.show()
    def SearchRows(self):
        sql = "select password from "+self.ui.tablenm.text() + " where address like '"+self.ui.email.text()+"'"
        try:
            conn = sqlite3.connect(self.ui.databasenm.text()+".db")
            cur = conn.cursor()
            print(sql)
            cur.execute(sql)
            row = cur.fetchone()
            if row == None:
                self.ui.message.setText("sorry,nouser found with this email address")
                self.ui.passwd.setText("")
            else:
                self.ui.message.setText("email address found, password of this user is:")
                self.ui.passwd.setText(row[0])
        except sqlite3.Error as e:
            self.ui.message.setText("Error in accessing row")
        finally:
            conn.close()
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())