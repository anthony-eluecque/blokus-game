from random import randint
from models.Player import Player
from models.Plateau import Plateau
from utils.game_utils import validPlacement, coordsBlocs
from copy import deepcopy

def getSolutions( positions: list, joueur: Player, plateau: Plateau, score: int, x: int = -1, y: int = -1, firstPID: int = -1, firstRota: int = -1 ) -> list[ dict ]:
    poses: list[ dict ] = []
    pieces: list = joueur.pieces.pieces_joueurs
    
    for pos in positions:
        for pieceID in pieces:         
            for i in range( 1 ):
                #if i > 0: joueur.pieces.rotate( pieceID )
                piece: list = joueur.jouerPiece( pieceID )
                canPlace = validPlacement( piece, pos[ 0 ], pos[ 1 ], plateau, joueur )
                
                if canPlace:
                    valPiece: int = 0

        for row in joueur.jouerPiece( pieceID ):
            valPiece += row.count( 1 )

                    poses.append( { 'x': pos[ 0 ], 'y': pos[ 1 ], 'score': score + valPiece, 'pieceID': pieceID, 'nbRota': i, 'firstX': x == -1 and pos[ 0 ] or x, 'firstY': y == -1 and pos[ 1 ] or y, 'firstPID': firstPID == -1 and pieceID or firstPID, 'firstRota': firstRota == -1 and i or firstRota } )
                            
            #joueur.pieces.resetRotation( pieceID )
    return poses

def managePiece(joueur:Player,plateau:Plateau,positions:list, index: int )->list:
    if len( positions ) < 1: return -1

    secTourPossibilities: list[ dict ] = []
    solutions: list[ dict ] = getSolutions( positions, joueur, plateau, 0 )
    
    for pose in sorted( solutions, key = lambda x: x[ "score" ] ):
        predictedPlate: Plateau = deepcopy( plateau )
        pieceBlokus = coordsBlocs( joueur.jouerPiece( pose[ "pieceID" ] ), pose[ "y" ], pose[ "x" ] )

        if pieceBlokus != -1:
            for xpos,ypos in pieceBlokus:
                predictedPlate.setColorOfCase( xpos, ypos, index )
        print( joueur.pieces.pieces_joueurs )
        joueur.pieces.pieces_joueurs.remove( pose[ "pieceID" ] )
        joueur.nb_piece -= 1

        possibilities = getPossibilities( index, predictedPlate, joueur )
        predictedFoundSoluces: list[ dict ] = getSolutions( possibilities, joueur, predictedPlate, pose[ "score" ], pose[ "x" ], pose[ "y" ], pose[ "pieceID" ], pose[ "nbRota" ] )

        joueur.pieces.pieces_joueurs.append( pose[ "pieceID" ] )
        joueur.nb_piece += 1

        if len( predictedFoundSoluces ) > 0: secTourPossibilities += predictedFoundSoluces

    possMin: dict = sorted( secTourPossibilities, key = lambda x: x[ "score" ], reverse = True )
    print( possMin )
    if len( possMin ) == 0: return -1
    possMin = possMin[ 0 ]

    idPiece: int = possMin[ "firstPID" ]
    if idPiece < 0: idPiece = possMin[ "pieceID" ]
    
    x: int = possMin[ "firstX" ]
    if x < 0: x = possMin[ "x" ]

    y: int = possMin[ "firstY" ]
    if y < 0: y = possMin[ "y" ]

    rota: int = possMin[ "firstRota" ]
    if rota < 0: rota = possMin[ "nbRota" ]

    print( x, y, rota, idPiece )

    for _ in range( rota ):
        joueur.pieces.rotate( idPiece )


    joueur.hasPlayedPiece( idPiece )
    #joueur.pieces.resetRotation( idPiece )
    return coordsBlocs( joueur.jouerPiece( idPiece ), y, x )

def adjacents( x, y, plateau: Plateau, indexJoueur: int ) -> list:
    adjs = [[x - 1, y], [x, y - 1], [x, y + 1], [x + 1, y]]
            # Top , Left , Right, Bottom
    possibilites = []
    grille = plateau.getTab()

    left = adjs[0];top = adjs[1]
    right = adjs[2];bottom = adjs[3]
    TAILLE : int = len(grille)

    def inGrid(side:list):
        if side[0] <= TAILLE and side[1] <= TAILLE and side[0] >= 0 and side[1] >= 0:
            return True
        return False
        
    
    if inGrid(left) and inGrid(top):
        if grille[left[0]][left[1]] != indexJoueur and grille[top[0]][top[1]] != indexJoueur:
            possibilites.append([left[0], top[1]])

    if inGrid(left) and inGrid(right):
        if grille[left[0]][left[1]] != indexJoueur and grille[right[0]][right[1]] != indexJoueur:
            possibilites.append([left[0], right[1]])

    if inGrid(bottom) and inGrid(top):
        if grille[bottom[0]][bottom[1]] != indexJoueur and grille[top[0]][top[1]] != indexJoueur:
            possibilites.append([bottom[0], top[1]])
 
    if inGrid(right) and inGrid(bottom):
        if grille[bottom[0]][bottom[1]] != indexJoueur and grille[right[0]][right[1]] != indexJoueur:
            possibilites.append([bottom[0],right[1]])

    return list( filter( lambda coords: grille[coords[0]][coords[1]] != indexJoueur, possibilites ) )

def easy_automate(joueurActuel : Player,plateau : Plateau,index:int,view):
    cheminFichierPiece = "./media/pieces/" + joueurActuel.getCouleur().upper()[0] + "/1.png"

    possibilities = getPossibilities(index,plateau,joueurActuel)
    pieceBlokus = managePiece(joueurActuel,plateau,possibilities, index )
    
    if pieceBlokus != -1:
        for xpos,ypos in pieceBlokus:
            view._addToGrid(cheminFichierPiece,ypos,xpos)
            plateau.setColorOfCase(xpos,ypos,index)