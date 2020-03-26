# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:51:42 2020

@author: Alexa
"""
class Coord: 
    
    def __init__(self, row, column):
        self.row = row
        self.column = column

    def __str__(self):
        return str(self.row) + ':' + str(self.column)
    
    def getRow(self):
        return self.row
    
    def getColumn(self):
        return self.column