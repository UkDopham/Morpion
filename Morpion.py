# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:26:32 2020

@author: Alexa
"""

class Morpion:
    
    def __init__(self, length):
        self.length = length
        self.actions = []
        self.matrix = self.createMatrix(length)
        
    def __str__(self):
        content = ""
        for row in self.matrix:
            rowContent = ""
            for colmun in self.matrix[row]:
                rowContent
        
    def createMatrix(self, length): #Create the matrix with the length given in parameter
        matrix = []
        for i in range (0, length):
            row = []
            for j in range(0, length):
                row.append(0)
            matrix.append(row)
        
        return matrix
    
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
    
        