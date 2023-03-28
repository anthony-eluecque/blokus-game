from random import randint
from models.Player import Player
from models.Plateau import Plateau
from utils.game_utils import validPlacement, coordsBlocs, hasAdjacentSameSquare, isInGrid

def getSolutions( positions: list, joueur: Player, plateau: Plateau, score: int, x: int = -1, y: int = -1, firstPID: int = -1, firstRota: int = -1 ) -> list[ dict ]:
    poses: list[ dict ] = []
    pieces: list = joueur.pieces.pieces_joueurs
    
    for pos in positions:
        for pieceID in pieces:         
            for i in range( 4 ):
                piece: list = joueur.jouerPiece( pieceID )
                if i > 0: joueur.pieces.rotate( pieceID )
                canPlace = validPlacement( piece, pos[ 0 ], pos[ 1 ], plateau, joueur )
                
                if canPlace:
                    valPiece: int = 0

                    for row in piece:
                        valPiece += row.count( 1 )

                    poses.append( { 'x': pos[ 0 ], 'y': pos[ 1 ], 'score': score + valPiece, 'pieceID': pieceID, 'nbRota': i, 'firstX': x == -1 and pos[ 0 ] or x, 'firstY': y == -1 and pos[ 1 ] or y, 'firstPID': firstPID == -1 and pieceID or firstPID, 'firstRota': firstRota == -1 and i or firstRota } )
                            
            joueur.pieces.resetRotation( pieceID )
    return poses

def managePiece(joueur:Player,plateau:Plateau, index: int )->list:
    positions: list = getPossibilities( index, plateau, joueur )
    if len( positions ) < 1: return -1

    secTourPossibilities: list[ dict ] = []
    solutions: list[ dict ] = getSolutions( positions, joueur, plateau, 0 )
    secTourPossibilities = solutions
    # for pose in sorted( solutions, key = lambda x: x[ "score" ] ):
    #     predictedPlate: Plateau = deepcopy( plateau )
    #     pieceBlokus = coordsBlocs( joueur.jouerPiece( pose[ "pieceID" ] ), pose[ "y" ], pose[ "x" ] )

    #     for _ in range( pose[ "nbRota" ] ):
    #         joueur.pieces.rotate( pose[ "pieceID" ] ) 

    #     if pieceBlokus != -1:
    #         for xpos,ypos in pieceBlokus:
    #             predictedPlate.setColorOfCase( xpos, ypos, index )

    #     joueur.pieces.pieces_joueurs.remove( pose[ "pieceID" ] )
    #     joueur.nb_piece -= 1

    #     possibilities = getPossibilities( index, predictedPlate, joueur )
    #     predictedFoundSoluces: list[ dict ] = getSolutions( possibilities, joueur, predictedPlate, pose[ "score" ], pose[ "x" ], pose[ "y" ], pose[ "pieceID" ], pose[ "nbRota" ] )
        
    #     joueur.pieces.resetRotation( pose[ "pieceID" ] )
    #     joueur.pieces.pieces_joueurs.append( pose[ "pieceID" ] )
    #     joueur.nb_piece += 1

    #     if len( predictedFoundSoluces ) > 0: secTourPossibilities += predictedFoundSoluces

    possMin: dict = sorted( secTourPossibilities, key = lambda x: x[ "score" ], reverse = True )

    if len( possMin ) == 0: return -1
    possMin = possMin[ 0 ]

    idPiece: int = possMin[ "firstPID" ]
    x: int = possMin[ "firstX" ]
    y: int = possMin[ "firstY" ]
    rota: int = possMin[ "firstRota" ]
    
    if x < 0:
        idPiece = possMin[ "pieceID" ]
        x = possMin[ "x" ]
        y = possMin[ "y" ]
        rota = possMin[ "nbRota" ]

    for _ in range( rota ):
        joueur.pieces.rotate( idPiece )

    joueur.hasPlayedPiece( idPiece )
    return ( coordsBlocs( joueur.jouerPiece( idPiece ), y, x ), idPiece )

class Position:
    def __init__( self, x, y ) -> None:
        self.left = [ x, y - 1 ]
        self.right = [ x, y + 1 ]
        self.top = [ x - 1, y ]
        self.bottom = [ x + 1, y ]

def adjacents( x:int , y:int, plateau:Plateau, joueur: Player ) -> list:
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

def easy_automate(joueurActuel : Player,plateau : Plateau,index:int,view):
    cheminFichierPiece = "./media/pieces/" + joueurActuel.getCouleur().upper()[0] + "/1.png"
    pieceBlokus, idPiece = managePiece(joueurActuel,plateau, index )

    if pieceBlokus != -1:
        for xpos,ypos in pieceBlokus:
            view._addToGrid(cheminFichierPiece,ypos,xpos)
            plateau.setColorOfCase(xpos,ypos,index)

    joueurActuel.pieces.resetRotation( idPiece )