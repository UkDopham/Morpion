# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:38:42 2020

@author: Alexa
"""
from Minimax import Minimax
from Morpion import Morpion


class Party:
    VAL_J1 = 1
    VAL_J2 = 2
    
    def __init__(self, game, name, playerTurn = 0):
        self.game = game()
        self.count = 0
        self.name = name
        self.playerTurn = playerTurn

        self.val_Player = self.VAL_J2  
        self.val_IA = self.VAL_J2 if self.val_Player == self.VAL_J1 else self.VAL_J1

        valOfFirstToPlay = self.val_Player if playerTurn == 0 else self.val_IA
        self.mM = Minimax(game,playerTurn,valOfFirstToPlay == self.VAL_J2)
        
    def runParty(self):
        while not self.isFinished():
            print(self.game)
            if self.count%2 == self.playerTurn:
                self.playPlayer()
            else:
                print("ia play")
                self.playIA()
            self.count = self.count + 1
        print(self.game)
        print('You'if((self.count-1)%2 == self.playerTurn) else 'IA',' won!')
        print("Finished !")
                
        
    def playIA(self):
        self.game = self.mM.Minimax_Decision(self.game)

    
    def playPlayer(self):
        coord = self.visual()
        while self.game.getCase(coord).isFilled():
            print("error coord not correct ")
            coord = self.visual()
        self.game.getCase(coord).setValue(self.val_Player)    


    def visual(self):
        print("it's your turn " + self.name)    
        print()
        print("select action : ")
        coord = self.game.askCoord()
        return coord
    
        
    def isFinished(self):
        return self.game.isFinished()

