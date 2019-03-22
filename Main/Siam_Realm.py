#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import SRealm.gamemap as gm
from SRealm.animal import Animal



def turn(nbplayer):
    print("\n ####### Player ", nbplayer, " #######")
    print("1 - Put an animal on the board")
    print("2 - Move on a free case")
    print("3 - Change the direction of an animal")
    print("4 - Take an animal off the board")
    choice = input("Type your choice : ")
    print('\n')
    return int(choice)


''' Initialisation du plateau de jeu '''
m = gm.GameMap()

condSortie=False

# Player turn
Player1=True


while not condSortie:

    # Show the board
    print(m)

    # Show the commands
    if Player1:
        choice = turn(1)
    else:
        choice = turn(2)

    # Processing the choice
    if choice == 1:
        c = input("Type the coords (x,y) : ")
        c = c.split(',')
        d = input("Type the direction np.array([x,y]) : ")
        x, y = int(c[0]), int(c[1])
        if Player1:
            a = Animal(x, y, dir, 'Elephant')
        else:
            a = Animal(x, y, dir, 'Rhinoceros')
        m.add(a)
    elif choice == 2:
        c = input("Type the actual coords (x,y) : ")
        c = c.split(',')
        nc = input("Type the new coords (nx,ny) : ")
        nc = nc.split(',')
        nc = int(nc[0]), int(nc[1])
        x, y = int(c[0]), int(c[1])
        m.move(m[x][y], nc)
    elif choice == 3:
        c = input("Type the coords (x,y) : ")
        c = c.split(',')
        d = input("Type the direction np.array([x,y]) : ")
        x, y = int(c[0]), int(c[1])
        m[x][y].rotate(d)
    elif choice == 4:
        c = input("Type the coords (x,y) : ")
        c = c.split(',')
        x, y = int(c[0]), int(c[1])
        m.delete(m[x][y])

    Player1 = not Player1