from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import model.Engine

class StartWidget(QWidget):
    launchedSignal = pyqtSignal()
    
    def onBrowse(self):
            self.dirline.setText(QFileDialog.getExistingDirectory(
                self, "Open Directory",
                ".",
                QFileDialog.ShowDirsOnly
                | QFileDialog.DontResolveSymlinks))

    def onLaunch(self):
        self.gameEngine.players.clear()
        i = 1
        while i <= self.playerSpinBox.value():
            self.gameEngine.addPlayer(model.Player.Player(name = "Joueur {}".format(str(i))))
            i += 1
        
        self.gameEngine.imgdir.path = self.dirline.text()
        self.gameEngine.laptime = self.timeSpinBox.value()

        self.gameEngine.imgdir.loadImages()
        self.gameEngine.imgdir.shuffleImages()
        self.launchedSignal.emit()

    def __init__(self, engine):
        super().__init__()
        flay = QFormLayout()
        self.gameEngine = engine
        self.playerSpinBox = QSpinBox()
        self.playerSpinBox.setMinimum(1)
        self.playerSpinBox.setMaximum(10)
        self.playerSpinBox.setValue(1)
        self.timeSpinBox = QSpinBox()
        self.timeSpinBox.setMinimum(1)
        self.timeSpinBox.setMaximum(3600)
        self.timeSpinBox.setValue(30)
        self.dirWidget = QWidget()
        hlay = QHBoxLayout()
        self.dirline = QLineEdit()
        self.dirbrowse = QPushButton("parcourir")
        self.dirbrowse.clicked.connect(self.onBrowse)
        hlay.addWidget(self.dirline)
        hlay.addWidget(self.dirbrowse)
        self.dirWidget.setLayout(hlay)

        flay.addRow("Nombre de joueurs", self.playerSpinBox)
        flay.addRow("Temps", self.timeSpinBox)
        flay.addRow("Dossier d'images", self.dirWidget)

        self.launchButton = QPushButton("lancer la partie")
        flay.addWidget(self.launchButton)
        self.launchButton.clicked.connect(self.onLaunch)

        self.setLayout(flay)
