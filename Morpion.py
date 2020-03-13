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
        
        
        
    def createMatrix(self, length): #Create the matrix with the length given in parameter
        matrix = []
        for i in range (0, length):
            row = []
            for j in range(0, length):
                row.append(0)
            matrix.append(row)
        
        return matrix
    
    
        
        