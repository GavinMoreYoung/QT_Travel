import sys

from PyQt5.QtWidgets import QApplication, QDialog

from untitledRS import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.roomtypes=['suite','super luxury','super deluxe','ordinary']
        self.addcontent()
        self.ui.pushButton.clicked.connect(self.computeRoomRent)
        self.show()
    def addcontent(self):
        for i in self.roomtypes:
            self.ui.comboBox.addItem(i)
    def computeRoomRent(self):
        dateselected = self.ui.calendarWidget.selectedDate()
        dateinstring = str(dateselected.toPyDate())
        noOfDays = self.ui.spinBox.value()
        chosenRoomType = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        self.ui.message.setText("Date of reservation: "+dateinstring+" , Number of days : "+ str(noOfDays) + " and Room type selected : " + chosenRoomType )
        roomRent = 0
        if chosenRoomType == "suite":
            roomRent=40
        if chosenRoomType=="super luxury":
            roomRent=30
        if chosenRoomType=="super deluxe":
            roomRent=20
        if chosenRoomType=="ordinary":
            roomRent=10
        total = roomRent*noOfDays
        self.ui.message1.setText("Room Rent for single day for "+chosenRoomType+" type is "+str(roomRent)+"$.nTotal room rent is "+str(total))
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())