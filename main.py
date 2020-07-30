import model.Player
import model.ImageDirectory

p = model.Player.Player(name = "test")
p2 = model.Player.Player()

imdir = model.ImageDirectory.ImageDirectory(path = "images")
imdir.loadPaths()
print(imdir.image_paths)
imdir.shufflePaths()
print(imdir.image_paths)

print(p)
print(p2)


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