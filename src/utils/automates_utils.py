from random import randint
from models.Player import Player
from models.Plateau import Plateau
from utils.game_utils import isValidMove, coordsBlocs
from copy import deepcopy

def getSolutions( positions: list, joueur: Player, plateau: Plateau, score: int, x: int = -1, y: int = -1, firstPID: int = -1, firstRota: int = -1 ) -> list[ dict ]:
    poses: list[ dict ] = []
    pieces: list = joueur.pieces.pieces_joueurs
    
    for pos in positions:
        for pieceID in pieces:         
            for i in range( 4 ):
                if i > 0: joueur.pieces.rotate( pieceID )
                piece: list = joueur.jouerPiece( pieceID )

                canPlace = isValidMove( piece, pos[ 0 ], pos[ 1 ], plateau, joueur )
                if pieceID == 14 and i == 2: print( piece )
                
                if canPlace:
                    valPiece: int = 0

                    for row in piece:
                        valPiece += row.count( 1 )
                    
                    preRota: int = firstRota
                    if preRota == -1: preRota = i

                    prePID: int = firstPID
                    if prePID == -1: prePID = pieceID

                    preX: int = x
                    if preX == -1: preX = pos[ 0 ]

                    preY: int = y
                    if preY == -1: preY = pos[ 1 ]
                    
                    poses.append( { 'x': pos[ 0 ], 'y': pos[ 1 ], 'score': score + valPiece, 'pieceID': pieceID, 'nbRota': i, 'firstX': preX, 'firstY': preY, 'firstPID': prePID, 'firstRota': preRota } )

            joueur.pieces.resetRotation( pieceID )
    return poses

def managePiece(joueur:Player,plateau:Plateau, index: int )->list:
    positions: list = getPossibilities( index, plateau, joueur )
    if len( positions ) < 1: return -1

    secTourPossibilities: list[ dict ] = []
    solutions: list[ dict ] = getSolutions( positions, joueur, plateau, 0 )

    for pose in sorted( solutions, key = lambda x: x[ "score" ] ):
        predictedPlate: Plateau = deepcopy( plateau )
        pieceBlokus = coordsBlocs( joueur.jouerPiece( pose[ "pieceID" ] ), pose[ "y" ], pose[ "x" ] )

        for _ in range( pose[ "nbRota" ] ):
            joueur.pieces.rotate( pose[ "pieceID" ] ) 

        if pieceBlokus != -1:
            for xpos,ypos in pieceBlokus:
                predictedPlate.setColorOfCase( xpos, ypos, index )

        joueur.pieces.pieces_joueurs.remove( pose[ "pieceID" ] )
        joueur.nb_piece -= 1

        possibilities = getPossibilities( index, predictedPlate, joueur )
        predictedFoundSoluces: list[ dict ] = getSolutions( possibilities, joueur, predictedPlate, pose[ "score" ], pose[ "x" ], pose[ "y" ], pose[ "pieceID" ], pose[ "nbRota" ] )
        
        joueur.pieces.resetRotation( pose[ "pieceID" ] )
        joueur.pieces.pieces_joueurs.append( pose[ "pieceID" ] )
        joueur.nb_piece += 1

        if len( predictedFoundSoluces ) > 0: secTourPossibilities += predictedFoundSoluces

    possMin: dict = sorted( secTourPossibilities, key = lambda x: x[ "score" ], reverse = True )

    if len( possMin ) == 0: return -1
    possMin = possMin[ 0 ]

    idPiece: int = possMin[ "firstPID" ]
    x: int = possMin[ "firstX" ]
    y: int = possMin[ "firstY" ]
    rota: int = possMin[ "firstRota" ]
    
    if x == -1:
        idPiece = possMin[ "pieceID" ]
        x = possMin[ "x" ]
        y = possMin[ "y" ]
        rota = possMin[ "nbRota" ]

    for _ in range( rota ):
        joueur.pieces.rotate( idPiece )
    print( possMin )
    joueur.hasPlayedPiece( idPiece )
    return ( coordsBlocs( joueur.jouerPiece( idPiece ), y, x ), idPiece )

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
    tour = managePiece(joueurActuel,plateau, index )

    if tour != -1:
        pieceBlokus, idPiece = tour[ 0 ], tour[ 1 ]

        
        for xpos,ypos in pieceBlokus:
            view._addToGrid(cheminFichierPiece,ypos,xpos)
            plateau.setColorOfCase(xpos,ypos,index)

        joueurActuel.pieces.resetRotation( idPiece )