#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


class Animal:
    """
        The Animal module
        =================

        This module creates an animal with a position and a direction.

        :Args:
            :param x (int): is the abscissa of the animal,
            :param y (int): is the ordinate of the animal,
            :param dir (numpy.array): is the direction of the animal,
            :param species (str): is the species of the animal. It can take only the values "Elephant" or "Rhinoceros".

        :Example:
            >>> a = Animal(0, 1, np.array([0,1]), "Elephant")

        .. seealso:: Boulder(), Crosses()
    """
    def __init__(self, x, y, dir, species):
        self.__coords = x,y
        self.__direction = dir
        self.__species = species

    @property
    def coords(self):
        """
            This is the coordinates of the animal in a tuple.

            :Getter: Return the coordinates of the animal.
            :Setter: Set the coordinates of the animal
            :Type: tuple of int

            :Getter's example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> print(a.coords)

            :Setter's example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> a.coords((0, 2))

            .. warning:: The coordinates should be on the 5x5 board game.
        """
        return self.__coords

    @coords.setter
    def coords(self, ncoords):
        """
            Setting the coordinates or the animal. The coords should be

            :param ncoords (tuple): which are the new coords of the animal.
        """
        nx,ny=ncoords
        if nx < 5 and ny < 5 :
            self.__coords = nx,ny

    @property
    def direction(self):
        """
            This is the direction of the animal in a numpy.array. The direction is a unitary vector with a null coordinate.

            :Getter: Return the direction of the animal.
            :Setter: Set the direction of the animal
            :Type: numpy.array

            :Getter's example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> dir = a.direction
                >>> print(dir)

            :Setter's example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> a.direction(np.array([-1, 0])

            .. warning:: the direction should be a numpy.array unitary vector with a null coordinate.
        """
        return self.__direction

    @direction.setter
    def direction(self, ndir):
        """
            Setting the direction of the animal. The direction is a unitary vector with a null coordinate.

            :param ndir (numpy.array): which is the new direction of the animal.
        """
        if np.sqrt(ndir[0]**2+ndir[1]**2)==1 and (ndir[0]==0 or ndir[1]==0) :
            self.__direction = ndir

    @property
    def species(self):
        """
            This is the species of the animal. It should be "Elephant" or "Rhinoceros".

            :Getter: Return the species of the animal.
            :Setter: Set the species of the animal
            :Type: str

            :Getter's example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> print(a.species)

            :Setter's example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> a.species("Rhinoceros")

            .. warning:: the species should be "Elephant" or "Rhinoceros".
        """
        return self.__species

    @species.setter
    def species(self, nspecies):
        """
            Getting the species of the animal.

            :param nspecies (str): which is the new species of the animal.
        """
        if nspecies in ['Elephant', 'Rhinoceros']:
            self.__species = nspecies

    def move(self, nx, ny):
        """

        """
        self.coords = (nx,ny)

    def rotate(self, dir):
        self.direction = dir

    def bearing(self, animal):
        dira, dirb = self.direction, animal.direction
        return dira @ dirb

    def __str__(self):
        """
            Show the current state of an animal

            :return: the string with the characteristics of the animal
            :rtype: str
        """
        return self.__species + ' : [Position = ' + str(self.coords) + ' ; Direction = ' + str(self.direction) + ']\n'


class Boulder:
    """
        The Boulder module
        =================

        This module creates a boulder at a position.

        :Args:
            :param x (int): is the abscissa of the boulder,
            :param y (int): is the ordinate of the boulder,
            :param species (str): is the species of the species. It can only take the values "Boulder" and is here to be used with polymorphism.

        :Example:
            >>> b = Boulder(1, 2)

        .. warning:: The coordinates should be on the 5x5 board game.
        .. seealso:: Animal(), Crosses()
    """
    def __init__(self, x, y):
        self.coords = (x, y)
        self.species = 'Boulder'


if __name__ == '__main__':
    a = Animal(0, 2, np.array([1,0]), 'Elephant')
    b = Animal(1, 2, np.array([1,0]), 'Rhinoceros')
    b.move(1,4)
    a.rotate(np.array([-1, 0]))
    print(a.bearing(b))
    print(a, b)

