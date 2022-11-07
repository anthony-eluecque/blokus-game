from typing_extensions import Self
from constants import PIECES, PIECES_IMAGES

class Pieces():


    def __init__(self : Self,color:str) -> None:
        self.liste_pieces : list[list] = PIECES
        self.liste_images_pieces : list[str] = self.__fichierJoueur(PIECES_IMAGES,color)

    def __fichierJoueur(self:Self,images_pieces:list[str],color:str)->list[str]:

        for i in range(len(images_pieces)):
            images_pieces[i] = "./Pieces/"+color.upper()+images_pieces[i]
        return images_pieces

    def getNbPieces(self: Self) -> int:
        """Retourne le nombre de pièces restantes

        Returns:
            int: Le nombre de pièces restantes
        """
        return len(self.liste_pieces)

    def getPiece(self: Self, num_piece: int) -> list:
        """Retourne une pièce

        Args:
            num_piece (int): La pièce voulue

        Returns:
            list: La pièce
        """
        return self.liste_pieces[num_piece]

    def getImagesPieces(self)->list[str]:
        return self.liste_images_pieces

    def rotate(self: Self, num_piece: int) -> None:
        """Tourne une pièce

        Args:
            num_piece (int): La pièce à tourner
        """
        self.liste_pieces[num_piece] = [list(row) for row in zip(*reversed(self.getPiece(num_piece)))]

    def afficherPiece(self: Self , num_piece: int) -> None:
        """Affiche une pièce

        Args:
            num_piece (int): La pièce à afficher
        """
        for line in self.getPiece(num_piece):
            print(line)   

    def __getitem__(self: Self, key: int) -> list:
        return self.liste_pieces[key]

    def __len__(self: Self) -> int:
        return len(self.liste_pieces)

    def __str__(self: Self) -> str:
        return str(self.liste_pieces)


if __name__ == "__main__":

    test = Pieces('R')
    test.afficherPiece(1)
    for i in range(4):
        test.rotate(1)
        test.afficherPiece(1)
