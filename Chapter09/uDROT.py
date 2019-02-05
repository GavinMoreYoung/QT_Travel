import sqlite3
import sys

from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QApplication

from untitledDROT import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui =Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.DisplayRows)
        self.show()
    def DisplayRows(self):
        sql = "select * from "+self.ui.lineEdit_2.text()
        try:
            conn = sqlite3.connect(self.ui.lineEdit.text()+".db")
            cur = conn.cursor()
            cur.execute(sql)
            rows = cur.fetchall()
            rowNo = 0
            for tuple in rows:
                self.ui.message.setText("")
                colNo = 0
                for columns in tuple:
                    oneC = QTableWidgetItem(columns)
                    self.ui.tableWidget.setItem(rowNo, colNo, oneC)
                    colNo += 1
                rowNo += 1
        except sqlite3.Error as e:
            self.ui.tableWidget.clear()
            self.ui.message.setText("Error in accessing table")
        finally:
            conn.close()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())