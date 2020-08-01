import model.Player as Player
import model.Engine as Engine


import view.MainWindow

import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

app = QApplication(sys.argv)
engine = Engine.Engine()
mainwindow = view.MainWindow.MainWindow(engine)
mainwindow.show()
app.exec_()


# import random
# import tkinter
# import PIL
# from os import listdir
# from os.path import isfile, join

# class PlayerTeam:
#     def __init__(self, name, score = 0):
#         self.name = name
#         self.score = score

# class GameConfig:
#     def __init__(self, lap_time = 30):
#         self.scores = []
#         self.lap_time = lap_time

# class GameUi:
#     def __init__(self, config: GameConfig):
#         self.config = config
#         self.window = tkinter.Tk()
#         self.window.title("PyMime")
#         self.__openImage("/home/ben/Imagesfleur-bougainvilliers-rose-isole-fond-blanc-copie-espace_127755-183.jpg")
#         self.canvas = tkinter.Canvas(self.window, width = 400, height = 400)
#         self.canvas.grid()

#     def __openImage(path):
#         img = PIL.Image.open(path)
#         self.image = PIL.ImageTk.PhotoImage(img)

#     def run(self):
#         self.window.mainloop()


# config = GameConfig()
# game = GameUi(config)


# game.run()