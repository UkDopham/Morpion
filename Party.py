# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:38:42 2020

@author: Alexa
"""
from Minimax import Minimax



class party:
    
    def __init__(self, game, name, playerTurn = 1): #0 is IA 1 is Player 
        self.game = game
        self.count = 0
        self.name = name
        self.playerTurn = playerTurn
        self.mM = Minimax(game)
        
    def runParty(self):
        while not self.isFinished():
            if self.count%2 == self.playerTurn:
                self.playPlayer()
            else:
                self.playIA()
            self.count = self.count + 1
        print("Finished !")
                
        
    def playIA(self):
        self.mM.UpdateNode(self.game)
        self.mM.minimax_decision()
    
    def playPlayer(self):
        coord = self.visual()
        while not self.game.playerPlay(coord):
            print("error coord not correct ")
            coord = self.visual()
            
    def visual(self):
        print("it's your turn " + self.name)
        print(self.game)
        print()
        print("select action : ")
        coord = self.game.askCoord()
        return coord
    
        
    def isFinished(self):
        return self.game.isFinished()

