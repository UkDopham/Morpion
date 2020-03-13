# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:45:30 2020

@author: Alexa
"""
from Node import *


class MiniMax:
    def __init__(self, game):
        self.game = game
        self.node = Node(game.__init__())
        self.generateNodeBranches(self.node)
        self.state = self.node

    def generateNodeBranches(self,node):  # return a tree composed of all the possible different states of the game
        nodeState = node.value.getState()
        if (nodeState==0 and len(node.value.emptyCases())==0) or (nodeState!=0):
            node.nexts= [Node(nodeState)]
        else:
            actionsPossibles = node.value.createNexts()
            node.nexts = [Node(action) for action in actionsPossibles]

    def minimax_decision(self, state):  # return de game state in the max node value
        return self.max_value(state)

    def max_value(self, state):  # node with de max value
        return state.Max_LinkedNodeValue()

    def mini_value(self, state):  # node with de min value
        return state.Max_LinkedNodeValue()

