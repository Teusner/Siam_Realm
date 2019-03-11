#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from animaux import Animal


class GameMap (list):
    def __init__(self):
        for k in range(5):
            self.append([0, 0, 0, 0, 0])
        self.__nb_elephants = 0
        self.__nb_rhinoceros = 0
        #for k in range(3):          # Setting up the 3 Boulders
        #    self[1+k][2]=Boulder()

    def add(self, animal):
        x, y = animal.coords
        if animal.species == 'Elephant' and self.__nb_elephants < 5 and (x == 0 or x == 4 or y == 0 or y == 4) and self[x][y]==0:
            self[x][y] = animal
        elif animal.species == 'Rhinoceros' and self.__nb_rhinoceros < 5 and (x == 0 or x == 4 or y == 0 or y == 4) and self[x][y]==0:
            self[x][y] = animal
        else:
            return False

    def delete(self, animal):
        x, y = animal.coords
        if x == 0 or x == 4 or y == 0 or y == 4:
            self[x][y] = 0
        else:
            return False

    def __str__(self):
        """
            Show the current state of the game board

            :return: the string with the characteristics of the board
            :rtype: str
        """
        s=' '
        for j in range(5):
            for i in range(5):
                if self[i][j] == 0:
                   s+='0 '
                elif self[i][j].species == 'Elephant' :
                    s+='E '
                elif self[i][j].species == 'Rhinoceros':
                    s+='R '
                else :
                    s+='B '
            s+='\n '
        return s


if __name__ == '__main__':
    g=GameMap()
    g.add(Animal(0, 0, np.array([1,0]), 'Rhinoceros'))
    g.add(Animal(4, 2, np.array([1, 0]), 'Elephant'))
    print(g)
