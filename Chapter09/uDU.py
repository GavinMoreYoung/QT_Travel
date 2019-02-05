import sqlite3
import sys

from PyQt5.QtWidgets import QDialog, QApplication

from untitledDU import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.delbutton.clicked.connect(self.DeleteUser)
        self.ui.byes.clicked.connect(self.ConfirmDelete)
        self.ui.label_4.hide()
        self.ui.byes.hide()
        self.ui.bno.hide()
        self.show()
    def DeleteUser(self):
        sql = "select *from user where address like '"+self.ui.email.text()+"' and password like '"+self.ui.passwd.text()+"'"
        try:
            conn = sqlite3.connect("_Database.db")
            cur = conn.cursor()
            cur.execute(sql)
            row = cur.fetchone()
            if row == None:
                self.ui.label_4.hide()
                self.ui.byes.hide()
                self.ui.bno.hide()
                self.ui.message.setText("sorry,incorrect email address or password")
            else:
                self.ui.label_4.show()
                self.ui.byes.show()
                self.ui.bno.show()
                self.ui.message.setText("")
        except sqlite3.Error as e:
            self.ui.message.setText("Error in accessing user account")
        finally:
            conn.close()
    def ConfirmDelete(self):
        sql = "delete from user where address= '"+self.ui.email.text()+"'"
        try:
            conn = sqlite3.connect("_Database.db")
            cur = conn.cursor()
            with conn:
                print(sql)
                cur.execute(sql)
                self.ui.message.setText("user successfully deleted")
        except sqlite3.Error as e:
            self.ui.message.setText("Error in deleting user account")
        finally:
            conn.close()
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())