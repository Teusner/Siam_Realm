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

        .. seealso:: :class:`KingOfSiam.Boulder()`, :class:`KingOfSiam.Cross()`
    """
    def __init__(self, x, y, dir, species):
        self.__coords = x,y
        self.__direction = dir
        self.__species = species

    def bearing(self, animal):
        """
            This method get the orientation of an animal relative to another.
            It return the scalar product between the two direction vector of each animal.

            :Example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> b = Animal(0, 2, np.array([-1,0]), "Rhinoceros")
                >>> c = a.bearing(b)

            .. note:: this method return a number in  {-1, 0, 1}. 0 is when the vectors are orthogonal, 1 is when the animals are in the same direction and -1 is when the animals are facing each other.
        """
        dira, dirb = self.direction, animal.direction
        return dira @ dirb

    @property
    def coords(self):
        """
            This is the coordinates of the animal in a tuple.

            :Getter: Return the coordinates of the animal.
            :Setter: Set the coordinates of the animal.
            :Type: tuple of int

            :Getter's example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> c = a.coords

            :Setter's example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> a.coords = (0, 2)

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
            :Setter: Set the direction of the animal.
            :Type: numpy.array

            :Getter's example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> dir = a.direction

            :Setter's example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> a.direction = np.array([-1, 0])

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
            :Setter: Set the species of the animal.
            :Type: str

            :Getter's example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> s = a.species

            :Setter's example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> a.species = "Rhinoceros"

            .. warning:: the species should be "Elephant" or "Rhinoceros".
        """
        return self.__species

    @species.setter
    def species(self, nspecies):
        """
            Getting the species of the KingOfSiam.

            :param nspecies (str): which is the new species of the animal.
        """
        if nspecies in ['Elephant', 'Rhinoceros']:
            self.__species = nspecies

    def __str__(self):
        """
            Show the current state of an animal

            :return: the string with the characteristics of the animal
            :rtype: str
        """
        return self.__species + ' : [Position = ' + str(self.coords) + ' ; Direction = ' + str(self.direction) + ']\n'


class GameMap (list):
    """
        The Gamemap module
        ==================

        Creating the Gamemap.

        This creates the 5x5 gamemap with the moves and position of the gamepieces to play at the King of Siam. It is inherited from a list.

        :Example:
            >>> m = GameMap()

        .. seealso:: :class:`KingOfSiam.Animal()`, :class:`KingOfSiam.Boulder()`, :class:`KingOfSiam.Crosses()`
    """
    def __init__(self):
        self.xmax = 5
        self.ymax = 5
        self.__nb_elephants = 0
        self.__nb_rhinoceros = 0
        self.nb_boulders = 0
        self.nb_crosses = 0
        for k in range(self.ymax):
            y=[]
            for i in range(self.ymax):
                y.append(0)
            self.append(y)
        for k in range(3): # Setting up the 3 Boulders
            self[1+k][2]=Boulder(1+k, 2)
            self.nb_boulders += 1

    @property
    def nb_elephants(self):
        """
            This is the number of elephant on the gamemap.

            :Getter: Return the number of elephant on the gamemap.
            :Type: int

            :Getter's example:
                >>> m = GameMap()
                >>> print(m.nb_elephants)

            .. note:: The elephant's number can not exceed 5.
            .. warning:: the number of elephant can't be changed by hand.
        """
        return self.__nb_elephants

    @nb_elephants.setter
    def nb_elephants(self, nb_el):
        """
            Setting the elephant's number.
            .. warning:: the number of elephant can't be changed by hand.
        """
        print('Warning ! Changing the number of Elephant is not possible!')

    @property
    def nb_rhinoceros(self):
        """
            This is the number of rinoceros on the gamemap.

            :Getter: Return the number of rhinoceros on the gamemap.
            :Type: int

            :Getter's example:
                >>> m = GameMap()
                >>> print(m.nb_rhinoceros)

            .. note:: The rhinoceros's number can not exceed 5.
            .. warning:: the number of rhinoceros can't be changed by hand.
        """
        return self.__nb_rhinoceros

    @nb_rhinoceros.setter
    def nb_rhinoceros(self, x):
        """
            Setting the rhinoceros's number.
            .. warning:: the number of rhinoceros can't be changed by hand.
        """
        print('Warning ! Changing the number of Rhinoceros is not possible!')

    def add(self, KingOfSiam):
        x, y = KingOfSiam.coords
        if KingOfSiam.species == 'Elephant' and self.__nb_elephants < 5 and (x == 0 or x == 4 or y == 0 or y == 4) and self[x][y] == 0:
            self[x][y] = KingOfSiam
            self.__nb_elephants += 1
        elif KingOfSiam.species == 'Rhinoceros' and self.__nb_rhinoceros < 5 and (x == 0 or x == 4 or y == 0 or y == 4) and self[x][y] == 0:
            self[x][y] = KingOfSiam
            self.__nb_rhinoceros += 1
        else:
            return False

    def delete(self, KingOfSiam):
        x, y = KingOfSiam.coords
        if x == 0 or x == 4 or y == 0 or y == 4:
            self[x][y] = 0
            if KingOfSiam.species == 'Elephant':
                self.__nb_elephants -= 1
            elif KingOfSiam.species == 'Rhinoceros':
                self.__nb_rhinoceros -= 1
        else:
            return False

    def move(self, KingOfSiam, ncoords):
        x, y = KingOfSiam.coords
        nx, ny = ncoords
        cx, cy = nx-x, ny-y
        if self[nx][ny] == 0 and (cx == 0 and cy == 1 or cx == 1 and cy == 0):
            KingOfSiam.coords = (nx, ny)
            self[x][y] = 0
            self[nx][ny] = KingOfSiam

    def __str__(self):
        """
            Show the current state of the game board

            :return: the string with the characteristics of the board
            :rtype: str
        """
        s=''
        for j in range(5):
            for i in range(5):
                ani = False
                if self[i][j] == 0:
                   s+=' 0  '
                elif self[i][j].species == 'Elephant' :
                    s+=' E'
                    ani = True
                elif self[i][j].species == 'Rhinoceros':
                    s+=' R'
                    ani = True
                else :
                    s+=' B  '
                if ani :
                    if self[i][j].direction[0] == 1 and self[i][j].direction[1] == 0:
                        d='> '
                    elif self[i][j].direction[0] == 0 and self[i][j].direction[1] == 1:
                        d='∧ '
                    elif self[i][j].direction[0] == -1 and self[i][j].direction[1] == 0:
                        d='< '
                    else :
                        d='∨ '
                    s += d
            s+='\n \n'
        return s


class Boulder:
    """
        The Boulder module
        ==================

        This module creates a boulder at a position.

        :Args:
            :param x (int): is the abscissa of the boulder,
            :param y (int): is the ordinate of the boulder,
            :param species (str): is the species of this object. It can only take the values "Boulder" and is here to be used with polymorphism.

        :Example:
            >>> b = Boulder(1, 2)

        .. warning:: The coordinates should be on the 5x5 board game.
        .. seealso:: :class:`KingOfSiam.Animal()`, :class:`KingOfSiam.Cross()`
    """
    def __init__(self, x, y):
        self.coords = (x, y)
        self.species = 'Boulder'


class Cross:
    """
        The Cross module
        ================

        This module creates a cross at a position.

        :Args:
            :param x (int): is the abscissa of the cross,
            :param y (int): is the ordinate of the cross,
            :param species (str): is the species of this object. It can only take the values "Cross" and is here to be used with polymorphism.

        :Example:
            >>> b = Cross(1, 2)

        .. warning:: The coordinates should be on the 5x5 board game.
        .. seealso:: :class:`KingOfSiam.Animal()`, :class:`KingOfSiam.Boulder()`
    """
    def __init__(self, x, y):
        self.coords = (x, y)
        self.species = 'Cross'


if __name__ == '__main__':
    a = Animal(0, 2, np.array([1,0]), 'Elephant')
    b = Animal(1, 2, np.array([1,0]), 'Rhinoceros')
    b.move(1,4)
    a.rotate(np.array([-1, 0]))
    print(a.bearing(b))
    print(a, b)

