from random import randint
from models.Player import Player
from models.Plateau import Plateau
from utils.game_utils import validPlacement,coordsBlocs,getDiagonals,getAdjacents


def pickPiece(joueur:Player)->int:
    index = 100
    while index not in joueur.pieces.pieces_joueurs:
        index = randint(0,20)
    return index


def managePiece(joueur:Player,plateau:Plateau,x:int,y:int):

    checkIf = False
    idPiece = 0
    piece = []

    while not checkIf: 
        idPiece =  pickPiece(joueur)
        piece = joueur.jouerPiece(idPiece)
        # checkIf = True
        checkIf = validPlacement(piece,y,x,plateau,joueur)

    joueur.hasPlayedPiece(idPiece)
    return coordsBlocs(piece,x,y)

def adjacents(x,y,plateau:Plateau,indexJoueur:int)->list:
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
    
    return list(filter(lambda coords : 0<=coords[0]<=19 and 0<=coords[1]<=20 and grille[coords[0]][coords[1]]!=indexJoueur,possibilites))

def getPossibilities(indexJoueur:int,plateau:Plateau,joueur:Player)->list:
    p = []
    grille = plateau.getTab()
    for i,ligne in enumerate(grille):
        for j,col in enumerate(ligne):
            if col == indexJoueur:
                possibilities = adjacents(i,j,plateau,indexJoueur)
                if len(possibilities):
                    for _pos in possibilities:
                        p.append(_pos)
    if not len(p):
        return [joueur.getPositionDepart()]
    return p

def easy_automate(joueurActuel : Player,plateau : Plateau,index:int,view):

    cheminFichierPiece = "./media/pieces/" + joueurActuel.getCouleur().upper()[0] + "/1.png"

    possibilities = getPossibilities(index,plateau,joueurActuel)

    choix = 0
    if len(possibilities) > 1:
        choix = randint(0,len(possibilities)-1)
    x,y = possibilities[choix]

    print("-------->",possibilities)
    print("-------->",x,y)

    pieceBlokus = managePiece(joueurActuel,plateau,x,y)

    for ypos,xpos in pieceBlokus:
        view._addToGrid(cheminFichierPiece,xpos,ypos)
        plateau.setColorOfCase(ypos,xpos,index)



