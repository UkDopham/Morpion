# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:26:32 2020

@author: Alexa
"""
from case import Case


class Morpion:
    VAL_J1 = 1
    VAL_J2 = 2
    
    def __init__(self, length=3, lastP = VAL_J2, matrix = None):
        self.length = length
        if matrix == None:            
            self.matrix = self.createMatrix()
        else:
            self.matrix = matrix
        self.lastP = lastP
        self.casesVides =self.emptyCases()  # diminue le cout en temps mais risque augmenter le cout en espace!! 
    
    def clone(self):
        tab =[]
        for i in range (0, self.length):
            row=[]
            for j in range(0, self.length):
                row.append(Case(i,j,self.matrix[i][j].val))
            tab.append(row)
        return Morpion(lastP= self.lastP,length= self.length,matrix= tab)


    def createNexts(self):
        nexts = []
        for caseVide in self.casesVides:
            nexts.append(self.playTurn(caseVide.x,caseVide.y,True))
        # for i in range(0, len(self.casesVides)):
        #     nexts.append(self.playTurn(i,True))
        return nexts


    def playTurn(self, i=0,j=0, createNewInstance=True): #simulate the play of the next player. createNewInstance=True will return a new instance of Morpion
        if not createNewInstance:
            self.lastP = (self.VAL_J1 if self.lastP == self.VAL_J2 else self.VAL_J2)
            self.matrix[i][j] = Case(i,j,self.lastP)
            self.casesVides = self.emptyCases()
        else:
            copie = self.clone()
            copie.playTurn(i,j,False)
            return copie
    
    def createMatrix(self): #Create the matrix with the length given in parameter
        matrix = []
        for i in range (0, self.length):
            row = []
            for j in range(0, self.length):
                row.append(Case(i,j))
            matrix.append(row)
        
        return matrix
    
    def emptyCases(self) : #Return an array contaning all the empty CASES of the MATRIX
        tab = []
        for i in range (0, self.length):
            for j in range(0, self.length):
                if self.matrix[i][j].val==0:
                    tab.append(self.matrix[i][j])
                
        return tab
    
    def getState(self): #return -1 if lost , 0 if even, 1 if win
        for row in range (0, len(self.matrix)):
            value = self.checkRow(row)
            if value != - 1:
                return 1 if value ==self.VAL_J1 else -1
        
        for column in range(0, len(self.matrix)):
            value = self.checkColumn(column)
            if value != -1:
                return 1 if value ==self.VAL_J1 else -1
        
        value = self.checkDiagonal(1)
        if value != -1:
            return 1 if value ==self.VAL_J1 else -1
        
        value = self.checkDiagonal(-1)
        if value != -1:
            return 1 if value ==self.VAL_J1 else -1
        
        return 0
    
    def checkRow(self, rowIndex): #return the value of the winner if there is none return -1
        row = self.matrix[rowIndex]
        tmp = row[0].val
        if tmp == 0:
            return -1
        for i in row:
        # for i in range(0, len(row)):
            if i != tmp:
                return -1
        return tmp
    
    def checkColumn(self, columnIndex): #return the value of the winner if there is none return -1
        column = []
        for i in range(0,len(self.matrix)):
            column.append(self.matrix[i][columnIndex]) #get the column value
        tmp = column[0].val
        if tmp == 0:
            return -1
        for i in column:
        # for i in range(0, len(column)):
            if i != tmp:
                return -1
        return tmp
   
    def checkDiagonal(self, direction): #return the value of the winner if there is none return -1 , direction = -1 from up to bottom , 1 from bottom to up
        diagonal = []

        for indexe in range(0, len(self.matrix)):
            diagonal.append(self.matrix[indexe][indexe if direction==1 else (self.length-indexe-1)]) 

        tmp = diagonal[0].val
        if tmp == 0:
            return -1

        for i in range(1,self.length):
            if tmp != diagonal[i].val:
                return -1
        return tmp


    def toLines(self, separateurLignes =''):  #return the values of the matrix in an string of three lines separated by 'separateurLignes'.   X = P1  O = P2  * = empty case
        s = separateurLignes
        for i in range(3):
            for j in range(3):
                s =s+ str("X" if self.matrix[i][j].val==self.VAL_J1 else ('O' if self.matrix[i][j].val==self.VAL_J2 else '*' )) + " "
            s+=separateurLignes
        return s

    def __str__(self): #return the values of the matrix in three separated lines.   X = P1  O = P2  * = empty case
        return self.toLines('\n')
        
    def GetMatrix(self):
        return self.matrix

    def __eq__(self,other): #used for comparing two instances of Morpion
        if isinstance(other,self.__class__):
            isEqual = True
            for x in range(0, self.length):
                for y in range(0, self.length):
                    isEqual = isEqual and (self.matrix[x][y] == other.matrix[x][y])
                    if not isEqual:
                        return isEqual
                    # print((self.matrix[x][y],'  ', other.matrix[x][y]),'  equal:',self.matrix[x][y] == other.matrix[x][y])
            # print('isEqual: ',isEqual)
            return isEqual
                    
        else:
            return False
    def __ne__(self,other): #same
        return not self.__eq__(other)

    def numberOfDifferences(self,other): #return the number of differences in two different instances of Morpion
        cpt=0
        for x in range(0, self.length):
            for y in range(0, self.length):
                if self.matrix[x][y] == other.matrix[x][y]:
                    cpt+=1
                
        return (self.length**2)-cpt
        