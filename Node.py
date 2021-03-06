# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:58:58 2020

@author: Alexa
"""
from Morpion import Morpion
from Puissance4 import Puissance4

class Node:
    
    def __init__(self, value=None):
        self.nexts = []
        self.value = value
        
    def find(self,value,rang = 1,nbPointsCommuns=0,cpt=0,s=""):#look in this tree, if there is a node like value       
        # print('find:    rang=',rang, '    nbDiff=',nbDifference)
        # print(value)
        # print(self)
        if (rang == 0 and self.value.numberOfDifferences(value,False)==0 ):#difference de la hauteur dans l'arbre entre self et value       
            # print("s")
            # if nbPointsCommuns==9:
            # if (self.value.numberOfDifferences(value)==0):
            # print('Copy found:')
            # print('nbPointsCommuns=',nbPointsCommuns,'    cpt=',cpt, '   erreur?:',self.value.PointsCommuns(value,True,True))
            # print('last case ',s)
            # # print('last case',self.value.lastCase.x,'x ',self.value.lastCase.y,'y  -')
            # print(value)
            # print(self)
            # print()

            #     return self
            return self
        elif (rang>0): 
            # print('find:')
            # print(self.value)
            # self.afficheProchains()
            for n in self.nexts:
                value2 = n.value
                if not (isinstance(value2, int)):
                    nb = nbPointsCommuns + value2.PointsCommuns(value,True)
                    # print('Comparaisons: points communs=',nbPointsCommuns,'    rang=',rang, '   valide:',nb,'  ',nb!=0)
                    # print(value)
                    # print(value2)
                    
                    if (nb>nbPointsCommuns):
                        cpt+=1
                        val = n.find(value,rang-1,nb,cpt,s+str(value2.lastCase.x)+'x '+str(value2.lastCase.y)+'y  _  ')
                        if val is not None:
                            return val
        return None
    def find2(self,value,rang = 1,nbDifference=-1):#look in this tree, if there is a node like value
        if nbDifference ==-1:
            nbDifference=9

        # print('find:    rang=',rang, '    nbDiff=',nbDifference)
        # print(value)
        # print(self)
        if (rang == 0):#difference de la hauteur dans l'arbre entre self et value

            if nbDifference==0:
                # print('Copy found:')
                # print('last case',value.lastCase.x,' ',value.lastCase.y)
                # print(value)
                # print(self)
                return self
        elif (rang>0): 
            for n in self.nexts:
                value2 = n.value
                if not (isinstance(value2, int)):
                    nb = value2.numberOfDifferences(value,False)
                    # print('Comparaisons: differences=',nb)
                    # print(value)
                    # print(value2)
                    if (nbDifference>nb):
                        val = n.find2(value,rang-1,nb)
                        if val is not None:
                            return val
        return None

    def GetValue(self):#get the int value of the node
        if isinstance( self.value , int):
            return self.value
        else :
            count = 0
            for i in self.nexts:
                count += i.GetValue()
            return count

    def GetAllPossiblesValues(self,valPossibles = [0,0,0]):
        if isinstance( self.value , int):
            return self.value
        else :
            for i in self.nexts:
                val = i.GetAllPossiblesValues(valPossibles)
                if isinstance( val , int):
                    valPossibles[0 if val == 1 else (1 if val==-1 else 2)] +=1

            return valPossibles

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

        return self.nexts[indexe_MaxValue],nexts_values[i]

    def Min_LinkedNodeValue(self):  #return the node that has the smallest value
        nexts_values = self.GetAllValues()

        indexe_MaxValue = 0
        for i in range(1,len(nexts_values)):
            if nexts_values[indexe_MaxValue]>nexts_values[i]:
                indexe_MaxValue=i

        return self.nexts[indexe_MaxValue],nexts_values[i]

    def __str__(self):
        # return "Valeur totale: "+ str(self.GetValue())
        return str(self.value)
    def __repr__(self):
        return "Valeur totale: "+ str(self.GetValue())

    def gothrough(self):#enable to go through the tree
        node =self
        prev = []
        
        print('\nAppuyez sur (0) pour revenir, (.) pour sortir, et (1-9) pour choisir une case.')
        ipt = -1
        toutVal = self.GetAllPossiblesValues()
        print('rang: ',str(len(prev)+1),"  tour de: ",str("X" if self.value.lastP==self.value.VAL_J1 else "O"),"  valeur:",str(self.GetValue()),'     victoire de : J1=',str(toutVal[0]), '  J2=',str(toutVal[1]),'  personne=', str(toutVal[2])) #ligne toute a fait visible, ce commentaire sert juste a la ralonger. voila.
        self.afficheProchains() 
        ipt = input()
        while ipt != '.':
            #if touche valide
            if ipt == '0':
                node=prev.pop()
            else:
                prev.append(node)
                node =node.nexts[int(ipt)-1]
            toutVal = node.GetAllPossiblesValues([0,0,0]) #il faut repreciser la valeur du parametre! meme si il y a une valeur par defaut!!!
            print('rang: ',str(len(prev)+1),"  tour de: ",str("X" if node.value.lastP==node.value.VAL_J1 else "O"),"  valeur:",str(node.GetValue()),'     victoire de : J1=',str(toutVal[0]), '  J2=',str(toutVal[1]),'  personne=', str(toutVal[2])) #ligne toute a fait visible, ce commentaire sert juste a la ralonger. voila.
            node.afficheProchains() 
            ipt = input()

    def afficheProchains(self):#print all nexts nodes 
        taille = self.value.length if isinstance(self.value,Morpion )else self.value.lengthy
        lignes=[]
        for i in range(taille):
            lignes.append('l'+ str(i+1)+'  ')

        for n in self.nexts:
            val = n.value
            if isinstance (val,int):
                lignes[0]+='Etat :  '
                lignes[1]+=((str(val)+" ") if val>0 else (str(val)))+'      '
                lignes[2]+='      '
            elif isinstance (val,Morpion)or isinstance (val,Puissance4):#a voir
                s = val.toLines(separateurLignes ='I| ').split('I')
                for i in range(0,len(lignes)):
                    lignes[i]+=str(s[i+1])
            else:
                print ('Type inconnu: ',type(val))

        for ligne in lignes:
            print(ligne)