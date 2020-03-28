import time
from Morpion import Morpion
from Arbre import Arbre
from Minimax import Minimax
from Party import Party

game = Party(Morpion, "liolio")
game.runParty()

#avec find 32 s   30%
#sans find 29 s   30%

# test = Morpion()

# coord = inputUser(test)
# print(coord)

