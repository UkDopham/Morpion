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
        
    def showMatrix(self):
        for row in range(0, len(self.matrix)):
            rowContent = ""
            for column in range(0,len(self.matrix[row])):
                rowContent += str(self.matrix[row][column].getValue()) + " "
            print(rowContent)
            print("\n")
        
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
    
    def getStateValue(self):#return -1 if lost , 0 if even, 1 if win
        for row in range (0, len(self.matrix)):
            value = self.checkRow(row)
            if value != - 1:
                return value
        
        for column in range(0, len(self.matrix)):
            value = self.checkColumn(column)
            if value != -1:
                return value
        
        value = self.checkDiagonal(1)
        if value != -1:
            return value
        
        value = self.checkDiagonal(-1)
        if value != -1:
            return value

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
        tmp = column[0]
        for i in range(0, len(column)):
            if tmp != i:
                return -1
        return tmp
    
    def checkDiagonal(self, direction): #return the value of the winner if there is none return -1 , direction = -1 from up to bottom , 1 from bottom to up
        diagonal = []
        if direction == 1:
            for row in range(len(self.matrix), 0, -1):
                for column in range(0, len(self.matrix)):
                    if row == column:
                        diagonal.append(self.matrix[row][column])
        else :
            for row in range(0, len(self.matrix)):
                for column in range(0, len(self.matrix)):
                    if row == column:
                        diagonal.append(self.matrix[row][column])
        tmp = diagonal[0]
        for i in range(0, len(diagonal)):
            if tmp != i:
                return -1
        return tmp
        
