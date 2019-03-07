#!/usr/bin/env python
# -*- coding: utf-8 -*-


import numpy as np
from animaux import Elephant , Rhinoceros

class GameMap:
    """
            Creating an animal.

            This create an animal with a position and a direction on a map.

            :param x: int
            :param y: int
            :param dir: int
            :param map: map.map
            :type car: car

            :Example:

            >>> a = animal(0,1,180,M)

            .. seealso:: elephant(), rhinoceros()
            .. warning:: This class is abstract and can not be instanciated.
    """
    def __init__(self, size, bouldercoords, nb_elephants, nb_rhinos):
        self.__size = [5,5]
        self.__bouldercoords = [[2,3],[3,3],[4,3]]
        self.__nb_elephants = 0
        self.__nb_rhinos = 0

    def add(self, car, x, y, dir):
        x, y = animal.coords
        if car=="Rhinoceros":
            if self.nb_rhinos < 5:
                self[x,y] = Rhinoceros(x, y, dir, self)
            else:
                return (False)

        if car=="Elephant":
            if self.nb_elephants < 5:
                self[x,y] = Elephant(x, y, dir, self)
            else:
                return False
        else:
            return False

    def delete(self, animal):
        x,y=animal.coords
        if self[x, y] != 0 and (x == 0 or x == 4 or y == 0 or y == 4):
            if isinstance(self[x,y],Rhinoceros):
                self.nb_rhinos-=1
                self[x, y] = 0
            else:
                return False

            if isinstance(self[x,y],Elephant):
                self.nb_elephants-=1
                self.Elephant(x, y, dir, self)
            else:
                return False
        else:
            return False