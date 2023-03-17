from constants import PIECES,PIECES_IMAGES
from copy import deepcopy

class Pieces:
    
    def __init__(self,color:str) -> None:

        self.liste_pieces : list[list] = PIECES
        self.liste_pieces_copy : list[list] = deepcopy(self.liste_pieces)
        self.images_pieces : list[str] = PIECES_IMAGES
        self.pieces_joueurs : list = [_ for _ in range(len(PIECES_IMAGES))]
        self.liste_images_pieces : list[str] = self.__fichierJoueur(color)

    def __fichierJoueur(self,color:str)->list:

        images_pieces : list[str] = ["" for _ in range(len(PIECES_IMAGES))]
        for i in range(len(self.images_pieces)):
            images_pieces[i] = "./media/pieces/"+color.upper()+self.images_pieces[i]
        return images_pieces

    def getNbPieces(self) -> int:
        """Retourne le nombre de pièces restantes

        Returns:
            int: Le nombre de pièces restantes
        """
        return len(self.liste_pieces)

    def getPiece(self, num_piece: int) -> list:
        """Retourne une pièce

        Args:
            num_piece (int): La pièce voulue

        Returns:
            list: La pièce
        """
        return self.liste_pieces[num_piece]

    def getImagesPieces(self)->list[str]:
        return self.liste_images_pieces

    def reverse(self,num_piece : int) -> None:
        """Inverse une pièce
        Args:
            num_piece (int): Le numéro de la pièce à tourner
        """
        self.liste_pieces[num_piece] = list(map(lambda x: x[::-1], self.getPiece(num_piece)))

    def rotate(self, num_piece: int) -> None:
        """Tourne une pièce

        Args:
            num_piece (int): La pièce à tourner
        """
        self.liste_pieces[num_piece] = [list(row) for row in zip(*reversed(self.getPiece(num_piece)))]

    def resetRotation( self, num_piece : int ) -> None:
        self.liste_pieces[ num_piece ] = deepcopy( self.liste_pieces_copy[ num_piece ] )

    def afficherPiece(self , num_piece: int) -> None:
        """Affiche une pièce

        Args:
            num_piece (int): La pièce à afficher
        """
        for line in self.getPiece(num_piece):
            print(line)   

    def __getitem__(self, key: int) -> list:
        return self.liste_pieces[key]

    def __len__(self) -> int:
        return len(self.liste_pieces)

    def __str__(self) -> str:
        return str(self.liste_pieces)