# -*- coding: utf-8 -*-
from Node import Node
from Morpion import Morpion
from Puissance4 import Puissance4
"""
essentials game methods :
 - toLines
 - numberOfDifferences
 - getState
 - createNexts
 - emptyCases


"""

class Arbre:
    def __init__(self, game):
        self.game = game
        self.node = Node(self.game())
        self.finDeBranches = 0
        self.nbSolutionTrouvee = 0
        self.cpt = 0
        self.generateNodeBranches(self.node)

    def generateNodeBranches(self,node,rang = 1):   # return a tree of nodes composed of all the possible different states of the game (Node class used)
                                                    #rang indique la hauteur du noeud dans l'arbre
        
        nodeState = node.value.getState()
        if (nodeState==0 and len(node.value.emptyCases())==0) or (nodeState!=0): # situation were the game ended 
            node.nexts= []
            node.nexts.append(Node(nodeState))
            self.finDeBranches+=1
        else:
            actionsPossibles = node.value.createNexts()
            nexts = [Node(action) for action in actionsPossibles]
            node.nexts=[]
            i=0
            for nxt in nexts:
                # print(nxt)
                copie = None # TODO: indicateur pour nombre de liaisons trouvees?
                if (rang <7):# hauteur maximale plus optimale (permet de gagner en vitesse)
                    copie = self.node.find(nxt.value,rang) # check in the already calculated tree if this situation was already calculated
                if copie is not None:
                    node.nexts.append(copie)
                else:
                    node.nexts.append(nxt)
                    self.generateNodeBranches(nxt,rang=rang+1)  # otherwise calculates the new values
                    
                
                if (rang==1):  #Indicateur de progretion de la recherche
                    valMax = 1
                    if (self.game is Puissance4):
                        valMax=node.value.lengthx*node.value.lengthy
                    elif (self.game is Morpion):
                        valMax=9
                    self.cpt+=1
                    i+=1
                    self.nbSolutionTrouvee+=self.fac(valMax-rang)
                    print(round(self.nbSolutionTrouvee/self.fac(valMax)*100),'%    nb de solutions trouvees: (',i,'-',self.cpt,') ',self.nbSolutionTrouvee)
            # print("Arbre")
            # print(node.value)
            # node.afficheProchains()

    def fac(self, n):
        """ factoriel """
        res = 1
        for i in range(1,n+1):
            res*=i
        return res  



    def __str__(self):
        return str(self.node)
