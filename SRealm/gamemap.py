#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
#from animal import Animal


class GameMap (list):
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
        for k in range(3):          # Setting up the 3 Boulders
            self[1+k][2]=Boulder((1+k, 2))
            self.nb_boulders += 1

    @property
    def nb_elephants(self):
        return self.__nb_elephants

    @nb_elephants.setter
    def nb_elephants(self, x):
        print('Warning ! Changing the number of Elephant is not possible!')

    @property
    def nb_rhinoceros(self):
        return self.__nb_rhinoceros

    @nb_rhinoceros.setter
    def nb_rhinoceros(self, x):
        print('Warning ! Changing the number of Rhinoceros is not possible!')

    def add(self, animal):
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
        x, y = animal.coords
        if x == 0 or x == 4 or y == 0 or y == 4:
            self[x][y] = 0
            if animal.species == 'Elephant':
                self.__nb_elephants -= 1
            elif animal.species == 'Rhinoceros':
                self.__nb_rhinoceros -= 1
        else:
            return False

    def move(self, animal, ncoords):
        x, y = animal.coords
        nx, ny = ncoords
        if self[nx][ny] == 0 and (nx-x ==0 ^ ny-y ==0):
            animal.coords = (nx,ny)
            self[nx][ny] = animal

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
                    s+=d
            s+='\n \n'
        return s


class Boulder:
    def __init__(self, coords):
        self.coords = coords
        self.species = 'Boulder'


if __name__ == '__main__':
    g=GameMap()
    #g.add(Animal(0, 0, np.array([1,0]), 'Rhinoceros'))
    #g.add(Animal(4, 2, np.array([1, 0]), 'Elephant'))
    print(g)
