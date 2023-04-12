from models.Player import Player
from models.Plateau import Plateau
from utils.game_utils import isValidMove, coordsBlocs, isInGrid, hasAdjacentSameSquare
from copy import deepcopy
from models.Thread import PossibilityThread

def getSolutions( positions: list, joueur: Player, plateau: Plateau, score: int, x: int = -1, y: int = -1, firstPID: int = -1, firstRota: int = -1, firstReverse: int = -1 ) -> list[ dict ]:
    poses: list[ dict ] = []
    pieces: list = joueur.pieces.pieces_joueurs
    
    for pos in positions:
        for pieceID in pieces:
            for j in range( 2 ):
                if j == 1: joueur.pieces.reverse( pieceID )

                for i in range( 4 ):
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
                        
                        poses.append( { 'x': pos[ 0 ], 'y': pos[ 1 ], 'score': score + valPiece, 'pieceID': pieceID, 'nbRota': i, 'nbReverse': j, 'firstX': preX, 'firstY': preY, 'firstPID': prePID, 'firstRota': preRota, 'firstReverse': preReverse } )

            joueur.pieces.resetRotation( pieceID )
    return poses

def predictSolutions( plateau: Plateau, joueur: Player, index: int, solutions: list[ dict ] ) -> list:
    secTourPossibilities: list[ dict ] = []
    threads: list = []

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

        thread = PossibilityThread( possibilities, joueur, predictedPlate, pose[ "score" ], pose[ "x" ], pose[ "y" ], pose[ "pieceID" ], pose[ "nbRota" ], pose[ "nbReverse" ] )
        thread.start()
        threads.append( thread )

        joueur.pieces.resetRotation( pose[ "pieceID" ] )
        joueur.pieces.pieces_joueurs.append( pose[ "pieceID" ] )
        joueur.nb_piece += 1

    for thread in threads:
        thread.join()
        if len( thread.result ) > 0: secTourPossibilities += thread.result
        
    return secTourPossibilities

def managePiece(joueur:Player,plateau:Plateau, index: int )->list:
    positions: list = getPossibilities( index, plateau, joueur )
    if len( positions ) < 1: return -1

    solutions: list[ dict ] = getSolutions( positions, joueur, plateau, 0 )

    secTourPossibilities: list[ dict ] = predictSolutions( plateau, joueur, index, solutions )

    possMin: dict = sorted( secTourPossibilities, key = lambda x: x[ "score" ], reverse = True )

    if len( possMin ) == 0: return -1
    possMin = possMin[ 0 ]

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

def hardAutomate(joueurActuel : Player,plateau : Plateau,index:int,view,db):
    cheminFichierPiece = "./media/pieces/" + joueurActuel.getCouleur().upper()[0] + "/1.png"
    tour = managePiece( joueurActuel,plateau, index )

    if tour != -1:
        pieceBlokus, idPiece = tour[ 0 ], tour[ 1 ]

        
        for xpos,ypos in pieceBlokus:
            view._addToGrid(cheminFichierPiece,ypos,xpos)
            plateau.setColorOfCase(xpos,ypos,index)


        db.addPoints(joueurActuel.couleur,len(pieceBlokus))
        db.addToHistoriquePlayer(joueurActuel.couleur,pieceBlokus[0][0],pieceBlokus[0][1],idPiece,0,0)
        joueurActuel.pieces.resetRotation( idPiece )

    return tour != -1