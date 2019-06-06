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
from GamePieces import Animal, Boulder


class GameMap(list):
    """
        The Gamemap module
        ==================

        Creating the Gamemap.

        This creates the 5x5 gamemap with the moves and position of the gamepieces to play at the King of Siam. It is inherited from a list.

        :Example:
            >>> m = GameMap()

        .. seealso:: :class:`KingOfSiam.Animal()`, :class:`KingOfSiam.Boulder()`, :class:`KingOfSiam.Crosses()`
        .. moduleauthor:: Luca FAROLFI <luca.farolfi@ensta-bretagne.org>
    """

    def __init__(self):
        super().__init__()
        self.xmax = 5
        self.ymax = 5
        self.__nb_elephants = 0
        self.__nb_rhinoceros = 0
        self.nb_boulders = 0
        self.nb_crosses = 0
        self.playerTurn = "Elephant"
        self.winner = ""
        for k in range(self.ymax):
            y = []
            for i in range(self.ymax):
                y.append(0)
            self.append(y)
        for k in range(3):  # Setting up the 3 Boulders
            self[2][1+k] = Boulder(2, 1+k)
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
            This method add a new animal onto the board, with position and orientation
            It returns whether the placement was possible or not.

            :Args:
                :param animal (Animal): the animal to add on the GameMap.

            :Example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> g = GameMap()
                >>> g.add(a)

            .. note:: the turn does not count if the insertion was not possible
            .. warning:: if the location of the insertion is already taken by another piece, add calls upon move to see
            if insertion is possible
        """
        x, y = animal.coords
        if animal.species == 'Elephant' and self.__nb_elephants < 5 and (x == 0 or x == 4 or y == 0 or y == 4) and self[x][y] == 0:
            self[x][y] = animal
            self.__nb_elephants += 1
            self.playerTurn = "Rhinoceros"

        elif animal.species == 'Rhinoceros' and self.__nb_rhinoceros < 5 and (x == 0 or x == 4 or y == 0 or y == 4) and self[x][y] == 0:
            self[x][y] = animal
            self.__nb_rhinoceros += 1
            self.playerTurn = "Elephant"
        else:
            return False

    def delete(self, animal):
        """
            This method removes an animal from the board
            It reduces by one the number of animals of that species

            :Args:
                :param animal (Animal): the animal to delete.

            :Example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> g = GameMap()
                >>> g.delete(a)

            .. note:: if removal of a boulder, game ends?
            .. warning:: error if piece is not on the edge
        """
        x, y = animal.coords
        if x == 0 or x == 4 or y == 0 or y == 4:
            self[x][y] = 0
            if animal.species == 'Elephant':
                self.__nb_elephants -= 1
            elif animal.species == 'Rhinoceros':
                self.__nb_rhinoceros -= 1
            if self.playerTurn == "Elephant":
                self.playerTurn = "Rhinoceros"
            elif self.playerTurn == "Rhinoceros":
                self.playerTurn = "Elephant"
        else:
            return False

    def push_counter(self, x, y, cx, cy, counter = 1, k = 0):
        """
            This recursive method determines if a push move is possible by counting the elements having to be pushed,
            and taking into account their orientation.
            It returns the number of pieces that are being pushed aswell as a counter. If the counter not negative, the push occurs.

            Args:
                :param x (int): is the abscissa of the current pawn,
                :param y (int): is the ordinate of the current pawn,
                :param cx (int): the direction of the move following the x-axis,
                :param cy (int): the direction of the move following the y-axis,
                :param counter (int): the sum of the scalar product of each animals in a row,
                :param k (int): the counter of pawns in a row.

            :Example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> g = GameMap()
                >>> g.push_counter(0, 1, 1, 0)

            .. note:: The function has a double use, as without it "move" wouldn't know how many pieces to move
            .. warning:: ...
            .. info:: An animal placed sideways does not impact a push, an opponent's animal in the right direction helps the push.
        """
        k += 1
        if not (0 <= (x+cx) <= 4 and 0 <= y+cy <= 4):
            return counter, k

        elif self[x + cx][y + cy] == 0:
            return counter, k

        elif isinstance(self[x + cx][y + cy], Animal):
            if self[x + cx][y + cy].direction @ + np.array([cx, cy]) == 1:
                counter += 1
            elif self[x + cx][y + cy].direction @ + np.array([cx, cy]) == -1:
                counter -= 2

        elif isinstance(self[x + cx][y + cy], Boulder):
            counter -= 1

        return self.push_counter(x + cx, y + cy, cx, cy, counter, k)

    def move(self, animal, ncoords, ndir):
        """
            This method moves an animal from on the board, as well as turns it
            If the coords to which the animal is moving are taken, the the animal pushes

            Args:
                :param animal (Animal): the animal to move,
                :param ncoords (Animal): the new coordinates of the animal,
                :param ndir (Animal): the new direction of the animal.

            :Example:
                >>> a = Animal(0, 1, np.array([0,1]), "Elephant")
                >>> g = GameMap()
                >>> g.move(a,(1,1),np.array([0,1]))

            .. note:: player turn does not change if move is not possible
            .. warning:: ...
            .. info:: it is possible to both rotate and move to another position in the same turn
        """
        x, y = animal.coords
        (nx, ny) = ncoords
        cx, cy = nx - x, ny - y
        if abs(cx) > 1 or abs(cy) > 1:
            return False
        elif self[nx][ny] != 0 and (cx == 0 and abs(cy) == 1 or abs(cx) == 1 and cy == 0) and (animal.direction[0] == cx and animal.direction[1] == cy):
            res = self.push_counter(x, y, cx, cy, 1)
            c = res[0]
            k = res[1]
            if c >= 0:
                for i in range(k, 0, -1):
                    if (x + i * cx) == -1 or (x + i * cx) == 5 or (y + i * cy) == -1 or (y + i * cy) == 5:
                        if isinstance(self[x + (i-1)*cx][y + (i-1)*cy], Animal):
                            self[x + (i-1)*cx][y + (i-1)*cy] = animal
                            if animal.species == 'Elephant':
                                self.__nb_elephants -= 1
                                self[x + (i-1)*cx][y + (i-1)*cy] = 0
                            elif animal.species == 'Rhinoceros':
                                self.__nb_rhinoceros -= 1
                                self[x + (i - 1) * cx][y + (i - 1) * cy] = 0
                        else:
                            self[x + (i - 1) * cx][y + (i - 1) * cy] = 0
                            for k in range(5):
                                if isinstance(self[x + (i - 1 - k) * cx][y + (i - 1 - k) * cy], Animal) and [self[x + (i - 1 - k) * cx][y + (i - 1 - k) * cy].direction[0], self[x + (i - 1 - k) * cx][y + (i - 1 - k) * cy].direction[1]] == [cx, cy]:
                                    self.winner=self[x + (i - 1 - k) * cx][y + (i - 1 - k) * cy].species
                                    print("winner is", self.winner)
                                    break
                    else:
                        self[x + i * cx][y + i * cy] = self[x + (i - 1) * cx][y + (i - 1) * cy]
                        self[x + (i - 1) * cx][y + (i - 1) * cy] = 0
                        self[x + i * cx][y + i * cy].coords = (x + i * cx, y + i * cy)

                if self.playerTurn == "Elephant":
                    self.playerTurn = "Rhinoceros"
                elif self.playerTurn == "Rhinoceros":
                    self.playerTurn = "Elephant"
            else:
                print("Push not possible")
                return (False)
        elif self[nx][ny] == 0 and (cx == 0 and abs(cy) == 1 or abs(cx) == 1 and cy == 0) or (cx == 0 and cy == 0):
            animal.coords = (nx, ny)
            animal.direction = ndir
            self[x][y] = 0
            self[nx][ny] = animal
            if self.playerTurn == "Elephant":
                self.playerTurn = "Rhinoceros"
            elif self.playerTurn == "Rhinoceros":
                self.playerTurn = "Elephant"
        else:
            return False

    def __str__(self):
        """
            Show the current state of the game board

            :return: the string with the characteristics of the board
            :rtype: str
        """
        s = ''
        for i in range(5):
            for j in range(5):
                ani = False
                if self[i][j] == 0:
                    s += ' 0  '
                elif self[i][j].species == 'Elephant':
                    s += ' E'
                    ani = True
                elif self[i][j].species == 'Rhinoceros':
                    s += ' R'
                    ani = True
                else:
                    s += ' B  '
                if ani:
                    if self[i][j].direction[0] == 0 and self[i][j].direction[1] == 1:
                        d = '> '
                    elif self[i][j].direction[0] == -1 and self[i][j].direction[1] == 0:
                        d = '∧ '
                    elif self[i][j].direction[0] == 0 and self[i][j].direction[1] == -1:
                        d = '< '
                    else:
                        d = '∨ '
                    s += d
            s += '\n \n'
        return s

    def save(self, fichier):
        """
            This method save a GameMap in a KingOfSiam file with the .kos extension.

            :Args:
                :param file (file object): is file in which to write.

            :Example:
                >>> g = GameMap()
                >>> file = open('save.kos', 'r')
                >>> g.load(file)

            .. note:: this method take in argument a file object.
        """
        boulders = []
        elephants = []
        rhinos = []
        for i in range(5):
            for j in range(5):
                if self[i][j]!= 0:
                    piece = self[i][j]
                    L = []
                    if not isinstance(self[i][j], Boulder):
                        L.append(self[i][j].direction[0])
                        L.append(self[i][j].direction[1])
                    if piece.species == "Elephant":
                        elephants.append("(" + str(i) + "," + str(j)+ ") : np.array(["+str(L[0])+ "," + str(L[1])+"])")
                    elif piece.species == "Rhinoceros":
                        rhinos.append("("+str(i)+"," +str(j)+ ") : np.array(["+str(L[0]) + "," + str(L[1])+"])")
                    elif isinstance(piece, Boulder):
                        boulders.append("(" + str(i) + "," + str(j) + ")")
        fichier.write("# King of Siam GameFile \n\nplayer_turn {\n    " + self.playerTurn + "\n}\n\n")
        fichier.write("Boulder {")
        for k in range(len(boulders)):
            fichier.write("\n    " + boulders[k] + ";")
        fichier.write("\n}\n\nElephant {")
        for elt in elephants:
            fichier.write("\n    " + elt + ";")
        fichier.write("\n}\n\nRhinoceros {")
        for elt in rhinos:
            fichier.write("\n    " + elt + ";")
        fichier.write("\n}")

        fichier.close()

    def load(self, file):
        """
            This method load a KingOfSiam file with the .kos extension in a GameMap object.

            :Args:
                :param file (file object): is file to load.

            :Example:
                >>> g = GameMap()
                >>> file = open('save.kos', 'r')
                >>> g.load(file)

            .. note:: this method take in argument a file object.
        """
        for i in range(5):
            for j in range(5):
                self[i][j] = 0

        f = file.readlines()
        k = 0
        while k < len(f) and "Boulder {" not in f[k]:
            k += 1
        k += 1
        while ";" in f[k]:
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

if __name__ == '__main__':
    g = GameMap()
    print(g)