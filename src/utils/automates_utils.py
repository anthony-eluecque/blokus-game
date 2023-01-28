from random import randint
from models.Player import Player
from models.Plateau import Plateau
from utils.game_utils import validPlacement,coordsBlocs,getDiagonals,getAdjacents


def pickPiece(joueur:Player)->int:
    index = 100
    while index not in joueur.pieces.pieces_joueurs:
        index = randint(0,20)
    return index

def firstPlacement(plateau:Plateau,indiceJoueur):
    for i,ligne in enumerate(plateau.getTab()):
        for j,col in enumerate(ligne):
            if plateau.getTab()[i][j] == indiceJoueur:
                return False
    return True

def managePiece(joueur:Player,plateau:Plateau,x:int,y:int):

    checkIf = False
    idPiece = 0
    pieceBlokus = []

    while not checkIf: 
        idPiece =  pickPiece(joueur)
        piece = joueur.jouerPiece(idPiece)
        pieceBlokus = coordsBlocs(piece,x,y)
        checkIf = True
        # checkIf = validPlacement(piece,y,x,plateau,joueur)

    joueur.hasPlayedPiece(idPiece)
    return pieceBlokus

def adjacents(x,y,plateau:Plateau,indexJoueur:int):
    adjs = [[x-1,y],[x,y-1],[x,y+1],[x+1,y]]

    possibilites = []
    grille = plateau.getTab()

        
    if grille[adjs[0][0]][adjs[0][1]] != indexJoueur and grille[adjs[1][0]][adjs[1][1]] != indexJoueur:
        possibilites.append([adjs[0][0],adjs[1][1]])
    
    if grille[adjs[0][0]][adjs[0][1]] != indexJoueur and grille[adjs[2][0]][adjs[2][1]] != indexJoueur:
        possibilites.append([adjs[0][0],adjs[2][1]])
    
    if grille[adjs[3][0]][adjs[3][1]] != indexJoueur and grille[adjs[1][0]][adjs[1][1]] != indexJoueur:
        possibilites.append([adjs[3][0],adjs[1][1]])
    
    if grille[adjs[3][0]][adjs[3][1]] != indexJoueur and grille[adjs[2][0]][adjs[2][1]] != indexJoueur:
        possibilites.append([adjs[3][0],adjs[2][1]])
    
    return list(filter(lambda coords : 0<=coords[0]<=19 and 0<=coords[1]<=20,possibilites))



def getSquare(x,y):
    square =  [ 
        [[x-1,y-1],[x,y-1],[x-1,y]],    # Diagonale en haut à gauche
        [[x+1,y-1],[x,y-1],[x+1,y]],    # Diagonale en bas à gauche
        [[x+1,y+1],[x+1,y],[x,y+1]],    # Diagonale en bas à droite
        [[x-1,y+1],[x-1,y],[x,y+1]]     # Diagonale en haut à droite
    ]
    return square

def easy_automate(joueurActuel : Player,plateau : Plateau,index:int,view):

    cheminFichierPiece = "./media/pieces/" + joueurActuel.getCouleur().upper()[0] + "/1.png"

    possibilities = []

    if firstPlacement(plateau,index):
        x,y = joueurActuel.getPositionDepart()
    # else:
    #     placement  = availableCorners(index,plateau)

    #     x,y = placement[0]
    #     if len(placement) > 1:
    #         x,y = placement[randint(0,len(placement)-1)]

    pieceBlokus = managePiece(joueurActuel,plateau,x,y)

    coords = []
    for ypos,xpos in pieceBlokus:

        coords.append([ypos,xpos])

        view._addToGrid(cheminFichierPiece,xpos,ypos)
        plateau.setColorOfCase(ypos,xpos,index)

    
    for x,y in coords:
        temp = adjacents(x,y,plateau,index)
        if len(temp):
            possibilities.append(temp)

    print(possibilities)

    



