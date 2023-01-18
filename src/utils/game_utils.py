from models.Plateau import Plateau
from models.Player import Player
from constants import MAX_PIECES
import math

def hasAllPieces(player : Player)->bool:
    """Fonction permettant de vérifier si un joueur n'a pas encore joué
    sur le plateau

    Args:
        player (Player): Le joueur actuel

    Returns:
        bool: Vrai => Il a pas encore joué 
    """
    return True if player.getNbPieces()==MAX_PIECES else False

def isPositionDepart(cube_traite,player : Player)->bool:
    """Fonction permettant de vérifier si le joueur place 
    sa pièce à la première position (premier placement)

    Args:
        cube_traite (_type_): Le cube d'origine de la pièce
        player (Player): le joueur actuel

    Returns:
        bool: Vrai => Le joueur est bien sur sa position de départ
    """
    return True if player.getPositionDepart()==cube_traite else False

def verifTotalPieces(piece,plateau:Plateau,player:Player)->bool:
    """Fonction permettant de vérifier que tous les carrés de la pièce
    respectent les conditions du jeu blokus, sinon la pièce ne peut pas
    se poser.

    Args:
        piece (_type_): La pièce jouée par le joueur
        plateau (Plateau): Le plateau de jeu
        player (Player): Le joueur actuel

    Returns:
        bool: Vrai => Il peut jouer
    """
    for part_piece in piece:
            if part_piece[0]<0 or part_piece[0]>19 or part_piece[1]<0 or part_piece[1]>19:
                return False

            if not verifAroundCube(player,part_piece,plateau):
                return False
            
    return True
        
def notPieceBelow(piece,plateau:Plateau)->bool:
    """Fonction permettant de vérifier qu'une pièce ne va pas se poser sur une pièce
    existante

    Args:
        piece (_type_): La pièce jouée par le joueur
        plateau (Plateau): Le plateau de jeu

    Returns:
        bool: Vrai => La pièce peut être posé
    """
    for cube in piece:
        if not isInPlateau(cube):
            return False
        x = cube[0]
        y = cube[1]
        if plateau.getColorOfCase(x,y)!='empty':
            return False
    return True

def isInPlateau(cube : list)->bool:
    return True if 0<=cube[0]<20 and 0<=cube[1]<20 else False


def verifAroundCube(player:Player,cube,plateau:Plateau)->bool:
    """Fonction permettant de vérifier qu'un cube n'a pas un côté adjacent
    avec une pièce déjà existante

    Args:
        player (Player): le joueur actuel
        cube (_type_): le cube de la pièce 
        plateau (Plateau): le plateau de jeu

    Returns:
        bool: Vrai => La pièce peut être joué
    """
    adjacents = getSquare(cube)[1]
    for coords in adjacents:
        x = coords[0]
        y = coords[1]
        if plateau.getColorOfCase(x,y) == player.getCouleur()[0]: # Le [0] c'est pour récup que la première lettre*
            return False
    return True


def coordsBlocs(piece : list, col : int , row : int) -> list:
    """Donnes les coordonnées de chaque piece d'un bloc si celui-ci est != 0
       0 équivaut à un emplacement "vide"
       >>> coords_blocs([1,1],2,2)
       >>> [3,3]

    Args:
        piece (list): la pièce du bloc
        row (int): la ligne à l'origine du premier cube (permet une simulation de déplacement de cube)
        col (int): la colonne à l'origine du premier cube 

    Returns:
        list: nouvelles coordonées d'une pièce dans un bloc.
    """
    new_piece : list = []
    for y in range(len(piece)): # Longeur
        for x in range(len(piece[0])): # Largeur
            if piece[y][x]==1:
                new_piece.append([y+row,col+x])
    return new_piece


def validPlacement(bloc: list[int], row: int, col: int, plateau: Plateau, player:Player) -> bool:
    """Fonction permettant de vérifier si un bloc peut être placer sur le plateau.

    Args:
        bloc (list[list]): le bloc à positionner sur le plateau
        row (int): ligne de position à l'origine de la pièce
        col (int): colonne de position à l'origine de la pièce
        plateau (Plateau): plateau de jeu
        player (Player): Joueur

    Returns:
        bool: le bloc peut être ajouté au tableau
    """
    playerColor : str = player.getCouleur()[0]
    new_bloc : list = coordsBlocs(bloc,col,row)
    allPieces: bool = hasAllPieces(player)
    verifTotal: bool = verifTotalPieces(new_bloc,plateau,player)
    notBelow: bool = notPieceBelow(new_bloc,plateau)
    
    #  Cas ou le joueur n'a pas encore joué, et il va jouer sa première pièce
    for each_cube in new_bloc:
        if allPieces:
            if isPositionDepart(each_cube,player):
                if verifTotal:
                    return True
        # Les cas généraux 
        else:
            # print("Cas générale")
            if expectedPlayerInDiagonals(each_cube,plateau,playerColor):
                # print("Joueur diagonale")
                if notBelow:
                    # print("Pas de pièce en dessous")
                    if verifTotal:
                        # print("Vérif total pièce")
                        return True
    return False
    

