from . import ImageDirectory
from . import Player


class Engine:
    def __init__(self):
        self.__players = []
        self.player_index = 0
        self.image_index = 0
        self.__found = []
        self.__imgdir = ImageDirectory.ImageDirectory()
        self.__laptime = 30

    def nextPlayer(self):
        self.player_index += 1
        self.player_index %= len(self.players)

    def nextImage(self):
        if len(self.imgdir) == 0:
            return

        self.image_index += 1
        self.image_index %= len(self.imgdir)

    def foundImage(self):
        self.current_player.score += 1
        self.__found.append(self.current_image)
        del self.imgdir[self.image_index]
        if len(self.imgdir) > 0:
            self.image_index %= len(self.imgdir)


    def isLapDone(self):
        return len(self.imgdir) == 0

    def isGameDone(self):
        return self.player_index == len(self.players)

    def lapEnd(self):
        self.imgdir.add_image_paths(self.__found)
        self.__found.clear()
        self.imgdir.shuffleImages()
    

    @property
    def current_player(self):
        return self.players[self.player_index]

    @property
    def players(self):
        return self.__players

    @property
    def current_image(self):
        return self.__imgdir[self.image_index]

    @property
    def imgdir(self):
        return self.__imgdir

    @property
    def laptime(self):
        return self.__laptime

    @laptime.setter
    def laptime(self, value):
        if value > 0:
            self.__laptime = value
        else:
            raise ValueError("value is not positive")

    def addPlayer(self, player: Player.Player):
        self.__players.append(player)

    def initParty(self):
        for p in self.__players:
            p.score = 0

        self.imgdir.loadPaths()
        self.imgdir.shufflePaths()