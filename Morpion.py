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
        self.matrix = self.createMatrix()
                
        
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
                    tab.append(Case(i,j))
                
        return tab
