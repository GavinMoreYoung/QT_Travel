import sqlite3
import sys

from PyQt5.QtWidgets import QDialog, QApplication

from untitledSR import Ui_Dialog

rowNo=1
sql="SELECT * FROM User"
conn = sqlite3.connect("_Database.db")
cur = conn.cursor()
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        cur.execute(sql)
        self.ui.first.clicked.connect(self.showFirstRow)
        self.ui.previous.clicked.connect(self.showPreviousRow)
        self.ui.next.clicked.connect(self.showNextRow)
        self.ui.last.clicked.connect(self.showLastRow)
        self.show()
    def showFirstRow(self):
        try:
            cur.execute(sql)
            row =cur.fetchone()
            if row:
                self.ui.eamil.setText(row[0])
                self.ui.passwd.setText(row[1])
        except sqlite3.Error as e:
            self.ui.message.setText("Error in accessing table")
    def showPreviousRow(self):
        global  rowNo
        rowNo -= 1
        sql = "select * from user where rowid = "+str(rowNo)
        cur.execute(sql)
        row = cur.fetchone()
        if row:
            self.ui.message.setText("")
            self.ui.eamil.setText(row[0])
            self.ui.passwd.setText(row[1])
        else:
            rowNo += 1
            self.ui.message.setText("This is the first row")
    def showNextRow(self):
        global rowNo
        rowNo += 1
        sql = "select * from user where rowid = "+str(rowNo)
        cur.execute(sql)
        row = cur.fetchone()
        if row:
            self.ui.message.setText("")
            self.ui.eamil.setText(row[0])
            self.ui.passwd.setText(row[1])
        else:
            rowNo -= 1
            self.ui.message.setText("This is the last row")
    def showLastRow(self):
        cur.execute(sql)
        for row in cur.fetchall():
            self.ui.eamil.setText(row[0])
            self.ui.passwd.setText(row[1])
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())