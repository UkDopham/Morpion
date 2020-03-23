# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:45:30 2020

@author: Alexa
"""
from Node import Node
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
        self.node = Node(self.game())
        self.compteur = 0
        self.finDeBranches = 0
        self.generateNodeBranches(self.node)
        self.state = self.node
        self.cpt = 0

    def generateNodeBranches(self,node,rang = 1):   # return a tree of nodes composed of all the possible different states of the game (Node class used)
                                                    #rang indique la hauteur du noeud dans l'arbre
        #print for console
        self.compteur+=1
        if self.compteur%50000==0:  
            print('cpt: ',self.compteur, '    fin de branches:',self.finDeBranches)


        nodeState = node.value.getState()
        if (nodeState==0 and len(node.value.emptyCases())==0) or (nodeState!=0): # situation were the game ended 
            node.nexts= []
            node.nexts.append(Node(nodeState))
            self.finDeBranches+=1
        else:
            actionsPossibles = node.value.createNexts()
            nexts = [Node(action) for action in actionsPossibles]
            node.nexts=[]

            for nxt in nexts:
                copie = None # TODO: indicateur pour nombre de liaisons trouvees?
                if (rang < 6):# hauteur maximale plus optimale (permet de gagner en vitesse)
                    copie = self.node.find(nxt.value,rang) # check in the already calculated tree if this situation was already calculated
                if copie is not None:
                    node.nexts.append(copie)
                else:
                    node.nexts.append(nxt)
                    self.generateNodeBranches(nxt,rang=rang+1)  # otherwise calculates the new values



    def minimax_decision(self, state):  # return de game state in the max node value
        return self.max_value(state)

    def max_value(self, state):  # node with de max value
        return state.Max_LinkedNodeValue()

    def mini_value(self, state):  # node with de min value
        return state.Max_LinkedNodeValue()

    def __str__(self):
        return str(self.node)
 
   