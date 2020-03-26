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
        self.s = self.node.value# s: valeur du jeu dans notre cas
    
    

    def Actions(self,s):  # listes les actions possibles
        return self.node.nexts

    def Result(self,s,a):  #applique l'action a dans l'etat s
        self.node = a

    def TerminalTest(self,s):  # test si s est terminal(fin de jeu)
        return len(self.node.nexts)==1 and isinstance( self.node.nexts[0],int)

    # def Utility(self):  # attribut une valeur a l'etat s (interet??)
    #     a=1     
    



    def minimax_decision(self, isMax=True):  # return de game state in the max node value
        if not self.TerminalTest:
            if isMax:
                self.max_value(self.Actions(self.node)) 
            else:
                self.mini_value(self.Actions(self.node)) 
        return self.node.value

    def max_value(self, state):  # node with de max value
        if not isinstance(state.value,int):
            state, val = state.Max_LinkedNodeValue()
            return self.mini_value(state)
        return state.value

    def mini_value(self, state):  # node with de min value
        if not isinstance(state.value,int):
            state, val = state.Max_LinkedNodeValue()
            return self.max_value(state)
        return state.value

    def __str__(self):
        return str(self.node)
 
   