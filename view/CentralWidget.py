from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.imageLabel = QLabel()
        vlay = QVBoxLayout()
        vlay.addWidget(self.imageLabel)
        self.setLayout(vlay)

    @property
    def image(self):
        return self.imageLabel

    @image.setter
    def image(self, path):
        image = QPixmap(path)
        self.imageLabel.setPixmap(image)