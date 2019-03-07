#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from animaux import Animal


class GameMap (np.ndarray):
    def __init__(self):
        self.resize((4, 4))
        self.__nb_elephants = 0
        self.__nb_rhinoceros = 0
        for k in range(3):          # Setting up the 3 Boulders
            self[1+k, 2]=Boulder()

    def add(self, animal):
        x, y = animal.coords
        if animal.species == 'Elephant' and self.__nb_elephants < 5 and (x == 0 or x == 4 or y == 0 or y == 4) and self[x, y] is None:
            self[x,y] = animal
        elif animal.species == 'Rhinoceros' and self.__nb_rhinoceros < 5 and (x == 0 or x == 4 or y == 0 or y == 4) and self[x, y] is None:
            self[x,y] = animal
        else:
            return False

    def delete(self, animal):
        x, y = animal.coords
        if x == 0 or x == 4 or y == 0 or y == 4:
            self[x, y] = 0
        else:
            return False
