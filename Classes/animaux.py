#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

'''
    The ``Animal`` module
    ======================

    This module is creating animals for the Siam Realm game. Each animals has
    a position on te map, a direction and an id.

    :Example:

    >>> import animal
    >>> import map
    >>> M = Map()
    >>> e = Elephant(0,1,180,M)
    >>> r = Rhinoceros(1,4,0,M)

    Inheritance of the Animal class
    -------------------------------

    Each animal (elephant, Rhinoceros) is inherited of the animal class. It's impossible to
'''


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

            # >>> M = Map()
            # >>> a = Animal(0,1,180,M)

            .. seealso:: elephant(), rhinoceros()
            .. warning:: This class is abstract and can not be instanciated.
    """
    def __init__(self, x, y, dir, species):
        self.__coords = x,y
        self.__direction = dir
        self.__species = species

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
        if np.sqrt(ndir[0]**2+ndir[1]**2)==1 and (ndir[0]==0 or ndir[1]==0) :
            self.__direction = ndir

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, nspecies):
        if nspecies in ['Elephant','Rhinoceros']:
            self.__species = nspecies

    def move(self, nx, ny):
        self.coords = (nx,ny)

    def rotate(self, dir):
        self.direction = dir

    def __str__(self):
        """
            Show the current state of an animal

            :return: the string with the characteristics of the animal
            :rtype: str
        """
        return self.__species + ' : [Position = (' + str(self.coords[0]) + \
               ',' + str(self.coords[1]) + ') ; Direction = '+ \
               str(self.direction) + ']\n'


if __name__ == '__main__':
    a = Animal(0, 2, np.array([1,0]), 'Elephant')
    b = Animal(1, 2, np.array([1,0]), 'Rhinoceros')
    b.move(1,4)
    a.rotate(np.array([0,1]))
    print(a, b)