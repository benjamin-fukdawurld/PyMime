import model.ImageDirectory as ImageDirectory
import model.Player as Player


class Engine:
    def __init__(self):
        self.__players = []
        self.__imgdir = ImageDirectory.ImageDirectory()
        self.__laptime = 30

    @property
    def players(self):
        return self.__players

    @property
    def imgdir(self):
        return self.__imgdir

    @property
    def laptime(self):
        return self.__laptime

    @laptime.setter
    def laptime(self, value):
        if value > 0:
            self.__laptime

        raise ValueError("value is not positive")

    def addPlayer(self, player: Player.Player):
        self.__players.append(player)

    def initParty(self):
        for p in self.__players:
            p.score = 0

        self.imgdir.loadPaths()
        self.imgdir.shufflePaths()

        imglen = len(self.imgdir)
        imgBonuses = imglen % len(self.players)
        imgMax = imglen - imgBonuses