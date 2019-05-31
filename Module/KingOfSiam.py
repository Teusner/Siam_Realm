#!/usr/bin/env python
# -*- coding: utf-8 -*-


__author__ = "Brateaqu, Farolflu"
__copyright__ = "Copyright 2019"
__credits__ = ["Quentin BRATEAU", "Luca FAROLFI"]

__license__ = "GPL"
__version__ = "1.0"
__email__ = ["quentin.brateau@ensta-bretagne.org", "luca.farolfi@ensta-bretagne.org"]


# Importing modules
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
    def __init__(self, x, y, direction, species):
        self.__coords = x, y
        self.__direction = direction
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
        direction_1, direction_2 = self.direction, animal.direction
        return direction_1@direction_2

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
        nx, ny = ncoords
        if 0 <= nx <= 4 and 0 <= ny <= 4:
            self.__coords = nx, ny

    @property
    def direction(self):
        """
            This is the direction of the animal in a numpy.array. The direction is a unitary vector with a null coordinate.

            :Getter: Return the direction of the animal.
            :Setter: Set the direction of the animal.
            :Type: numpy.array

            :Getter's example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> d = a.direction

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
        if np.sqrt(ndir[0]**2+ndir[1]**2) == 1 and (ndir[0] == 0 or ndir[1] == 0) and ndir.size == 2:
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
        super().__init__()
        self.xmax = 5
        self.ymax = 5
        self.__nb_elephants = 0
        self.__nb_rhinoceros = 0
        self.nb_boulders = 0
        self.nb_crosses = 0
        for k in range(self.ymax):
            y = []
            for i in range(self.ymax):
                y.append(0)
            self.append(y)
        for k in range(3):  # Setting up the 3 Boulders
            self[1+k][2] = Boulder(1+k, 2)
            self.nb_boulders += 1

    @property
    def nb_elephants(self):
        """
            This is the number of elephant on the gamemap.

            :Getter: Return the number of elephant on the gamemap.
            :Type: int

            :Getter's example:
                >>> m = GameMap()
                >>> ne = m.nb_elephants

            .. note:: The elephant's number can not exceed 5.
            .. warning:: the number of elephant can't be changed by hand.
        """
        return self.__nb_elephants

    @nb_elephants.setter
    def nb_elephants(self, x):
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
                >>> nr = m.nb_rhinoceros

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

    def add(self, animal):
        """
            This method introduces a new animal onto the board, letting you decide the position and orientation
            It returns whether the placement was possible or not.

            :Example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> g = GameMap()
                >>> g.add(a)

            .. note:: the turn does not count if the insertion was not possible
            .. warning:: if the location of the insertion is already taken by another piece, add calls upon move to see
            if insertion is possible
            .. info:: ...
        """
        x, y = animal.coords
        if animal.species == 'Elephant' and self.__nb_elephants < 5 and (x == 0 or x == 4 or y == 0 or y == 4) and self[x][y] == 0:
            self[x][y] = animal
            self.__nb_elephants += 1
        elif animal.species == 'Rhinoceros' and self.__nb_rhinoceros < 5 and (x == 0 or x == 4 or y == 0 or y == 4) and self[x][y] == 0:
            self[x][y] = animal
            self.__nb_rhinoceros += 1
        else:
            return False

    def delete(self, animal):
        """
                    This method removes an animal from the board
                    It reduces by one the number of animals of that species

                    :Example:
                        >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                        >>> g = GameMap()
                        >>> g.delete(a)

                    .. note:: if removal of a boulder, game ends?
                    .. warning:: error if piece is not on the edge
                    .. info:: ...
        """
        x, y = animal.coords
        if x == 0 or x == 4 or y == 0 or y == 4:
            self[x][y] = 0
            if animal.species == 'Elephant':
                self.__nb_elephants -= 1
            elif animal.species == 'Rhinoceros':
                self.__nb_rhinoceros -= 1
        else:
            return False

    def push_counter(self, x, y, cx, cy, compteur=1,k=0):
        k+=1
        print('compteur=', k)
        #on étudie cas par cas selon la direction de la poussée, à simplifier car rien ne change sauf 2 premières lignes
        if self[x + cx][y + cy] == 0:
            print(compteur)
            return compteur
        elif isinstance(self[x+cx][y+cy], Animal):
            if cx * self[x+cx][y+cy].direction[0] + cy * self[x+cx][y+cy].direction[1] == 1:
                compteur += 1
            elif cx * self[x+cx][y+cy].direction[0] + cy * self[x+cx][y+cy].direction[1] == -1:
                compteur -= 2

        elif isinstance(self[x+cx][y+cy], Boulder):
            compteur -= 1

        return compteur, k, self.push_counter(x + cx, y + cy, cx, cy, compteur)



    def move(self, animal, ncoords, ndir):
        """
                    This method moves an animal from on the board, as well as turns it
                    If the coords to which the animal is moving are taken, the the animal pushes

                    :Example:
                        >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                        >>> g = GameMap()
                        >>> g.move(a,(1,1),np.array([0,1]))

                    .. note:: coords outside the board, it removes
                    .. warning:: error if push is not possible
                    .. info:: ...
                """
        x, y = animal.coords
        (nx,ny) = ncoords
        cx, cy = nx-x, ny-y
        if abs(cx) > 1 or abs(cy) > 1:
            return False
        elif (self[nx][ny] == 0 and (cx == 0 and abs(cy) == 1 or abs(cx) == 1 and cy == 0)) or (nx == x and ny == y):
            animal.coords = (nx, ny)
            animal.direction = ndir
            self[x][y] = 0
            self[nx][ny] = animal

        # Je pense que tu en as pas besoin car tu ne vas pas pousser les animaux avec move mais de case en case, il faut revoir toutess les utilisations de move dans la methode move qui ne doivent pas etre la

        elif nx < 0 or nx > 4 or ny < 0 or ny > 4:
            self.delete(animal)

        elif cx == 0 and abs(cy) == 1 or abs(cx) == 1 and cy == 0:
            c = self.push_counter(x, y, cx, cy, 1)[0]
            k = self.push_counter(x, y, cx, cy, 1)[1]
            if c >= 0:
                "move tous les elmts de 1 selon cx ou cy"
                for i in range(k, -1, -1):
                    self[x+(i+1)*cx][y+(i+1)*cy] = self[x+i*cx][y+i*cy]
                    self[x+i*cx][y+i*cy] = 0
        else:
            return False





    def rotate(self, animal, ndir):
        """
                    This method turns an animal without moving it

                    :Example:
                        >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                        >>> g = GameMap()
                        >>> g.rotate(a, np.array([-1,0]))

                    .. note:: ...
                    .. warning:: if coords don't correspond to a direction, it returns an error
                    .. info:: ...
                """

        x, y = animal.coords
        if ndir[0] == 0 and abs(ndir[1]) == 1 or ndir[0] == 1 and abs(ndir[1]) == 0:
            animal.direction = dir
            self[x][y] = animal

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
                   s += ' 0  '
                elif self[i][j].species == 'Elephant' :
                    s += ' E'
                    ani = True
                elif self[i][j].species == 'Rhinoceros':
                    s += ' R'
                    ani = True
                else:
                    s += ' B  '
                if ani:
                    if self[i][j].direction[0] == 1 and self[i][j].direction[1] == 0:
                        d = '> '
                    elif self[i][j].direction[0] == 0 and self[i][j].direction[1] == 1:
                        d = '∧ '
                    elif self[i][j].direction[0] == -1 and self[i][j].direction[1] == 0:
                        d = '< '
                    else:
                        d = '∨ '
                    s += d
            s += '\n \n'
        return s

    def load(self, fichier):
        for i in range(5):
            for j in range(5):
                self[i][j] = 0

        f = fichier.readlines()
        k = 0
        while k < len(f) and "Boulder {" not in f[k]:
            k += 1
        k += 1
        while ";" in f[k] :
            coords = f[k][5:8].split(",")
            x, y = int(coords[0]), int(coords[1])
            self[x][y] = Boulder(x, y)
            k += 1

        while k < len(f) and "Elephant {" not in f[k]:
            k += 1
        k += 1
        while ":" in f[k] and ";" in f[k]:
            coords = f[k][5:8].split(",")
            x, y = int(coords[0]), int(coords[1])
            d = f[k][22:].split("]")[0].split(",")
            xdir, ydir = 0, 0
            if d[0] == "1":
                xdir = 1
            elif d[0] == "-1":
                xdir = -1
            if d[1] == "1":
                ydir = 1
            elif d[1] == "-1":
                ydir = -1
            direction = np.array([xdir, ydir])
            self[x][y] = Animal(x, y, direction, 'Elephant')
            k += 1

        while k < len(f) and "Rhinoceros {" not in f[k]:
            k += 1
        k += 1
        while ":" in f[k] and ";" in f[k]:
            coords = f[k][5:8].split(",")
            x, y = int(coords[0]), int(coords[1])
            d = f[k][22:].split("]")[0].split(",")
            xdir, ydir = 0, 0
            if d[0] == "1":
                xdir = 1
            elif d[0] == "-1":
                xdir = -1
            if d[1] == "1":
                ydir = 1
            elif d[1] == "-1":
                ydir = -1
            direction = np.array([xdir, ydir])
            self[x][y] = Animal(x, y, direction, 'Rhinoceros')
            k += 1


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
    g = GameMap()
    #mon_fichier = open("../Saves/save.kos", "w")
    #mon_fichier.write("player_turn {\nelephant or rhino\n}\n\nBoulder {\n    (2,1);\n    (2,2);\n    (2,3);\n}"
    #                 "\n\nElephant {\n    (0,0) : np.array([0,1]);\n    (0,1) : np.array([0,-1]);\n  "
    #                  "  (0,2) : np.array([-1,0]);\n (0,3) : np.array([0,1]);\n    (0,4) : np.array([1,0]);\n}\n\n"
    #                  "Rhinoceros {\n    (1,0) : np.array([0,1]);\n    (1,1) : np.array([0,-1]);\n    (1,2) : "
    #                  "np.array([-1,0]);\n    (1,3) : np.array([0,1]);\n    (1,4) : np.array([1,0]);\n}")
    #mon_fichier.close()

    f = open('../Saves/save.kos')
    g.load(f)
    print(g)
