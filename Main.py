import time
from Morpion import Morpion
from Puissance4 import Puissance4
from Arbre import Arbre
from Minimax import Minimax
from Party import Party

game = Party(Morpion, "liolio",playerTurn=1)
# game = Party(Puissance4, "liolio") #ne marche pas encore 
game.runParty()



# m = Minimax(Puissance4)
# m.arbre.node.gothrough()

