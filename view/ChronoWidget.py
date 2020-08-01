from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class ChronoWidget(QWidget):
    timeout = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.onTimer)
        self.label = QLabel("")
        f = self.label.font()
        f.setPointSize(25)
        self.label.setFont(f)
        self.elapsed_time = 0
        vlay = QVBoxLayout()
        vlay.addWidget(self.label)
        self.setLayout(vlay)
        self.remaining_time = 0
        self.__max_time = 0
        hlay = QHBoxLayout()
        self.pauseButton = QPushButton("pause")
        self.pauseButton.setCheckable(True)
        self.pauseButton.toggled.connect(self.onPauseButton)
        hlay.addWidget(self.pauseButton)
        self.restartButton = QPushButton("recommencer")
        self.restartButton.clicked.connect(self.onRestartButton)
        hlay.addWidget(self.restartButton)
        vlay.addLayout(hlay)

    def onPauseButton(self, checked):
        if checked:
            self.pause()
            self.pauseButton.setText("lecture")
        else:
            self.play()
            self.pauseButton.setText("pause")

    def onRestartButton(self):
        self.stop()
        self.pauseButton.blockSignals(True)
        self.pauseButton.setChecked(True)
        self.pauseButton.blockSignals(False)

    def onTimer(self):
        self.elapsed_time += 16
        self.remaining_time = self.max_time - self.elapsed_time
        if self.remaining_time < 0:
            self.remaining_time = 0
            self.timeout.emit()

        self.showTime()

    def pause(self):
        self.timer.stop()
        self.showTime()

    def play(self):
        self.timer.start()
        self.showTime()

    def stop(self):
        self.timer.stop()
        self.elapsed_time = 0
        self.remaining_time = self.max_time
        self.showTime()

    @property
    def max_time(self):
        return self.__max_time

    @max_time.setter
    def max_time(self, value):
        self.__max_time = value
        self.remaining_time = value
        self.elapsed_time = 0

    def showTime(self):
        seconds = (self.remaining_time/1000)%60
        seconds = int(seconds)
        minutes = (self.remaining_time/(1000*60))
        minutes = int(minutes)

        self.label.setText("{}:{}.{}".format(minutes, seconds, (self.remaining_time%1000)/10))