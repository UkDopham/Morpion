# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:45:30 2020

@author: Alexa
"""
from Node import Node
from Arbre import Arbre
"""
essentials game methods :
 - toLines
 - numberOfDifferences
 - getState
 - createNexts
 - emptyCases


"""

class MiniMax:
    def __init__(self, game):
        self.game = game
        self.arbre = Arbre(game)
        self.node = Node(self.arbre.node)

    
    # s: valeur du jeu dans notre cas

    # def Actions(s):  # listes les actions possibles
    # def Result(s,a):  #applique l'action a dans l'etat s
    # def TerminalTest(s):  # test si s est terminal(fin de jeu)
    # def Utility(s):  # attribut une valeur a l'etat s

    def minimax_decision(self, state):  # return de game state in the max node value
        return self.max_value(state)

    def max_value(self, state):  # node with de max value
        return state.Max_LinkedNodeValue()

    def mini_value(self, state):  # node with de min value
        return state.Max_LinkedNodeValue()

    def __str__(self):
        return str(self.node)
 
   