# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:24:35 2020

@author: Alexa
"""
import time
from Morpion import Morpion
from Minimax import MiniMax


print("Debut")
debutchrono = time.time()
mM = MiniMax(Morpion)
print('cpt: ', mM.arbre.compteur  ,'   fin de branches:', mM.arbre.finDeBranches)
finchrono = time.time()
print("Travail termine !     temps ecoule: ", str(round(finchrono - debutchrono, 3)))

mM.arbre.node.gothrough()
print("Fin")

#avec find 32 s   30%
#sans find 29 s   30%
