from typing_extensions import Self
from pieces import Pieces
from controller.player import Player


class Plateau():

    def __init__(self : Self,rows : int,cols : int) -> None:
        self.tab : list[list] =  [['X']*rows for _ in range(cols)]
        self.colors = ["B","V","J","R"]

    def getCase(self : Self,row : int,col : int)->int:
        """Retourne une case spécifiée du plateau

        Args:
            row (int): Ligne du plateau
            col (int): Colonne du plateau

        Returns:
            int: La case voulue du plateau
        """
        return self.tab[row][col]

    def getColorOfCase(self: Self, row : int, col : int)->str:
        """Retourne la couleur d'une case spécifiée du plateau

        Args:
            row (int): Ligne du plateau
            col (int): Colonne du plateau

        Returns:
            str: Retourne la couleur de la case, empty si la case est vide
        """
        return self.colors[self.tab[row][col]] if self.tab[row][col]!="X" else "empty"

    def setColorOfCase(self: Self, row: int, col: int, statement: int) -> None:
        """Donne une couleur spécifiée à une case spécifiée du plateau

        Args:
            row (int): Ligne du plateau
            col (int): Colonne du plateau
            statement (int): Nouvelle couleur
        """
        
        # self.tab[row][col] = self.colors[statement]
        self.tab[row][col] = statement

    def isEmpty(self: Self, row: int, col: int ) -> bool:
        """Retourne si une case spécifiée du plateau est vide ou non

        Args:
            row (int): Ligne du plateau
            col (int): Colonne du plateau

        Returns:
            bool: Vrai: La case est vide
                  Faux: La case est remplie
        """
        
        return True if self.tab[row][col]==0 else False

    def getTab(self:Self)->list[list]:
        """Obtenir la list[list] du tableau

        Args:
            self (Self): l'objet Plateau

        Returns:
            list[list]: la liste de liste du plateau
        """
        return self.tab

    def __str__(self: Self) -> str:
        affichage_tab = ""
        for line in self.tab:
            affichage_tab+=str(line)+"\n"

        return affichage_tab