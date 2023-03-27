from models.Player import Player
from models.Plateau import Plateau
from utils.game_utils import validPlacement, coordsBlocs

# comment faire pour qu'une IA joue en fonction du coup qui lui rapportera le plus de point sur un plateau de jeu déjà valué en python 

def managePiece(joueur: Player, plateau: Plateau, positions: list ) -> list :
    """TODO"""
    ...

class Position:
    def __init__(self, x, y) -> None:
        self.left = [x, y-1]
        self.right = [x, y+1]
        self.top = [x-1, y]
        self.bottom = [x+1, y]

TAILLE = 20
class gameManager:

    @staticmethod
    def isInGrid(side: list)->bool:
        if side[0] <= TAILLE and side[1] <= TAILLE and side[0] >= 0 and side[1] >= 0:
            return True
        return False
    
    @staticmethod
    def iterateGrid(plateau: Plateau, indexJoueur: int):
        for i in range(len(plateau.getTab())):
            for j in range(len(plateau.getTab()[0])):
                if plateau.getTab()[i][j] == indexJoueur:
                    yield i,j

    @staticmethod
    def getBestPossibilities(plateau: Plateau, indexJoueur: int, joueur: Player):
        startPos = joueur.getPositionDepart()
        grid = plateau.getTab()
        if grid[startPos[0]][startPos[1]] != indexJoueur:
            return [startPos]
        
        possibilites = []
        for cell in gameManager.iterateGrid(plateau,indexJoueur):
            state = gameManager.getAdjacents(cell[0], cell[1], plateau, indexJoueur)
            if len(state):
                for pos in state:
                    possibilites.append(pos)
        return possibilites

    @staticmethod
    def valoriser_grille(plateau: Plateau) -> list:
        """TODO: faire jouer l'ia en fonction du score du plateau"""
        grille = plateau.getTab()

        centre_x = len(grille) // 2
        centre_y = len(grille[0]) // 2
        max_distance = max(centre_x, centre_y)
        valeurs = []
        for i in range(len(grille)):
            ligne = []
            for j in range(len(grille[0])):
                distance = abs(i - centre_x) + abs(j - centre_y)
                proportion_distance = 1 - (distance / max_distance)
                valeur = round((proportion_distance), 2)*10
                ligne.append(valeur)
            valeurs.append(ligne)
        return valeurs

    @staticmethod
    def canPlacePiece(numPiece: int, plateau: Plateau, x, y, joueur: Player) -> list:

        piece = joueur.jouerPiece(numPiece)
        checkIf = validPlacement(piece,x,y,plateau,joueur)

        if checkIf:
            return coordsBlocs(piece,x,y)
        return [-1, -1]

    @staticmethod
    def getAdjacents(x: int , y: int, plateau: Plateau, indexJoueur: int) ->list:
        possibilites = []
        grid = plateau.getTab()
        pos = Position(x,y)

        if gameManager.isInGrid(pos.left) and gameManager.isInGrid(pos.top):
            if grid[pos.left[0]][pos.left[1]] != indexJoueur and grid[pos.top[0]][pos.top[1]] != indexJoueur:
                possibilites.append([pos.left[0], pos.top[1]])

        if gameManager.isInGrid(pos.left) and gameManager.isInGrid(pos.right):
            if grid[pos.left[0]][pos.left[1]] != indexJoueur and grid[pos.right[0]][pos.right[1]] != indexJoueur:
                possibilites.append([pos.left[0], pos.right[1]])

        if gameManager.isInGrid(pos.bottom) and gameManager.isInGrid(pos.top):
            if grid[pos.bottom[0]][pos.bottom[1]] != indexJoueur and grid[pos.top[0]][pos.top[1]] != indexJoueur:
                possibilites.append([pos.bottom[0], pos.top[1]])
    
        if gameManager.isInGrid(pos.right) and gameManager.isInGrid(pos.bottom):
            if grid[pos.bottom[0]][pos.bottom[1]] != indexJoueur and grid[pos.right[0]][pos.right[1]] != indexJoueur:
                possibilites.append([pos.bottom[0],pos.right[1]])

        return list(filter(lambda coords: grid[coords[0]][coords[1]] != indexJoueur, possibilites))

def easy_automate(joueurActuel: Player, plateau: Plateau, index: int, view):

    cheminFichierPiece = "./media/pieces/" + joueurActuel.getCouleur().upper()[0] + "/1.png"

    possibilities = gameManager.getBestPossibilities(plateau, index, joueurActuel)
    pieceBlokus = managePiece(joueurActuel, plateau, possibilities)

    if pieceBlokus != -1:
        for xpos, ypos in pieceBlokus:
            view._addToGrid(cheminFichierPiece, ypos, xpos)
            plateau.setColorOfCase(xpos, ypos, index)

    print("/////////////////////////")
    print(gameManager.getBestPossibilities(plateau, index, joueurActuel))
    print("/////////////////////////")