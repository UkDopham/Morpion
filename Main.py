# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:24:35 2020

@author: Alexa
"""
import time
from Morpion import Morpion
from Arbre import Arbre
from Minimax import Minimax
from Coord import Coord
from Party import Party

game = Party(Morpion, "liolio", )
game.runParty()

#avec find 32 s   30%
#sans find 29 s   30%

# test = Morpion()

# coord = inputUser(test)
# print(coord)