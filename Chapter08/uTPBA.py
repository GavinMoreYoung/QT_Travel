import asyncio
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from quamash import QEventLoop

from untitledTPBA import Ui_Dialog

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.invokeAsync)
        self.show()
    def invokeAsync(self):
        asyncio.ensure_future(self.updt(0.5, self.ui.progressBar))
        asyncio.ensure_future(self.updt(1, self.ui.progressBar_2))
    @staticmethod
    async def updt(delay, progressbar):
        for i in range(101):
            await asyncio.sleep(delay)
            progressbar.setValue(i)
def stopper(loop):
    loop.stop()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    w = MyForm()
    w.exec()
    with loop:
        loop.run_forever()
    loop.close()
    sys.exit(app.exec_())
