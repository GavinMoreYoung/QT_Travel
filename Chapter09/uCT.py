import sqlite3
import sys

from PyQt5.QtWidgets import QApplication, QDialog

from untitledCT import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_2.clicked.connect(self.createTable)
        self.ui.pushButton.clicked.connect(self.addColumns)
        self.show()
    def addColumns(self):
        try:
            conn = sqlite3.connect(self.ui.databasenm.text()+".db")
            c = conn.cursor()
            sql = "alter table "+self.ui.databasenm.text()+" add column "+self.ui.columnmn.text()+" "+self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
            print(sql)
            c.execute(sql)
            self.ui.message.setText("column add successfully")
        except:
            self.ui.message.setText("Error in creating table")
        finally:
            conn.close()
        self.ui.columnmn.setText("")
        self.ui.columnmn.setFocus()
    def createTable(self):
        try:
            conn = sqlite3.connect(self.ui.databasenm.text()+".db")
            self.ui.message.setText("Database is connected ")
            c = conn.cursor()
            sql = "create table "+self.ui.tablenm.text()+"("+self.ui.columnmn.text()+" "+self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())+");"
            print(sql)
            c.execute(sql)
            self.ui.message.setText("table is successfully created")
        except sqlite3.Error as e:
            self.ui.message.setText("Error in creating table")
        finally:
            conn.close()
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

