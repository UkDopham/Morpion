# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:45:30 2020

@author: Alexa
"""
from Node import Node
from Arbre import Arbre
import time
"""
essentials game methods :
 - toLines
 - numberOfDifferences
 - getState
 - createNexts
 - emptyCases


"""


class Minimax:
    def __init__(self, game):
        debutchrono = time.time()
        self.arbre = Arbre(game)
        finchrono = time.time()
        print("Travail termine !     temps ecoule: ", str(round(finchrono - debutchrono, 3)))
        self.game = game
        self.node = self.arbre.node
        # self.node.gothrough()
        self.s = self.node.value# s: valeur du jeu dans notre cas
        # self.stop = False
    
    def UpdateNode(self,state):
        # print("Minimax UpdateNode: Enter")
        # print(self.node.value)
        # if self.node.value != state:
        # print("equal: ",state == self.node.value)
        # print("COMPARAISON: +++++++++++++++")
        # print(self.node.value)
        # print(state)
        # print('Different: ',state != self.node.value,'  -   -   -   -   -   -   -')
        if state != self.node.value:
            self.node = self.node.find2(state)
        # else:
        #     print('TTTTTTTTTTTTTTTTTTTTTTTTTTT')
        # print('Nouvelle matrice:',self.node.value)
        
        # print(self.node.value)
        # # self.node.gothrough()
        # print("Minimax UpdateNode: Out")

    def Actions(self,s):  # listes les actions possibles
        return s.nexts

    def Result(self,s,a):  #applique l'action a dans l'etat s
        self.node = a

    def TerminalTest(self):  # test si s est terminal(fin de jeu)
        return len(self.node.nexts)==1 and isinstance( self.node.nexts[0],int)

    # def Utility(self):  # attribut une valeur a l'etat s (interet??)
    #     a=1     
    



    def minimax_decision(self, isMax=True):  # return de game state in the max node value
        # if not self.TerminalTest():
        

        if not isMax:
            print('Max')
            self.node, val = self.alphabeta(self.node,-1000,1000) 
            print('minimax_decision: ',val)
        else:
            print('Min')
            self.node, val = self.alphabeta(self.node,-1000,1000, False) 
            print('minimax_decision: ',val)
        # self.stop=False
        return self.node.value

    def max_value(self, node,alpha,beta):  # node with de max value
        actions = self.Actions(node)
        # if not self.stop:
        #     print('node:',node.value)
        #     node.afficheProchains()
        #     self.stop = True
        # print('max_value: finished ? ',node.value.isFinished())
        # print(node)
        # print('Nombre de nexts: ',len(actions))
        # input()
        # if len(actions)>1 or not isinstance(actions[0].value,int):
        if not node.value.isFinished():
            maxVal = None
            maxValIndex = 0
            cpt = 0
            while len(actions)>cpt and (maxVal == None or maxVal > beta):
                next = actions[cpt]
                # print('next: ',next)

                node, val = self.mini_value(next,alpha,beta)

                if maxVal == None:
                    maxVal = val
                elif maxVal <val:
                    maxVal = val
                    maxValIndex = cpt
                
                cpt+=1
            # print('max_value: ',len(actions),' - ',maxVal)
            
            if val>beta:
                beta = maxVal
            return actions[maxValIndex], maxVal
        else:
            # print('returning: ',type(actions[0].value))
            return None, actions[0].value

    
    def mini_value(self, node,alpha,beta):  # node with de min value
        actions = self.Actions(node)
        # print('[',alpha,' , ',beta,']')
        # if not self.stop:
        #     print('node:',node.value)
        #     node.afficheProchains()
        #     self.stop = True
        # print('mini_value: finised ? ',node.value.isFinished())
        # print('Nombre de nexts: ',len(actions))
        # input()
        # if len(actions)>1 or not isinstance(actions[0].value,int):
        if not node.value.isFinished():
            minVal = None
            minValIndex = 0
            cpt = 0
            while len(actions)>cpt :
                next = actions[cpt]
                # print('next: ',next)
                node, val = self.max_value(next,alpha,beta)

                

                if minVal == None:
                    minVal = val
                elif minVal >val:
                    minVal = val
                    minValIndex = cpt
                
                cpt+=1
            # print('min_value: ',len(actions),' - ',minVal)
            
            return actions[minValIndex], minVal
        else:
            # print('returning: ',type(actions[0].value))
            return None, actions[0].value



    def max_valueAB(self, node,alpha,beta):
        # print('max_valueAB  [',alpha,',',beta,']')
        if node.value.isFinished():
            # print('val:',node.nexts[0].value)
            return None, node.nexts[0].value

        else:
            maxVal = 1000
            copyChild = None

            for child in self.Actions(node):
                copyChild = child
                nde, val = self.min_valueAB(child,alpha,beta)

                maxVal = min(maxVal, val)
                beta = min(beta,maxVal)

                if alpha>= beta:
                    # print('break')
                    break
            # print(type(copyChild))
            return copyChild,maxVal

    def min_valueAB(self, node,alpha,beta): 
        # print('min_valueAB  [',alpha,',',beta,']')
        if node.value.isFinished():
            # print('val:',node.nexts[0].value)
            return None, node.nexts[0].value

        else:
            minVal = -1000
            copyChild = None

            for child in self.Actions(node):
                copyChild = child
                nde, val = self.max_valueAB(child,alpha,beta)
                # print(type(nde))    
                minVal = max(minVal, val)
                alpha = max(alpha,minVal)

                if alpha>= beta:
                    # print('break')
                    break
            
            # print(type(copyChild))
            return copyChild,minVal

    def alphabeta(self, node,alpha,beta, maximizing=True): 

        if node.value.isFinished():
            return None, node.nexts[0].value

        if maximizing:
            minVal = -1000
            copyChild = None

            for child in self.Actions(node):
                copyChild = child
                nde, val = self.alphabeta(child,alpha,beta,False)
                minVal = max(minVal, val)
                alpha = max(alpha,minVal)

                if alpha >= beta:
                    return copyChild, minVal
            
            # print('alphabeta  [',alpha,',',beta,']   max=',maximizing)
            return copyChild,minVal
        else:
            maxVal = 1000
            copyChild = None

            for child in self.Actions(node):
                copyChild = child
                nde, val = self.alphabeta(child,alpha,beta,True)
                maxVal = min(maxVal, val)
                beta = min(beta,maxVal)

                if alpha >= beta:
                    return copyChild,maxVal
            
            # print('alphabeta  [',alpha,',',beta,']   max=',maximizing)
            return copyChild,maxVal


    def Max(self,n1,n2):
        return n1 if n1>n2 else n2
    
    def Min(self,n1,n2):
        return n1 if n1<n2 else n2
    
    def __str__(self):
        return str(self.node)
