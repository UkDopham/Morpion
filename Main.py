# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:24:35 2020

@author: Alexa
"""
import time
from Morpion import Morpion
from Arbre import Arbre
from Minimax import MiniMax
from Coord import Coord


def inputUser(morpion):
    print('A votre tour de jouer')
    print(morpion)
    row = int(input('row : '))
    column = int(input('column : '))
    return Coord(row, column)


print("Debut")
debutchrono = time.time()
mM = Arbre(Morpion)
finchrono = time.time()
print("Travail termine !     temps ecoule: ", str(round(finchrono - debutchrono, 3)))

mM.node.gothrough()
print("Fin")

#avec find 32 s   30%
#sans find 29 s   30%

# test = Morpion()

# coord = inputUser(test)
# print(coord)