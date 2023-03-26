# Sur quoi je me base pour évaluer mon jeu :

#  Le nombre de pièce restante par joueur
# Chaque carré = +1
# Faut prioriser en premier les grosses pièces et au max
# vers le centre


def evaluateGame(grid,color):

    jeuScore = {"Bleu":0,"Rouge":0,"Jaune":0,"Vert":0}
    for i,row in enumerate(grid):
        for j,elem in enumerate(row):
            if elem!='X':
                if elem==0:
                    jeuScore["Bleu"] +=1
                elif elem==1:
                    jeuScore["Jaune"] +=1
                elif elem==2:
                    jeuScore["Vert"] +=1
                else:
                    jeuScore["Rouge"] +=1

    return jeuScore[color]

class Tree:

    def __init__(self,color,grid = []) -> None:
        
        self._color : str = color
        self._left : None|Tree = None
        self._right : None|Tree = None
        self._grid : None|list = grid
        self._value : int = evaluateGame(grid,self._color)

    def isLeaf(self) -> bool:
        return self._left == None and self._right == None
    
    def insertLeft(self, grid) -> None:
        if not self._left:
            self._left = Tree(self._color,grid)
    
    def insertRight(self, grid) -> None:
        if not self._right:
            self._right = Tree(self._color,grid)

    def playGame(self,grid,deep = 2) -> None:
        if deep>2 : ...
            
    

if __name__ == "__main__":
    t = Tree("Rouge",[[1,2,3,4]])
    t.insertLeft([[1,1,1,2,3]])
    t.insertRight([[1,1,1,2,3,3]])

    print(t._left._value)
    



    
    


    

