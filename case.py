class Case:
    """  Une case du jeu du morpion """

    def __init__(self,x,y,val=0):
        self.x = x
        self.y = y
        self.val = val    #value of the case
        
    def getValue(self):
        return self.val
    
    def getRow(self):
        return self.x
    
    def getColumn(self):
        return self.y