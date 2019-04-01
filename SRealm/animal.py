#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


class Animal:
    """
        Creating an animal.

        This creates an animal with a position and a direction.

        :Args:
            :param x: is the abscissa of the animal,
            :type x: int,
            :param y: is the ordinate of the animal,
            :type y: int,
            :param dir: is the direction of the animal,
            :type dir: numpy.array,
            :param species: is the species of the animal. It can take only the values : "Elephant" or "Rhinoceros",
            :type car: car.

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
            Getting the coordinates of the animal.

            :Returns:
                :return coords: which are the coordinates of the animal,
                :rtype coords: tuple of int.

            :Example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> print(a.coords)

            .. seealso:: animal.direction(), animal.species()
        """
        return self.__coords

    @coords.setter
    def coords(self, ncoords):
        """
            Setting the coordinates or the animal. The coords should be

            :Args:
                :param ncoords: which are the new coords of the animal,
                :type ncoords: tuple of int.

            :Example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> a.coords((0, 2))

            .. seealso:: animal.direction(), animal.species()
        """
        nx,ny=ncoords
        if nx < 5 and ny < 5 :
            self.__coords = nx,ny

    @property
    def direction(self):
        """
            Getting the direction of the animal.

            :Returns:
                :return direction: which is the direction of the animal,
                :rtype direction: numpy.array.

            :Example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> print(a.direction)

            .. seealso:: animal.coords(), animal.species()
        """
        return self.__direction

    @direction.setter
    def direction(self, ndir):
        """
            Setting the direction of the animal. The direction is a unitary vector with a null coordinate.

            :Args:
                :param ndir: which is the new direction of the animal,
                :type ndir: tuple of int.

            :Example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> a.direction(np.array([-1, 0])

            .. seealso:: animal.coords(), animal.species()
        """
        if np.sqrt(ndir[0]**2+ndir[1]**2)==1 and (ndir[0]==0 or ndir[1]==0) :
            self.__direction = ndir

    @property
    def species(self):
        """
            Getting the species of the animal.

            :Returns:
                :return species: which is the direction of the animal,
                :rtype species: string.

            :Example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> print(a.species)

            .. seealso:: animal.coords(), animal.direction()
        """
        return self.__species

    @species.setter
    def species(self, nspecies):
        """
            Getting the direction of the animal. The direction is a unitary vector with a null coordinate.

            :Args:
                :param nspecies: which is the new species of the animal,
                :type nspecies: string.

            :Example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> a.species("Rhinoceros")

            .. seealso:: animal.coords(), animal.direction()
        """
        if nspecies in ['Elephant', 'Rhinoceros']:
            self.__species = nspecies

    def move(self, nx, ny):
        """
            Getting the direction of the animal. The direction is a unitary vector with a null coordinate.

            :Args:
                :param nspecies: which is the new species of the animal,
                :type nspecies: string.

            :Example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> a.move((0, 2))

            .. seealso:: animal.coords(), animal.direction()
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


if __name__ == '__main__':
    a = Animal(0, 2, np.array([1,0]), 'Elephant')
    b = Animal(1, 2, np.array([1,0]), 'Rhinoceros')
    b.move(1,4)
    a.rotate(np.array([-1, 0]))
    print(a.bearing(b))
    print(a, b)

