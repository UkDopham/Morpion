# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 12:58:58 2020

@author: Alexa
"""

class Node:
    
    def __init__(self):
        self.nexts = []
        self.value
        
    def GetValue(self):
        if len(self.nexts) !=  0:
            count = 0
            for i in self.nexts:
                count += i.GetValue()
            return count
        else :
            return self.value