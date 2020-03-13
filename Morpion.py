# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:26:32 2020

@author: Alexa
"""
from case import Case


class Morpion:
    VAL_J1 = 1
    VAL_J2 = 2
    
    def __init__(self, length=3):
        self.length = length
        self.actions = []
<<<<<<< HEAD
        self.matrix = self.createMatrix()
                
=======
        self.matrix = self.createMatrix(length)
        
    def __str__(self):
        content = ""
        for row in self.matrix:
            rowContent = ""
            for colmun in self.matrix[row]:
                rowContent
>>>>>>> 8c94550ede3f5f7da3594467686c17f708da70b7
        
    def createMatrix(self): #Create the matrix with the length given in parameter
        matrix = []
        for i in range (0, self.length):
            row = []
            for j in range(0, self.length):
                row.append(Case(i,j))
            matrix.append(row)
        
        return matrix
    
<<<<<<< HEAD
    def emptyCases(self) : #Return an array contaning all the empty CASES of the MATRIX
        tab = []
        for i in range (0, self.length):
            for j in range(0, self.length):
                if self.matrix[i][j].val==0:
                    tab.append(Case(i,j))
                
        return tab
=======
    def getStateValue(self):#return -1 if lost , 0 if even, 1 if win
        return 0
    
    def checkRow(self, rowIndex): #return the value of the winner if there is none return -1
        row = self.matrix[rowIndex]
        tmp = row[0]
        for i in range(0, len(row)):
            if tmp != i:
                return -1
        return tmp
    
    def checkColumn(self, columnIndex): #return the value of the winner if there is none return -1
        column = []
        for i in len(self.matrix):
            column.append(self.matrix[i][columnIndex]) #get the column value
    
        
>>>>>>> 8c94550ede3f5f7da3594467686c17f708da70b7
