# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:58:58 2020

@author: Alexa
"""
from Morpion import Morpion

class Node:
    
    def __init__(self, value=None):
        self.nexts = []
        self.value = value
        
    def find(self,value,rang,nbDifference=9):#look in this tree, if there is a node like value
        if (rang == 0):#difference de l'hauteur dans l'arbre entre self et value

            if nbDifference==0:
                return self
        elif (rang>0): 
            for n in self.nexts:
                value2 = n.value
                if(isinstance(value2, Morpion)):
                    nb = value2.numberOfDifferences(value)
                    if (nbDifference>nb):
                        val = n.find(value,rang-1,nb)
                        if val is not None:
                            return val
        return None

    def GetValue(self):#get the int value of the node
        if isinstance( self.value , Morpion):
            count = 0
            for i in self.nexts:
                count += i.GetValue()
            return count
        else :
            return self.value
    
    def GetAllValues(self): # return an array contaning de value of each next node (the order is kept)
        nexts_values = []
        for node in self.nexts:
            nexts_values.append(node.GetValue())
        return nexts_values

    def Max_LinkedNodeValue(self):    #return the node that has the biggest value
        nexts_values = self.GetAllValues()

        indexe_MaxValue = 0
        for i in range(1,len(nexts_values)):
            if nexts_values[indexe_MaxValue]>nexts_values[i]:
                indexe_MaxValue=i

        return self.nexts[indexe_MaxValue]

    def Min_LinkedNodeValue(self):  #return the node that has the smallest value
        nexts_values = self.GetAllValues()

        indexe_MaxValue = 0
        for i in range(1,len(nexts_values)):
            if nexts_values[indexe_MaxValue]>nexts_values[i]:
                indexe_MaxValue=i

        return self.nexts[indexe_MaxValue]

    def __str__(self):
        # return "Valeur totale: "+ str(self.GetValue())
        return str(self.value)
    def __repr__(self):
        return "Valeur totale: "+ str(self.GetValue())

    def gothrough(self):#enable to go through the tree
        node =self
        prev = []
        
        print('Appuyez sur (0) pour revenir, et sur (.) pour sortir.')
        ipt = -1
        
        print('rang: ',str(len(prev)+1),"    valeur:",str(node.GetValue()))
        self.afficheProchains() 
        ipt = input()
        while ipt != '.':
            #if touche valide
            if ipt == '0':
                node=prev.pop()
            else:
                prev.append(node)
                node =node.nexts[int(ipt)-1]
            print('rang: ',str(len(prev)+1),"    valeur:",str(node.GetValue()))
            node.afficheProchains() 
            ipt = input()

    def afficheProchains(self):#print all nexts nodes 
        
        lignes=['l1  ','l2  ','l3  ']

        for n in self.nexts:
            val = n.value
            if isinstance (val,int):
                lignes[0]+='Etat :  '
                lignes[1]+=((str(val)+" ") if val>0 else (str(val)))+'      '
                lignes[2]+='      '
            elif isinstance (val,Morpion):
                s = val.toLines(separateurLignes ='I| ').split('I')
                for i in range(0,len(lignes)):
                    lignes[i]+=str(s[i+1])
            else:
                print ('Type inconnu: ',type(val))

        for ligne in lignes:
            print(ligne)