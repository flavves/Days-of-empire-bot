import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time

class AThread(QThread):
    threadSignalAThread = pyqtSignal(int)
    def __init__(self):
        super().__init__()

    def run(self):
        count = 0
        while 1:
            time.sleep(1)
            count += 1
            print("hello")
            self.threadSignalAThread.emit(count)


class MsgBoxAThread(QDialog):
    def __init__(self):
        super().__init__()
        layout     = QVBoxLayout(self)
        self.label = QLabel("")
        layout.addWidget(self.label)
        close_btn  = QPushButton("Close window")
        layout.addWidget(close_btn)
        close_btn.clicked.connect(self.close) 
        self.setGeometry(900, 300, 400, 80)
        self.setWindowTitle('MsgBox AThread(QThread)')


class Example(QMainWindow):
    def __init__(self, parent=None, *args):
        super().__init__(parent, *args)  
        self.setWindowTitle("Pyqt5 stop QThread worker on QAction")
        self.setGeometry(550, 300, 300, 300)
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)        
        layout   = QVBoxLayout(centralWidget)
        self.lbl = QLabel("Start")
        layout.addWidget(self.lbl)

        bar       = self.menuBar()
        barThread = bar.addMenu('Thread')
        quit      = bar.addMenu('Quit')
        quit.aboutToShow.connect(app.quit)         

        self.start_update = QAction('&Start', self)
        self.start_update.setShortcut('Ctrl+S')      
        self.start_update.triggered.connect(self._start_thread)

        self.stop_update = QAction('Sto&p', self)
        self.stop_update.setShortcut('Ctrl+P')
        self.stop_update.setVisible(False)
        self.stop_update.triggered.connect(self._stop_thread)

        barThread.addAction(self.start_update)
        barThread.addAction(self.stop_update)

        self.msg      = MsgBoxAThread()  
        self.myworker = None
        self.counter  = 0
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.recurring_timer)   
        self.timer.start()        
        self.show()

    def recurring_timer(self):
        self.counter += 10
        self.lbl.setText(" Do something in the GUI: <b> %d </b>" % self.counter)        

    def _start_thread(self):
        self.start_update.setVisible(False)
        self.stop_update.setVisible(True)
        self.myworker = AThread() 
        self.myworker.threadSignalAThread.connect(self.on_threadSignalAThread)
        self.myworker.finished.connect(self.finishedAThread)
        self.myworker.start()

    def finishedAThread(self):
        self.myworker = None
        self.start_update.setVisible(True)
        self.stop_update.setVisible(False)

    def on_threadSignalAThread(self, value):
        self.msg.label.setText(str(value))
        if not self.msg.isVisible():        
            self.msg.show() 

    def _stop_thread(self):
        self.stop_update.setVisible(False)
        self.start_update.setVisible(True)
        self.myworker.terminate()         
        self.myworker = None

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Question',
            "Are you sure you want to close the application?",
             QMessageBox.Yes,
             QMessageBox.No)
        if reply == QMessageBox.Yes:
            if self.myworker:
                self.myworker.quit()
            del self.myworker
            self.msg.close()

            super(Example, self).closeEvent(event)
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex  = Example()
    #ex.show()
    sys.exit(app.exec_())  