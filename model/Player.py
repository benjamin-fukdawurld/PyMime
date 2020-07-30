from typing import NewType

class Player:
    def __init__(self, **kwargs):
        self.__name = kwargs.get("name", "Anonymous")
        self.__score = 0

    @property
    def name(self):
        return self.__name

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if value >= 0:
            self.__score = value

        raise ValueError("value is negative")

    def __add__(self, value):
        if value >= 0:
            return self.__score + value

        raise ValueError("value is negative")

    def __iadd__(self, value):
        if value >= 0:
            self.__score += value

        raise ValueError("value is negative")

    def __lt__(self, other):
        return self.score < other.score

    def __le__(self, other):
        return self.score <= other.score

    def __ge__(self, other):
        return self.score >= other.score

    def __gt__(self, other):
        return self.score > other.score

    def __eq__(self, other):
        return self.score == other.score

    def __ne__(self, other):
        return self.score != other.score

    def __str__(self):
        return self.name + ": " + str(self.score)
