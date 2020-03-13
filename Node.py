# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:58:58 2020

@author: Alexa
"""

class Node:
    
    def __init__(self, value=None):
        self.nexts = []
        self.value = value
        
    def GetValue(self):
        if len(self.nexts) !=  0:
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


        