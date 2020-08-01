from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from . import CentralWidget, RightPanel, ChronoWidget, StartWidget
import model.Engine

class GameWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.nextPlayerButton = QPushButton("Joueur suivant")
        self.passButton = QPushButton("Image suivante")
        self.foundButton = QPushButton("Image trouvée")
        self.restartButton = QPushButton("Nouvelle partie")
        self.playerLabel = QLabel("Joueur 1")
        vlay = QVBoxLayout()
        vlay.addWidget(self.playerLabel)
        hlay = QHBoxLayout()
        hlay.addWidget(self.nextPlayerButton)
        hlay.addWidget(self.passButton)
        hlay.addWidget(self.foundButton)
        hlay.addWidget(self.restartButton)
        vlay.addLayout(hlay)
        self.setLayout(vlay)

class BottomPanel(QDockWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.setMinimumHeight(100)
        self.chronoWidget = ChronoWidget.ChronoWidget()
        self.gameWidget = GameWidget()
        self.setWidget(QWidget())
        hlay = QHBoxLayout()
        hlay.addWidget(self.gameWidget)
        hlay.addStretch()
        hlay.addWidget(self.chronoWidget)
        self.widget().setLayout(hlay)

class MainWindow(QMainWindow):
    def setImage(self):
        self.centralwidget.image = self.gameEngine.current_image

    def onLaunched(self):
        self.setImage()
        self.stackedWidget.setCurrentWidget(self.centralwidget)
        self.rightPanel.scoreWidget.setPlayers(self.gameEngine.players)
        self.bottomPanel.chronoWidget.elapsed_time = 0
        self.bottomPanel.chronoWidget.max_time = self.gameEngine.laptime * 1000
        self.bottomPanel.chronoWidget.timer.start(16)
        self.rightPanel.show()
        self.bottomPanel.show()

    def onTimeout(self):
        self.bottomPanel.chronoWidget.timer.stop()
        self.gameEngine.lapEnd()

    def onNextPlayerButton(self):
        self.gameEngine.nextPlayer()
        self.bottomPanel.gameWidget.playerLabel.setText(self.gameEngine.current_player.name)

    def onPassButton(self):
        self.gameEngine.nextImage()
        self.setImage()

    def onFoundButton(self):
        self.gameEngine.foundImage()
        self.setImage()
        self.rightPanel.scoreWidget.setScore(self.gameEngine.player_index, self.gameEngine.current_player.score)
        if self.gameEngine.isLapDone():
            self.restart()

    def restart(self):
        self.gameEngine.lapEnd()
        self.stackedWidget.setCurrentWidget(self.startwidget)
        self.rightPanel.hide()
        self.bottomPanel.hide()

    def __init__(self, engine):
        super().__init__()
        self.gameEngine = engine

        self.resize(800, 600)
        self.stackedWidget = QStackedWidget()
        self.centralwidget = CentralWidget.CentralWidget()
        self.startwidget = StartWidget.StartWidget(self.gameEngine)
        self.stackedWidget.addWidget(self.startwidget)
        self.stackedWidget.addWidget(self.centralwidget)
        self.stackedWidget.setCurrentWidget(self.startwidget)

        self.setCentralWidget(self.stackedWidget)
        self.rightPanel = RightPanel.RightPanel("Information", self)
        self.addDockWidget(Qt.RightDockWidgetArea, self.rightPanel)
        self.bottomPanel = BottomPanel(self)
        self.bottomPanel.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.addDockWidget(Qt.BottomDockWidgetArea, self.bottomPanel)

        self.startwidget.launchedSignal.connect(self.onLaunched)
        self.bottomPanel.chronoWidget.timeout.connect(self.onTimeout)
        self.bottomPanel.gameWidget.nextPlayerButton.clicked.connect(self.onNextPlayerButton)
        self.bottomPanel.gameWidget.passButton.clicked.connect(self.onPassButton)
        self.bottomPanel.gameWidget.foundButton.clicked.connect(self.onFoundButton)
        self.bottomPanel.gameWidget.restartButton.clicked.connect(self.restart)

        self.rightPanel.hide()
        self.bottomPanel.hide()