class Case:
    """  Une case du jeu du morpion """

    def __init__(self,x,y,val=0):
        self.x = x
        self.y = y
        self.val = val    #value of the case
    
    def __eq__(self,other):#used for comparing two instances of Morpion
        if isinstance(other,self.__class__):
            return self.val == other.val
        elif isinstance(other,int):
            return self.val == other
        else:
            return False
    def __ne__(self,other):
        return not self.__eq__(other)

    def getValue(self):#get val
        return self.val
    
    def getRow(self):#get x
        return self.x
    
    def getColumn(self):#get y
        return self.y

    def __str__(self):
        return str(self.val)+" "

    def __repr__(self):
        return str(self.val)
    
    def isFilled(self):
        return False if self.val == 0 else True
    
    def setValue(self, value):
        self.val = value