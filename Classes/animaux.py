#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from gamemap import Map

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


class Elephant(Animal):
    """
            Creating an elephant.

            This create an elephant with a position and a direction on a map.

            :param x: int
            :param y: int
            :param dir: int
            :param map: map.map
            :type car: car

            :Example:

            # >>> e = Elephant(0,1,180,M)

            .. seealso:: move(), rotate()
            .. warning:: You should create an Elephant on a map.
    """
    def __init__(self, x, y, dir, map):
        super().__init__(x, y, dir, map)
        self._car = 'E'

    def __str__(self):
        """
            Show the current state of an elephant

            :return: the string with all
            :rtype: str
        """
        return 'Elephant : [Position = (' + str(self.coords[0]) + \
               ',' + str(self.coords[1]) + ') ; Direction = '+ \
               str(self.direction) + ']\n'


class Rhinoceros(Animal):
    """
            Creating a rhinoceros.

            This create a rhinoceros with a position and a direction on a map.

            :param x: int
            :param y: int
            :param dir: int
            :param map: map.map
            :type car: car

            :Example:

            # >>> r = rhinoceros(0,1,180,M)

            .. seealso:: move(), rotate()
            .. warning:: You should create a rhinoceros on a map.
    """
    def __init__(self, x, y, dir, map):
        super().__init__(x, y, dir, map)
        self.car = 'R'

    def __str__(self):
        """
            Show the current state of an elephant

            :return: the string with all
            :rtype: str
        """
        return 'Rhinoceros : [Position = (' + str(self.coords[0]) + \
               ',' + str(self.coords[1]) + ') ; Direction = '+ \
               str(self.direction) + ']\n'


if __name__ == '__main__':
    a = Elephant(0, 2, 90, 10)
    b = Rhinoceros(0, 2, 90, 10)
    b.move(1,5)
    a.rotate(180)
    print(a, b)