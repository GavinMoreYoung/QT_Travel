import sys

from PyQt5.QtWidgets import QDialog, QApplication

from untitledSC import Ui_Dialog


class Student:
    name = ""
    code = ""
    def __init__(self,name,code):
        self.name = name
        self.code = code
    def getCode(self):
        return self.code
    def getName(self):
        return self.name
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.dispmessage)
        self.show()
    def dispmessage(self):
        studentObj = Student(self.ui.lineEdit_2.text(),self.ui.lineEdit.text())
        self.ui.label_3.setText("Name "+studentObj.getName()+" ,Code "+studentObj.getCode())
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())