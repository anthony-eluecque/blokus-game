from models.Player import Player
from models.Plateau import Plateau
from utils.game_utils import isValidMove, coordsBlocs, isInGrid, hasAdjacentSameSquare
from copy import deepcopy
from queue import Queue
from threading import Thread
import asyncio
from random import randint
from time import time

def getSolucesSinglePiece( pieceID, joueur, plateau, score, x, y, firstPID, firstRota, firstReverse, pos, results ):
    # predicted = []
    for j in range( 1 ):
        if j == 1: joueur.pieces.reverse( pieceID )

        for i in range( 1 ):
            if i > 0: joueur.pieces.rotate( pieceID )
            piece: list = joueur.jouerPiece( pieceID )

            canPlace = isValidMove( piece, pos[ 0 ], pos[ 1 ], plateau, joueur )
            
            if canPlace:
                valPiece: int = 0
                
                for row in piece:
                    valPiece += row.count( 1 )
                
                preReverse: int = firstReverse
                if preReverse == -1: preReverse = j
                
                preRota: int = firstRota
                if preRota == -1: preRota = i

                prePID: int = firstPID
                if prePID == -1: prePID = pieceID

                preX: int = x
                if preX == -1: preX = pos[ 0 ]

                preY: int = y
                if preY == -1: preY = pos[ 1 ]
                results.put( [ { 'x': pos[ 0 ], 'y': pos[ 1 ], 'score': score + valPiece, 'pieceID': pieceID, 'nbRota': i, 'nbReverse': j, 'firstX': preX, 'firstY': preY, 'firstPID': prePID, 'firstRota': preRota, 'firstReverse': preReverse } ] )
                # predicted += [ { 'x': pos[ 0 ], 'y': pos[ 1 ], 'score': score + valPiece, 'pieceID': pieceID, 'nbRota': i, 'nbReverse': j, 'firstX': preX, 'firstY': preY, 'firstPID': prePID, 'firstRota': preRota, 'firstReverse': preReverse } ]
    # return predicted

def pieceSoluceThread( joueur, plateau, score, x, y, firstPID, firstRota, firstReverse, pos, results ):
    threads: list[ Thread ] = []
    pieces: list = joueur.pieces.pieces_joueurs

    for pieceID in pieces:
        thread = Thread( target = getSolucesSinglePiece, args = ( pieceID, joueur, plateau, score, x, y, firstPID, firstRota, firstReverse, pos, results ) )
        threads.append( thread )
        thread.start()
        # poses += getSolucesSinglePiece( pieceID, joueur, plateau, score, x, y, firstPID, firstRota, firstReverse, pos )
        joueur.pieces.resetRotation( pieceID )

    for thread in threads:
        thread.join( 0.12 )

def getSolutions( positions: list, joueur: Player, plateau: Plateau, score: int, x: int = -1, y: int = -1, firstPID: int = -1, firstRota: int = -1, firstReverse: int = -1 ) -> list[ dict ]:
    results: Queue = Queue()
    threads: list[ Thread ] = []
    poses: list[ dict ] = []

    for pos in positions: 
        process = Thread( target = pieceSoluceThread, args = ( joueur, plateau, score, x, y, firstPID, firstRota, firstReverse, pos, results ) )
        threads.append( process )
        process.start()
    
    for process in threads:
        process.join( 1.5 )

    while not results.empty():
        result = results.get()
        if not result: continue
        poses += result

    return poses

