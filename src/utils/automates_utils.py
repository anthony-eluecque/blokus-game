from models.Player import Player
from models.Plateau import Plateau
from utils.game_utils import validPlacement, coordsBlocs, isValidMove, isInGrid, hasAdjacentSameSquare
from copy import deepcopy

"""
TODO: 
1. Terminer l'adaptation de la fonction getSolution
2. Terminer la fonction managePiece
"""


def getSolutions(positions: list, joueur: Player, plateau: Plateau, x: int = -1, y: int = -1, firstRota: int = -1, firstReverse: int = -1) -> list[dict]:
    poses: list[dict] = []
    pieces: list = joueur.pieces.pieces_joueurs
    score: int = 0
    
    for pos in positions:
        for pieceID in pieces:
            for j in range(2):
                if j == 1: joueur.pieces.reverse(pieceID)

                for i in range(4):
                    if i > 0: joueur.pieces.rotate(pieceID)
                    piece: list = joueur.jouerPiece(pieceID)

                    canPlace = isValidMove(piece, pos[0], pos[1], plateau, joueur) # type: ignore
                    
                    if canPlace:
                        valPiece: int = 0

                        for row in piece:
                            # TODO: Simuler un coup et comptabiliser le score que celui ci apporte avec @valuateBoard
                            ...
                        
                        preReverse: int = firstReverse
                        if preReverse == -1: preReverse = j
                        
                        preRota: int = firstRota
                        if preRota == -1: preRota = i

                        preX: int = x
                        if preX == -1: preX = pos[0]

                        preY: int = y
                        if preY == -1: preY = pos[1]
                        
                        poses.append({'x': pos[0], 'y': pos[1], 'score': score + valPiece, 'pieceID': pieceID, 'nbRota': i, 'nbReverse': j, 'firstX': preX, 'firstY': preY, 'firstRota': preRota, 'firstReverse': preReverse})

            joueur.pieces.resetRotation( pieceID )
    return poses

def managePiece(joueur: Player, plateau: Plateau, positions: list) -> list:
    """TODO"""
    ...

def getPossibilities(indexJoueur: int, plateau: Plateau, joueur: Player) -> list:
    p = []
    grille = plateau.getTab()
    for i, ligne in enumerate(grille):
        for j, col in enumerate(ligne):
            if col == indexJoueur:
                possibilities = getAdjacents(i,j,plateau,joueur)
                if len(possibilities):
                    for _pos in possibilities:
                        p.append(_pos)
    if not len(p):
        return [joueur.getPositionDepart()]
    return p

def getAdjacents(x, y, plateau: Plateau, joueur: Player) -> list:
        possibilites = []
        
        if isInGrid(y - 1, x - 1):
            if not hasAdjacentSameSquare(plateau, joueur, x - 1, y - 1):
                possibilites.append([y - 1, x - 1])

        if isInGrid(y + 1, x - 1):
            if not hasAdjacentSameSquare(plateau, joueur, x - 1, y + 1):
                possibilites.append([y + 1 , x - 1])

        if isInGrid(y - 1, x + 1):
            if not hasAdjacentSameSquare(plateau, joueur, x + 1, y - 1):
                possibilites.append([y - 1 , x + 1])

        if isInGrid(y + 1, x + 1):
            if not hasAdjacentSameSquare(plateau, joueur, x + 1, y + 1):
                possibilites.append([y + 1, x + 1])

        return possibilites

def valuateBoard(plateau: Plateau) -> list[list[float]]:
    """Évalue le plateau en fonction de la distance de chaque case par rapport au centre

    Args:
        plateau (Plateau): Le plateau à valuer

    Returns:
        list[list[float]]: Le tableau de valeurs de chaque case du plateau
    """
    grille = plateau.getTab()

    centre_x, centre_y = len(grille) // 2, len(grille[0]) // 2
    max_distance = max(centre_x, centre_y)
    valeurs: list[list[float]] = []

    for i in range(len(grille)):
        ligne: list[float] = []

        for j in range(len(grille[0])):
            distance = abs(i - centre_x) + abs(j - centre_y)
            proportion_distance = 1 - (distance / max_distance)
            valeur = round((proportion_distance), 2)*10
            ligne.append(valeur)

        valeurs.append(ligne)
    return valeurs

def easy_automate(joueurActuel: Player, plateau: Plateau, index: int, view):
    cheminFichierPiece = "./media/pieces/" + joueurActuel.getCouleur().upper()[0] + "/1.png"

    possibilities = getPossibilities(index, plateau, joueurActuel)
    pieceBlokus = managePiece(joueurActuel, plateau, possibilities)

    if pieceBlokus != -1:
        for xpos, ypos in pieceBlokus:
            view._addToGrid(cheminFichierPiece, ypos, xpos)
            plateau.setColorOfCase(xpos, ypos, index)

    print("/////////////////////////")
    print(getPossibilities(index, plateau, joueurActuel))
    print("/////////////////////////")