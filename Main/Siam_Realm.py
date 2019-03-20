#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from SiamRealm.gamemap import GameMap
from SiamRealm.animal import Animal



def turn(nbplayer):
    print("\n ####### Player ", nbplayer, " #######")
    print("1 - Put an animal on the board")
    print("2 - Move on a free cass")
    print("3 - Change the direction of an animal")
    print("4 - Take an animal off the board")
    choice = input("Type your choice : ")
    print('\n')
    return choice


''' Initialisation du plateau de jeu '''
m=Gamemap()

condSortie=False

# Player turn
Player1=False
Player2=False


while condSortie:

    # Player 1
    while Player1 :
        print(m)
        choice = turn(1)
        if choice == 1:
            while coords[0]:
            coords = input("Type the coords (x,y) : ")
        elif choice == 1:
        elif choice == 3:
        elif choice == 4: