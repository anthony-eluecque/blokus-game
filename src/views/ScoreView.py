from utils.window_utils import _resizeWindow, _createFrame, _deleteChilds
from tkinter import Label
from views.View import View
from PIL import ImageTk, Image
from utils.leaderboard_utils import openJson
from customtkinter import CTk
from components.bouton import Bouton

class ScoreView(View):
    """
    Classe qui gère la partie graphique du ScoreController . ScoreView hérite de View
    """

    colors = ["#ffb800", "#787878", "#ff5c00", "#110eb8"]

    def __init__(self, controller, window: CTk, longueur=914, hauteur=606):
        super().__init__()

        self.window = window
        self.scoreController = controller

    def _makeFrame(self):
        self.mainFrame = _createFrame(self.window, 914, 606)

    def _makeBackground(self):
        img = Image.open("./media/assets/bg_score.png")
        self.img = ImageTk.PhotoImage(img)
        self.bgImg = Label(self.mainFrame, image=self.img, text="")
        self.bgImg.place(x=0,y=0,anchor="nw")

    def _makeTitleClassement(self):
        self.scoreTbLabel = Label(self.mainFrame, text="Tableau des scores", font="Roboto 30 bold", bg="white" )
        self.scoreTbLabel.place(x=457, y=130, anchor="center")

    def _makeClassement(self,classement):
        i: int = 1
        for couleur in classement.keys():
            podium: str = i == 1 and "1er :" or str( i ) + "ème :"
            podiumPos: Label = Label(self.mainFrame, text=podium, font="Roboto 30 bold", bg="white", fg=self.colors[ i - 1 ])
            podiumPos.place(x=280, y=250 + ( ( i-1) * 50 ), anchor="e")
            podiumScore: Label = Label(self.mainFrame, text=f'{ couleur } avec { classement[ couleur ] } points', font="Roboto 30 bold", bg="white" )
            podiumScore.place(x=285, y=250 + ( ( i-1) * 50 ), anchor="w")
            i += 1

    def _leaveGame(self):
        self.close()
        self.scoreController._backToHome()

    def _makeBackButton(self):
        self.backButton: Bouton = Bouton(self.window, self, 354, 500,  width=206, heigth=49, file="./media/assets/buttun_rules_return.png", son="button", command=self._leaveGame)

    def main(self, longueur=914, hauteur=606):
        classement = list(openJson()).pop()
        _resizeWindow(self.window, longueur, hauteur)
        self._makeFrame()
        self._makeBackground()
        self._makeTitleClassement()
        self._makeClassement(classement)
        self._makeBackButton()

    def close(self):
        _deleteChilds(self.window)