async def predictSolutions( plateau: Plateau, joueur: Player, index: int, solutions: list[ dict ] ) -> list:
    secTourPossibilities: list[ dict ] = []
    
    for pose in sorted( solutions, key = lambda x: x[ "score" ] ):
        predictedPlate: Plateau = deepcopy( plateau )
        pieceBlokus = coordsBlocs( joueur.jouerPiece( pose[ "pieceID" ] ), pose[ "y" ], pose[ "x" ] )

        for _ in range( pose[ "nbReverse" ] ):
            joueur.pieces.reverse( pose[ "pieceID" ] ) 

        for _ in range( pose[ "nbRota" ] ):
            joueur.pieces.rotate( pose[ "pieceID" ] ) 

        if pieceBlokus != -1:
            for xpos,ypos in pieceBlokus:
                predictedPlate.setColorOfCase( xpos, ypos, index )

        joueur.pieces.pieces_joueurs.remove( pose[ "pieceID" ] )
        joueur.nb_piece -= 1

        possibilities = getPossibilities( index, predictedPlate, joueur )
        predictedPoses = getSolutions( possibilities, joueur, predictedPlate, pose[ "score" ], pose[ "x" ], pose[ "y" ], pose[ "pieceID" ], pose[ "nbRota" ], pose[ "nbReverse" ] )

        if len( predictedPoses ) > 0: secTourPossibilities += predictedPoses

        joueur.pieces.resetRotation( pose[ "pieceID" ] )
        joueur.pieces.pieces_joueurs.append( pose[ "pieceID" ] )
        joueur.nb_piece += 1

    return secTourPossibilities

async def managePiece(joueur:Player,plateau:Plateau, index: int )->list:
    positions: list = getPossibilities( index, plateau, joueur )

    if len( positions ) < 1: return -1

    solutions: list[ dict ] = getSolutions( positions, joueur, plateau, 0 )
    secTourPossibilities: list[ dict ] = await predictSolutions( plateau, joueur, index, solutions )
    possMin: dict = sorted( secTourPossibilities, key = lambda x: x[ "score" ], reverse = True )

    if len( possMin ) == 0: return -1

    possMin = possMin[ randint( 0, min( 3, len( possMin ) - 1 ) ) ]

    idPiece: int = possMin[ "firstPID" ]
    x: int = possMin[ "firstX" ]
    y: int = possMin[ "firstY" ]
    rota: int = possMin[ "firstRota" ]
    reverse: int = possMin[ "firstReverse" ]
    
    if x == -1:
        idPiece = possMin[ "pieceID" ]
        x = possMin[ "x" ]
        y = possMin[ "y" ]
        rota = possMin[ "nbRota" ]
        reverse = possMin[ "nbReverse" ]

    for _ in range( reverse ):
        joueur.pieces.reverse( idPiece )

    for _ in range( rota ):
        joueur.pieces.rotate( idPiece )
        
    joueur.hasPlayedPiece( idPiece )
    return ( coordsBlocs( joueur.jouerPiece( idPiece ), y, x ), idPiece )

def adjacents(x,y,plateau:Plateau,joueur:Player)->list:
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

def getPossibilities(indexJoueur:int,plateau:Plateau,joueur:Player)->list:
    p = []
    grille = plateau.getTab()
    for i,ligne in enumerate(grille):
        for j,col in enumerate(ligne):
            if col == indexJoueur:
                possibilities = adjacents(i,j,plateau,joueur)
                if len(possibilities):
                    for _pos in possibilities:
                        p.append(_pos)
    if not len(p):
        return [joueur.getPositionDepart()]
    return p

async def hardAutomate(joueurActuel : Player,plateau : Plateau,index:int,view,db):
    cheminFichierPiece = "./media/pieces/" + joueurActuel.getCouleur().upper()[0] + "/1.png"
    tour = await managePiece( joueurActuel,plateau, index )

    if tour != -1:
        pieceBlokus, idPiece = tour[ 0 ], tour[ 1 ]

        for xpos,ypos in pieceBlokus:
            view._addToGrid(cheminFichierPiece,ypos,xpos)
            plateau.setColorOfCase(xpos,ypos,index)


        db.addPoints(joueurActuel.couleur,len(pieceBlokus))
        db.addToHistoriquePlayer(joueurActuel.couleur,pieceBlokus[0][0],pieceBlokus[0][1],idPiece,0,0)
        joueurActuel.pieces.resetRotation( idPiece )

    return tour != -1