import sqlite3
import sys

from PyQt5.QtWidgets import QDialog, QApplication

from untitledRIT import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.InsertRows)
        self.show()
    def InsertRows(self):
        sqlStatement = "insert into "+self.ui.tablenm.text()+" values("+self.ui.email.text()+","+self.ui.password.text()+");"
        print(sqlStatement)
        try:
            conn = sqlite3.connect(self.ui.datanm.text()+".db")
            with conn:
                cur = conn.cursor()
                cur.execute(sqlStatement)
                self.ui.message.setText("Row successfully")
        except sqlite3.Error as e:
            self.ui.message.setText("Error in inserting row")
        finally:
            conn.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())