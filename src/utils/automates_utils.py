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

def managePiece(joueur:Player,plateau:Plateau,positions:list )->list:
    if len( positions ) < 1:
        return [ -1, -1 ]

    score: int = joueur.score

    pieces: list = joueur.pieces.pieces_joueurs

    possibilites: list = []

    for pos in positions:
        for pieceID in pieces:
            piece: list = joueur.jouerPiece( pieceID )
            canPlace = validPlacement( piece, pos[ 0 ], pos[ 1 ], plateau, joueur )

            if canPlace:
                valPiece: int = 0

                for row in piece:
                    valPiece += row.count( 1 )

                possibilites.append( { 'x': pos[ 0 ], 'y': pos[ 1 ], 'score': score + valPiece, 'pieceID': pieceID } )

    if len( possibilites ) < 1:
        return [ -1, -1 ]
    else:
        choix: dict = max( possibilites, key = lambda x: x[ 'score' ] )
        idPiece: int = choix[ 'pieceID' ]
        x: int = choix[ 'x' ]
        y: int = choix[ 'y' ]

        joueur.hasPlayedPiece( idPiece )
        return coordsBlocs( joueur.jouerPiece( idPiece ), y, x )

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
    pieceBlokus = managePiece(joueurActuel,plateau,possibilities)

    if pieceBlokus[ 0 ] != -1:
        for xpos,ypos in pieceBlokus:
            view._addToGrid(cheminFichierPiece,ypos,xpos)
            plateau.setColorOfCase(xpos,ypos,index)