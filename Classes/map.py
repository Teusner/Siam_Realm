#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import numpy as np
import numpy as np

class Animal:
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
    def __init__(self, x, y, dir, map):
        self.__coords = x,y
        self.__direction = dir

    @property
    def coords(self):
        return self.__coords

    @coords.setter
    def coords(self, ncoords):
        nx,ny=ncoords
        if nx < 5 and ny < 5 :
            self.__coords = nx,ny

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, ndir):
        if ndir % 90 == 0:
            self.__direction = ndir

    def move(self, nx, ny):
        self.coords = (nx,ny)

    def rotate(self, dir):
        self.direction = dir