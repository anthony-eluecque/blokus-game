from random import randint
from models.Player import Player
from models.Plateau import Plateau
from utils.game_utils import validPlacement,coordsBlocs,getDiagonals


def pickPiece(joueur:Player)->int:
    index = -1
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
        checkIf = validPlacement(piece,y,x,plateau,joueur)

    joueur.hasPlayedPiece(idPiece)
    return pieceBlokus

def availableCorners(idJoueur:int,plateau:Plateau):

    corners = []
    for i,ligne in enumerate(plateau.getTab()):
        for j,col in enumerate(ligne):
            if plateau.getTab()[i][j]==idJoueur:
                corners.append(diagonals(i,j))

    return corners
    # return list(filter(lambda el:(0<=el[0]<=19 and 0<=el[1]<=19),corners))

def diagonals(x,y):
    return [
        [x-1,y-1],[x-1,y+1],
        [x+1,y-1],[x+1,y+1] 
    ]
            

def easy_automate(
    joueurActuel : Player,
    plateau : Plateau,index:int,view):

    cheminFichierPiece = "./media/pieces/" + joueurActuel.getCouleur().upper()[0] + "/1.png"
    print(availableCorners(index,plateau))

    if firstPlacement(plateau,index):
        print("Cas début de game")
        x,y = joueurActuel.getPositionDepart()
        pieceBlokus = managePiece(joueurActuel,plateau,x,y)
        for ypos,xpos in pieceBlokus:
            view._addToGrid(cheminFichierPiece,xpos,ypos)
            plateau.setColorOfCase(ypos,xpos,index)
    else:
        print("Cas générale")
        print(availableCorners(index,plateau))
    # print(plateau)
    return


