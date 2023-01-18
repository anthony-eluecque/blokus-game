from core.Controller import Controller
from core.Core import Core
from customtkinter import CTk

class ScoreController(Controller):
    """ 
    Controller gérant la fin de partie (score) héritant de la classe Controller ainsi que de sa méthode abstraite main()
    """

    def __init__(self,window : CTk):
        
        self.window = window
        self.scoreView = self.loadView("score",self.window)
        # self.core = Core()

        # self._sortClassement()
        # self.scoreView._makeClassement(classement)

    def _sortClassement(joueurs):
        classement = {}
        for joueur in joueurs :
            for numPiece in joueur.pieces.pieces_joueurs:
                piece = joueur.jouerPiece(numPiece-1)
                for line in piece:
                    for square in line:
                        if square == 1:
                            joueur.removeScore()
            classement[joueur.couleur]=joueur.score

        print(classement)

    def main(self):
        self.scoreView.main()
