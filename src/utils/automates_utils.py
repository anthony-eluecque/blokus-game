from random import randint
from models.Player import Player
from models.Plateau import Plateau
from utils.game_utils import validPlacement,coordsBlocs,getDiagonals,getAdjacents
from copy import deepcopy

def pickPiece(joueur:Player)->int:
    index = 100
    while index not in joueur.pieces.pieces_joueurs:
        index = randint(0,20)
    return index


def managePiece(joueur:Player,plateau:Plateau,positions:list):

    choix = 0
    if len(positions) > 1:
        choix = randint(0,len(positions)-1)
    x,y = positions[choix]

    checkIf = False
    idPiece = 0
    piece = []
    print(f"Ce qui arrive en x : {x} et y : {y}")

    copyPieces = deepcopy(joueur.pieces.pieces_joueurs)
    # print(copyPieces)

    while not checkIf: 
        idPiece =  pickPiece(joueur)
        print(idPiece in copyPieces)
        if idPiece in copyPieces:
            copyPieces.remove(idPiece)
            print(copyPieces)
            piece = joueur.jouerPiece(idPiece)
            checkIf = validPlacement(piece,x,y,plateau,joueur)
        if not len(copyPieces):
            choix = 0
            if len(positions) > 1:
                choix = randint(0,len(positions)-1)
            x,y = positions[choix] 
            copyPieces = deepcopy(joueur.pieces.pieces_joueurs)

    joueur.hasPlayedPiece(idPiece)
    return coordsBlocs(piece,y,x)

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

    print("-------->",possibilities)
    # print("-------->",x,y)

    pieceBlokus = managePiece(joueurActuel,plateau,possibilities)

    for xpos,ypos in pieceBlokus:
        view._addToGrid(cheminFichierPiece,ypos,xpos)
        plateau.setColorOfCase(xpos,ypos,index)



