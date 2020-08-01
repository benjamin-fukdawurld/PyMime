import random
from os import listdir
from os.path import isfile, join

class ImageDirectory:
    def __init__(self, **kwargs):
        self.__path = kwargs.get("path", ".")
        self.__image_paths = []

    def shuffleImages(self):
        random.shuffle(self.__image_paths)

    def loadImages(self):
        for f in listdir(self.path):
            p = join(self.__path, f)
            if isfile(p):
                self.__image_paths.append(p)

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value
        self.__image_paths = []

    def add_image_paths(self, paths):
        self.__image_paths += paths

    @property
    def image_paths(self):
        return self.__image_paths

    def __len__(self):
        return len(self.__image_paths)
    
    def __getitem__(self, index):
        return self.__image_paths[index]

    def __setitem__(self, index, value):
        self.__image_paths[index] = value

    def __delitem__(self, index):
        del self.__image_paths[index]

    def __getslice__(self, i, j):
        return self.__image_paths[i:j]

    def __setslice__(self, i, j, sequence):
        self.__image_paths[i:j] = sequence

    def __delslice__(self, i, j):
        del self.__image_paths[i:j]
