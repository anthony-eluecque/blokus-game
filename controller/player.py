from typing_extensions import Self
from pieces import Pieces
from constants import POSITION_DEPART

class Player():

    def __init__(self: Self, couleur: str) -> None:
        self.couleur : str = couleur
        self.pieces : Pieces = Pieces(self.couleur[0])
        self.position_depart : list = POSITION_DEPART[couleur]

    def getCouleur(self: Self) -> str:
        """Retourne la couleur du joueur

        Returns:
            str: La couleur du joueur
        """
        return self.couleur

    def jouerPiece(self: Self, num_piece: int) -> list[int]:
        """Joue une pièce

        Args:
            num_piece (int): La pièce à jouer

        Returns:
            list[int]: La liste des pièces jouables
        """
        return self.pieces.getPiece(num_piece)
    
    def getPositionDepart(self)->list:
        return self.position_depart

    def getNbPieces(self)->int:
        return len(self.pieces)

    def __str__(self: Self) -> str:
        return("Le joueur " + self.couleur + " est en possession de " +  str(self.pieces.getNbPieces()) + " pièce(s).")


# ---- kind of test
if __name__ == "__main__":

    joueur = Player("Rouge")
    print(joueur.getPositionDepart())

