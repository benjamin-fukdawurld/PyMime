from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class ScoreWidget(QTableWidget):
    def __init__(self, players = []):
        super().__init__()
        self.setColumnCount(2)
        self.setPlayers(players)

    def setPlayers(self, players):
        self.players = players
        self.setRowCount(len(self.players))
        i = 0
        for p in self.players:
            self.setItem(i, 0, QTableWidgetItem(p.name))
            self.setItem(i, 1, QTableWidgetItem(str(p.score)))
            i += 1

    def setScore(self, index, value):
        self.item(index, 1).setText(str(value))
