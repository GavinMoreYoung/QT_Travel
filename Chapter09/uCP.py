import sqlite3
import sys

from PyQt5.QtWidgets import QDialog, QApplication

from untitledCP import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.ChangePassword)
        self.show()
    def ChangePassword(self):
        sql = "select * from user where address='"+self.ui.email.text()+"' and password='"+self.ui.oldpasswd.text()+"';"
        try:
            conn = sqlite3.connect("_Database.db")
            cur = conn.cursor()
            print(sql)
            cur.execute(sql)
            row = cur.fetchone()
            if row == None:
                self.ui.message.setText("sorry,incorrect email or password")
            else:
                if self.ui.newpassword.text() == self.ui.renewpasswd.text():
                    sql = "update user set password='"+self.ui.newpassword.text()+"' where address like '"+self.ui.email.text()+"'"
                    with conn:
                        cur.execute(sql)
                        self.ui.message.setText("Password successfully changed")
                else:
                    self.ui.message.setText("the two password don't match")
        except sqlite3.Error as e:
            self.ui.message.setText("Error in accessing row")
        finally:
            conn.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())