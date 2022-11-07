from pieces import Pieces
from controller.plateau import Plateau
from controller.player import Player

class Game():

    def __init__(self, tab: Plateau, players: list[Player]) -> None:
        
        self.plateau : Plateau = tab
        self.players : list[Player] = players
        self.running : bool = True

    def run(self):

        # self.players[0].pieces.rotate(2)
        # self.players[0].pieces.rotate(1)
        print(self.players[0].pieces.afficherPiece(2))
        # self.plateau.placerPiece(15,17,self.players[0].jouerPiece(2),self.players[0])
        # self.plateau.placerPiece(3,0,self.players[0].jouerPiece(0),self.players[0])
        # self.plateau.placerPiece(13,17,self.players[0].jouerPiece(1),self.players[0])
        print(self.plateau)

        

if __name__ == "__main__":

    
    Jeu = Game(Plateau(20,20),[Player("Rouge"),Player("Bleu")])
    
    Jeu.run()

    # print(joueur)