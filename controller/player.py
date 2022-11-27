from typing_extensions import Self
from pieces import Pieces
from constants import POSITION_DEPART

class Player():

    def __init__(self: Self, couleur: str) -> None:
        self.couleur : str = couleur
        self.pieces : Pieces = Pieces(self.couleur[0])
        self.position_depart : list = POSITION_DEPART[couleur]
        self.nb_piece = 21

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
            list[int]: La pièce
        """
        return self.pieces.getPiece(num_piece)
    
    def getPositionDepart(self)->list:
        return self.position_depart

    def getNbPieces(self)->int:
        return self.nb_piece

    def removePiece(self)->None:
        self.nb_piece-=1

    def hasPlayedPiece(self,indice_piece:int):
        self.pieces.pieces_joueurs.remove(indice_piece)
        f_piece = './Pieces/'+self.couleur[0].upper()+'/'+str(indice_piece+1)+'.png'
        self.pieces.liste_images_pieces.remove(f_piece)


    def __str__(self: Self) -> str:
        return("Le joueur " + self.couleur + " est en possession de " +  str(self.pieces.getNbPieces()) + " pièce(s).")


# ---- kind of test
if __name__ == "__main__":

    joueur = Player("Rouge")
    print(joueur.getPositionDepart())


