from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from . import ScoreWidget

class RightPanel(QDockWidget):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.setAllowedAreas(Qt.RightDockWidgetArea)
        self.scoreWidget = ScoreWidget.ScoreWidget()
        self.setMinimumWidth(200)
        vlay = QVBoxLayout()
        vlay.addWidget(self.scoreWidget)
        widget = QWidget()
        widget.setLayout(vlay)
        self.setWidget(widget)
