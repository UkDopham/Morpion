from Node import Node
from Arbre import Arbre
import time


class Minimax:
    MIN_VAL = -1000   #valeur minimale possible
    MAX_VAL =  1000   #valeur maximale possible

    def __init__(self, game):
        # generation de l'arbre des differents etats possibles
        debutchrono = time.time()
        self.arbre = Arbre(game)
        finchrono = time.time()
        print("Travail termine !     temps ecoule: ", str(round(finchrono - debutchrono, 3)))

        self.game = game
        self.node = self.arbre.node

    # no ->  node
    #  s ->  etat


    def Actions(self,no):
        """ liste des actions possibles  """
        return no.nexts

    # def Result(self,s,a):
    #     """ applique l'action dans l'etat s  """

    def TerminialTest(self,no): # MARCHE PAS
        """ test si s est terminal  """
        return len(no.nexts)==1 and isinstance(no.nexts[0],int)

    def Utility(self,no):
        """ recupere la valeur de s  """
        return no.nexts[0].value

    
    def Max(self,n1,n2):
        return n1 if n1>n2 else n2
    
    def Min(self,n1,n2):
        return n1 if n1<n2 else n2
   


    def Minimax_Decision(self, state,maximise = True,alphabeta=True):
        if state != self.node.value:
            self.node = self.node.find2(state)
        val = None
        if alphabeta:
            if maximise:
                print('MAXIMISE')
                self.node, val = self.MaxValueAB(self.node,self.MIN_VAL,self.MAX_VAL)
            else:
                print('MINIMISE')
                self.node, val = self.MinValueAB(self.node,self.MIN_VAL,self.MAX_VAL)
        
        else:                
            if maximise:
                print('MAXIMISE')
                self.node, val = self.MaxValue(self.node)
            else:
                print('MINIMISE')
                self.node, val = self.MinValue(self.node)
        print('val trouvee: ',val)
        return self.node.value


    def MaxValue(self,no,rang=0):
        if no.value.isFinished():
            return None,self.Utility(no)
        v = self.MIN_VAL
        node = None
        for n in self.Actions(no):
            nd, val = self.MinValue(n,rang+1)
            if val > v:
                node = n
            v = max(v,val)
        return node,v

    def MinValue(self,no,rang=0):
        if no.value.isFinished():
            return None, self.Utility(no)
        v = self.MAX_VAL
        node = None
        for n in self.Actions(no):
            nd, val = self.MaxValue(n,rang+1)
            if val < v:
                node = n
            v = min(v,val)
        return node,v




    def MaxValueAB(self,no,alpha,beta,rang=0):
        if no.value.isFinished():
            return None,self.Utility(no)
        v = self.MIN_VAL
        node = None
        for n in self.Actions(no):
            nd, val = self.MinValueAB(n,alpha,beta,rang+1)
            if val > v:
                node = n
            v = max(v,val)
            if v >= beta:
                return n,v
            alpha = max(alpha,v)
        return node,v

    def MinValueAB(self,no,alpha,beta,rang=0):
        if no.value.isFinished():
            return None, self.Utility(no)
        v = self.MAX_VAL
        node = None
        for n in self.Actions(no):
            nd, val = self.MaxValueAB(n,alpha,beta,rang+1)
            if val < v:
                node = n
            v = min(v,val)
            if v <= alpha:
                return n,v
            beta = min(beta,v)
        return node,v