def getSquare(piece: list) -> list[list]:
    """Obtenir toutes les positions autour d'un cube

    Args:
        piece (list): le cube du bloc

    Returns:
        list[list]: liste des positions autour du cube
    """
    return [list(filter(lambda el:(0<=el[0]<=19 and 0<=el[1]<=19),getDiagonals(piece))),
            list(filter(lambda el:(0<=el[0]<=19 and 0<=el[1]<=19),getAdjacents(piece)))]

def getDiagonals(piece: list) -> list[list]:
    """Obtenir toutes les diagonales autour d'un cube

    Args:
        piece (list): le cube du bloc

    Returns:
        list[list]: liste des diagonales autour du cube
    """
    return [
            [piece[0]-1,piece[1]-1],[piece[0]-1,piece[1]+1],  
            [piece[0]+1,piece[1]-1],[piece[0]+1,piece[1]+1]     
    ]

def getAdjacents(piece: list) -> list[list]:
    """Obtenir toutes les côtés adjacents autour d'un cube

    Args:
        piece (list): le cube du bloc

    Returns:
        list[list]: liste des adjacents autour du cube
    """
    return [
                                 [piece[0]-1,piece[1]],   
            [piece[0],piece[1]-1]         ,           [piece[0],piece[1]+1], 
                                 [piece[0]+1,piece[1]]   
    ]

def expectedPlayerInDiagonals(piece: list, plateau: Plateau, colorPlayer: str) -> bool:
    """Fonction permettant de savoir si il existe dans une des diagonales il existe un cube de la couleur
    correspondante au joueur actuel

    Args:
        piece (list): le cube du bloc à ajouter
        plateau (Plateau): le plateau de jeu
        colorPlayer (str): la couleur du joueur

    Returns:
        bool: Vrai : il existe dans l'une des diagonales un carré existant de la même couleur.
              Faux : l'inverse.
    """
    diagonals = getSquare(piece)[0]
    # print(colorPlayer,plateau.getColorOfCase())
    for y,x in diagonals:
        if plateau.getColorOfCase(y,x) == colorPlayer:
            return True
    return False

def playerCanPlay(player:Player,plateau:Plateau)->bool:
    """Permet de vérifier si un joueur est en capacité de jouer ou non.

    Args:
        player (Player): Le joueur actuel
        plateau (Plateau): Le plateau derrière l'affichage graphique

    Returns:
        bool: Vrai = Il peut jouer, Faux l'inverse
    """
    if not player.canplay: return False

    for indice_piece in player.pieces.pieces_joueurs:
        for i in range(0,20):
            for j in range(0,20):
                if validPlacement(player.pieces.liste_pieces[indice_piece],i,j,plateau,player):
                    print(f"La pièce n°{indice_piece+1} peut jouer en {i}-{j}")
                    return True
                if validPlacementRotation(indice_piece,i,j,plateau,player):
                    print(f"La pièce n°{indice_piece+1} peut jouer en {i}-{j} en étant rotate")
                    return True
                    
    player.canplay = False
    return False

def validPlacementRotation(indice_piece,i:int,j:int,plateau:Plateau,player:Player)->bool:
    """Fonction permettant de vérifier si un joueur est en capacité de jouer parmis les 4 rotations possibles d'une pièce

    Args:
        indice_piece (int): l'indice de la pièce 
        i (int): la position en i dans le tableau 
        j (int): la position en j dans le tableau
        plateau (Plateau): Le plateau de jeu 
        player (Player): Le joueur actuel

    Returns:
        bool: True = il peut jouer, False = Il ne peut pas
    """
    for _ in range(3):
        player.pieces.rotate(indice_piece)
        piece = player.jouerPiece(indice_piece)
        if validPlacement(piece,i,j,plateau,player):
            player.pieces.resetRotation(indice_piece)
            return True
    player.pieces.resetRotation(indice_piece)
    return False

def roundDown(n, decimals=2)->int:
    """Fonction permettant d'arrondir à l'inférieur pour notre jeu.

    Args:
        n : le nombre à arrondir à l'inférieur
        decimals (int, optional): l'arrondis à faire . Defaults to 2.

    Returns:
        int: le nombre arrondi
    """
    multiplier = 10 ** decimals
    result =  int(math.floor(n * multiplier) / multiplier)
    return (result//30)*30