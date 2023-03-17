from random import randint
from models.Player import Player
from models.Plateau import Plateau
from utils.game_utils import validPlacement,coordsBlocs,getDiagonals,getAdjacents
from copy import deepcopy

def getPosScore( joueur: Player, plateau: Plateau, positions: list, pieceID: list, score: int, valPiece: int ) -> list[ dict ]:
    #for i in range( 3 ):
    #joueur.pieces.rotate( pieceID )
    newPositions: list[ dict ] = []

    for pos in positions:
        piece: list = joueur.jouerPiece( pieceID )
        canPlace = validPlacement( piece, pos[ 0 ], pos[ 1 ], plateau, joueur )

        if canPlace:
            if score > 0 and score < valPiece: newPositions[ "score" ] += valPiece
            else:
                newPositions.append( { 'x': pos[ 0 ], 'y': pos[ 1 ], 'score': valPiece, 'nbRota': 0, 'pieceID': pieceID } )
                    
            #joueur.pieces.resetRotation( pieceID )

    return newPositions

def predictPieces( joueur: Player, plateau: Plateau, positions: list, index: int ) -> dict:
    score: int = joueur.score
    pieces: list = joueur.pieces.pieces_joueurs

    possMin: dict = {}
    pieceScore: list[ dict ] = []

    for pieceID in pieces:
        valPiece: int = 0

        for row in joueur.jouerPiece( pieceID ):
            valPiece += row.count( 1 )

        pl: Plateau = deepcopy( plateau )

        for i in range( 3 ):
            if not len( pieceScore ):
                positions: list = getPossibilities( index, pl, joueur )

                for pieceSc in [ x for x in pieceScore if x.pieceID == pieceID ]:
                    pieceSc
            else:
                pieceScore.append( getPosScore( joueur, pl, positions, pieceID, 0, valPiece ) )

        for piecesPoss in pieceScore[ pieceID ]:
            if not possMin or possMin[ "score" ] > abs( score + piecesPoss[ "score" ] ):
                possMin = { 'x': piecesPoss[ "x" ], 'y': piecesPoss[ "y" ], 'score': score + valPiece, 'pieceID': pieceID, 'nbRota': 0 }

    return possMin

def managePiece(joueur:Player,plateau:Plateau, index: int )->list:
    positions: list = getPossibilities( index, plateau, joueur )

    if len( positions ) < 1:
        return -1

    possMin: list = predictPieces( joueur, plateau, positions, index )

    if len( possMin ) == 1:
        return -1
    else:
        idPiece: int = possMin[ 'pieceID' ]
        x: int = possMin[ 'x' ]
        y: int = possMin[ 'y' ]

        for _ in range( possMin[ "nbRota" ] ):
            joueur.pieces.rotate( idPiece )

        joueur.hasPlayedPiece( idPiece )
        #joueur.pieces.resetRotation( idPiece )
        return coordsBlocs( joueur.jouerPiece( idPiece ), y, x )

def adjacents( x, y, plateau: Plateau, indexJoueur: int ) -> list:
    adjs = [ [ x - 1, y ], [ x, y - 1 ], [ x, y + 1 ], [ x + 1, y ] ]

    possibilites = []
    grille = plateau.getTab()
    lg_grille: int = len( grille )
    
    if adjs[ 0 ][ 0 ] <= lg_grille and adjs[ 0 ][ 1 ] <= lg_grille and adjs[ 0 ][ 0 ] >= 0 and adjs[ 0 ][ 1 ] > 0:
        if adjs[ 1 ][ 0 ] <= lg_grille and adjs[ 1 ][ 1 ] <= lg_grille and adjs[ 1 ][ 0 ] >= 0 and adjs[ 1 ][ 1 ] >= 0:
            if grille[ adjs[ 0 ][ 0 ] ][ adjs[ 0 ][ 1 ] ] != indexJoueur and grille[ adjs[ 1 ][ 0 ] ][ adjs[ 1 ][ 1 ] ] != indexJoueur:
                possibilites.append( [ adjs[ 0 ][ 0 ], adjs[ 1 ][ 1 ] ] )
        
        if adjs[ 0 ][ 0 ] <= lg_grille and adjs[ 1 ][ 1 ] <= lg_grille and adjs[ 0 ][ 0 ] >= 0 and adjs[ 1 ][ 1 ] >= 0:
            if grille[ adjs[ 0 ][ 0 ] ][ adjs[ 2 ][ 1 ] ] != indexJoueur and grille[ adjs[ 2 ][ 0 ] ][ adjs[ 2 ][ 1 ] ] != indexJoueur:
                possibilites.append( [ adjs[ 0 ][ 0 ], adjs[ 2 ][ 1 ] ] )

    if adjs[ 3 ][ 0 ] <= lg_grille and adjs[ 3 ][ 1 ] <= lg_grille and adjs[ 3 ][ 0 ] >= 0 and adjs[ 3 ][ 1 ] >= 0:
        if adjs[ 1 ][ 0 ] <= lg_grille and adjs[ 1 ][ 1 ] <= lg_grille and adjs[ 1 ][ 0 ] >= 0 and adjs[ 1 ][ 1 ] >= 0:
            if grille[ adjs[ 3 ][ 0 ] ][ adjs[ 3 ][ 1 ] ] != indexJoueur and grille[ adjs[ 1 ][ 0 ] ][ adjs[ 1 ][ 1 ] ] != indexJoueur:
                possibilites.append( [ adjs[ 3 ][ 0 ], adjs[ 1 ][ 1 ] ] )
 
        if adjs[ 2 ][ 0 ] <= lg_grille and adjs[ 2 ][ 1 ] <= lg_grille and adjs[ 2 ][ 0 ] >= 0 and adjs[ 2 ][ 1 ] >= 0:
            if grille[ adjs[ 3 ][ 0 ] ][ adjs[ 3 ][ 1 ] ] != indexJoueur and grille[ adjs[ 2 ][ 0 ] ][ adjs[ 2 ][ 1 ] ] != indexJoueur:
                possibilites.append( [ adjs[ 3 ][ 0 ], adjs[ 2 ][ 1 ] ] )

    return list( filter( lambda coords: grille[ coords[ 0 ] ][ coords[ 1 ] ] != indexJoueur, possibilites ) )

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
    pieceBlokus = managePiece( joueurActuel ,plateau, index)

    if pieceBlokus != -1:
        for xpos,ypos in pieceBlokus:
            view._addToGrid(cheminFichierPiece,ypos,xpos)
            plateau.setColorOfCase(xpos,ypos,index)