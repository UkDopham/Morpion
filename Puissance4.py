from Case import Case

class Puissance4:
    VAL_J1 = 1
    VAL_J2 = 2
    
    def __init__(self, lengthx=4, lengthy=4,tailleCombi = 4,lastP = VAL_J2, matrix = None):
        self.lengthx = lengthx
        self.lengthy = lengthy
        self.tailleCombi = tailleCombi
        if matrix == None:            
            self.matrix = self.createMatrix()
        else:
            self.matrix = matrix
        self.lastP = lastP
        self.lastCase = None
        #self.casesVides =self.emptyCases()  # diminue le cout en temps mais risque augmenter le cout en espace!! 
    
    def clone(self):
        tab =[]
        for i in range (0, self.lengthx):
            row=[]
            for j in range(0, self.lengthy):
                row.append(Case(i,j,self.matrix[i][j].val))
            tab.append(row)
        return Puissance4(lastP= self.lastP,lengthx= self.lengthx,lengthy= self.lengthy,matrix= tab)


    def createNexts(self):
        nexts = []
        for colVide in self.notFullColumn():
            nexts.append(self.playTurn(colVide,True))
        return nexts

    def createNextsOld(self):
        nexts = []
        for caseVide in self.emptyCases():
            nexts.append(self.playTurnOld(caseVide.x,caseVide.y,True))
        # for i in range(0, len(self.casesVides)):
        #     nexts.append(self.playTurn(i,True))
        return nexts

    def PoseJeton(self, numColonne, value):
        coordy = self.lengthy-1
        for y in range(self.lengthy-1,-1,-1):
            if self.matrix[numColonne][y].isFilled():
                break
            coordy = y
        self.matrix[numColonne][coordy] = Case(numColonne,coordy,value)
        self.lastCase = Case(numColonne,coordy,value)

    def playTurn(self, y=0, createNewInstance=True): #simulate the play of the next player. createNewInstance=True will return a new instance of Puissance4
        if not createNewInstance:
            self.lastP = (self.VAL_J1 if self.lastP == self.VAL_J2 else self.VAL_J2)
            self.PoseJeton(y,self.lastP)
        else:
            copie = self.clone()
            copie.playTurn(y,False)
            return copie
   
    def playTurnOld(self, i=0,j=0, createNewInstance=True): #simulate the play of the next player. createNewInstance=True will return a new instance of Puissance4
        if not createNewInstance:
            self.lastP = (self.VAL_J1 if self.lastP == self.VAL_J2 else self.VAL_J2)
            self.matrix[i][j] = Case(i,j,self.lastP)
            self.lastCase = Case(i,j,self.lastP)
            #self.casesVides = self.emptyCases()
        else:
            copie = self.clone()
            copie.playTurnOld(i,j,False)
            return copie
    
    def createMatrix(self): #Create the matrix with the length given in parameter
        matrix = []
        for i in range (0, self.lengthx):
            row = []
            for j in range(0, self.lengthy):
                row.append(Case(i,j))
            matrix.append(row)
        
        return matrix
    
    def emptyCases(self) : #Return an array contaning all the empty CASES of the MATRIX
        tab = []
        for i in range (0, self.lengthx):
            for j in range(0, self.lengthy):
                if self.matrix[i][j].val==0:
                    tab.append(self.matrix[i][j])
                
        return tab
    
    def notFullColumn(self): # check all columns and return the indexes of the colums that are not full
        tab = []
        for x in range(self.lengthx):
                if not self.matrix[x][self.lengthy-1].isFilled():
                    tab.append(x)
        return tab

    def nextEmptyCase(self,column):
        for y in range(self.lengthy-1,-1,-1):
            if self.matrix[column][y].isFilled():
                break
            coordy = y
        return Case(column,y)

    def getState(self): #return -1 if lost , 0 if even, 1 if win
        #check all rows
        for x in range(0,self.lengthx-self.tailleCombi):
            for y in range(0,self.lengthy):
                value = self.checkRow(x,y)
                if value != - 1:
                    return 1 if value ==self.VAL_J1 else -1

        
        #check all columns
        for x in range(0,self.lengthx):
            for y in range(0,self.lengthy-self.tailleCombi):
                value = self.checkColumn(x,y)
                if value != - 1:
                    return 1 if value ==self.VAL_J1 else -1

        #check all diag 1
        for x in range(0,self.lengthx-self.tailleCombi):
            for y in range(0,self.lengthy-self.tailleCombi):
                value = self.checkDiagonal(x,y,1)
                if value != - 1:
                    return 1 if value ==self.VAL_J1 else -1

        #check all diag 2
        for x in range(0,self.lengthx-self.tailleCombi):
            for y in range(self.tailleCombi,self.lengthy):
                value = self.checkDiagonal(x,y,-1)
                if value != - 1:
                    return 1 if value ==self.VAL_J1 else -1
        return 0
    
    def checkRow(self, x,y): #return the value of the winner if there is none return -1
        """  x,y coordinate of the first case of the row"""
        tmp = self.matrix[x][y].val
        if tmp == 0:
            return -1
        for i in range(self.tailleCombi):
            if self.matrix[x+i][y].val != tmp:
                return -1
        return tmp
    
    def checkColumn(self,x,y): #return the value of the winner if there is none return -1
        tmp = self.matrix[x][y].val
        if tmp == 0:
            return -1
        for i in range(self.tailleCombi):
            if self.matrix[x][y+i].val != tmp:
                return -1
        return tmp
   
    def checkDiagonal(self,x,y, direction): #return the value of the winner if there is none return -1 , direction = -1 from up-left to bottom-rigth , 1 from bottom-left to up-rigth
        tmp = self.matrix[x][y].val
        if tmp == 0:
            return -1
        for i in range(self.tailleCombi):
            if self.matrix[x+i][y+direction*i].val != tmp:
                return -1
        return tmp


    def toLines(self, separateurLignes =''):  #return the values of the matrix in an string of three lines separated by 'separateurLignes'.   X = P1  O = P2  * = empty case
        s = separateurLignes
        for j in range(self.lengthy-1,-1,-1):
            for i in range(self.lengthx):
                s =s+ str("X" if self.matrix[i][j].val==self.VAL_J1 else ('O' if self.matrix[i][j].val==self.VAL_J2 else '*' )) + " "
            s+=separateurLignes
        return s

    def __str__(self): #return the values of the matrix in three separated lines.   X = P1  O = P2  * = empty case
        return self.toLines('\n')
        
    def __eq__(self,other): #used for comparing two instances of Puissance4
        if isinstance(other,self.__class__):
            isEqual = True
            for x in range(0, self.lengthx):
                for y in range(0, self.lengthy):
                    isEqual = (self.matrix[x][y] == other.matrix[x][y])
                    if not isEqual:
                        return isEqual
                    # print((self.matrix[x][y],'  ', other.matrix[x][y]),'  equal:',self.matrix[x][y] == other.matrix[x][y])
            # print('isEqual: ',isEqual)
            return isEqual
                    
        else:
            return False
    def __ne__(self,other): #same
        return not self.__eq__(other)

    def numberOfDifferences(self,other, lastCase=True): #return the number of differences in two different instances of Puissance4
        cpt=0
        if lastCase:
            if other.matrix[self.lastCase.x][self.lastCase.y] !=self.lastCase:
                cpt+=1
            else:
                cpt-=1

        else:
            for x in range(0, self.lengthx):
                for y in range(0, self.lengthy):
                    if self.matrix[x][y] != other.matrix[x][y]:
                        cpt+=1
        return cpt
    def PointsCommuns(self,other, lastCase=True, test=False): #return the number of differences in two different instances of Puissance4
        cpt=0
        if lastCase:
            if other.matrix[self.lastCase.x][self.lastCase.y].val ==self.lastCase.val:
                # if test:
                #     print('Erreur:')
                #     print('case diff ? ', other.matrix[self.lastCase.x][self.lastCase.y].val ==self.lastCase.val)
                #     print('val1:',other.matrix[self.lastCase.x][self.lastCase.y].val,'    val2:',self.lastCase.val)
                #     print('coord: x=',self.lastCase.x,'   y=',self.lastCase.y)
                #     print(other,self)
                cpt+=1
            

        else:
            for x in range(0, self.lengthx):
                for y in range(0, self.lengthy):
                    if self.matrix[x][y] == other.matrix[x][y]:
                        cpt+=1
        return cpt
    
    def askCoord(self):
        column = int(input("column ? :"))
        return column
    
    def isFinished(self):
        """ check if the game is finished  """
        state = self.getState()
        if ((state!=0  or state==0 and len(self.emptyCases())==0) ): # situation were the game ended
            return True
        else:
            return False
        
    def getCase(self,x,y=0):
        """ return the case, either with x="Case" or x="coordX", y="coordY"  """
        if isinstance(x,int):
            return self.matrix[x][self.nextEmptyCase(x).y]
        elif isinstance(x,Case):
            return self.matrix[x.x][x.y]

        
    def getMatrix(self):
        return self.matrix
                                                               
                                                              
    def invertPlayers(self):
        """  invert the values of player 1 and player 2 """
        for x in range(self.lengthx):                                   
            for y in range(self.lengthy):                                   
                if self.matrix[x][y] == self.VAL_J1:
                    self.matrix[x][y].setValue(self.VAL_J2)
                elif self.matrix[x][y] == self.VAL_J2:
                    self.matrix[x][y].setValue(self.VAL_J1)
                