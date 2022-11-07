from controller.plateau import Plateau
from controller.player import Player
from constants import MAX_PIECES


def coords_blocs(piece : list, row : int , col : int) -> list:
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

def valid_placement(bloc: list[list], row: int, col: int, plateau: Plateau, player:Player) -> bool:
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
    new_bloc : list = coords_blocs(bloc,row,col)
    for cube in new_bloc:
        if player.getNbPieces()==MAX_PIECES:
            if cube==player.getPositionDepart():
                return True
        pos_depart = player.getPositionDepart()
        if plateau.getColorOfCase(pos_depart[0],pos_depart[1]) == player.getCouleur()[0]:
            if expected_player_in_diagonals(cube,plateau,playerColor):
                for other_cube in new_bloc:
                    if other_cube[0]<0 or other_cube[0]>19 or other_cube[1]<0 or other_cube[1]>19:
                        return False
                    if other_cube!=cube:
                        square = get_square(other_cube)[1]
                        for coords in square:
                            if plateau.getColorOfCase(coords[0],coords[1]) == player.getCouleur()[0]:
                                return False
                return True
    return False
    
# Ajouter une vérif que toutes les pièces du bloc sont sur le plateau

def get_square(piece: list) -> list[list]:
    """Obtenir toutes les positions autour d'un cube

    Args:
        piece (list): le cube du bloc

    Returns:
        list[list]: liste des positions autour du cube
    """
    return [list(filter(lambda el:(0<=el[0]<=19 and 0<=el[1]<=19),get_diagonals(piece))),
            list(filter(lambda el:(0<=el[0]<=19 and 0<=el[1]<=19),get_adjacents(piece)))]

def get_diagonals(piece: list) -> list[list]:
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

def get_adjacents(piece: list) -> list[list]:
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

def expected_player_in_diagonals(piece: list, plateau: Plateau, colorPlayer: str) -> bool:
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
    diagonals = get_square(piece)[0]
    for y,x in diagonals:
        if plateau.getColorOfCase(y,x) == colorPlayer:
            return True
    return False

if __name__ == "__main__":

    tab = Plateau(20,20)
    joueur = Player("Vert")
    piece = joueur.jouerPiece(2)
    if valid_placement(piece,16,0,tab,joueur):
        new_bloc = coords_blocs(piece,16,0)
        for y,x in new_bloc:
            tab.setColorOfCase(y,x,1)
    joueur.pieces.rotate(2)
    piece = joueur.jouerPiece(2)
    if valid_placement(piece,14,2,tab,joueur):
            new_bloc = coords_blocs(piece,14,2)
            for y,x in new_bloc:
                tab.setColorOfCase(y,x,1)
    piece = joueur.jouerPiece(2)
    print(piece)
    if valid_placement(piece,12,3,tab,joueur):
            new_bloc = coords_blocs(piece,12,3)
            for y,x in new_bloc:
                tab.setColorOfCase(y,x,1)
    print(tab)
