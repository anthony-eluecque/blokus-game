from tkinter import Label
from views.View import View
from customtkinter import CTk
from PIL import Image,ImageTk
from typing_extensions import Self
import os
from utils.window_utils import _resizeWindow,_deleteChilds,_createFrame
from components.bouton import Bouton
from components.SoundButton import SoundButton

class HomeView(View):
    """
    Classe qui gère la partie graphique du HomeController . HomeView hérite de View
    """

    def __init__(self,controller,window:CTk, longueur = 700, hauteur = 700):
        super().__init__()

        self.window = window
        self.homeController = controller

    def _makeFrame(self):
        self.mainFrame = _createFrame(self.window,700,1000)

    def _placement(self):
        self.label.place(x = 0,y = 0)  

    def _UI(self : Self):
        self.playButton: Bouton = Bouton(self.window, self, 165, 315, width=370, heigth=49, file="./media/assets/button_play.png", son="button", command=self.homeController.btnPlay)

        self.rulesButton: Bouton = Bouton(self.window, self, 165, 380, width=370, heigth=49, file="./media/assets/button_rules.png", son="button", command=self.homeController.btnRules)
        
        self.statsButton: Bouton = Bouton(self.window, self, 165, 445, width=370, heigth=49, file="./media/assets/button_stats.png", son="button", command=self.homeController.btnStats)

        self.leaveButton: Bouton = Bouton(self.window, self, 165, 510, width=370, heigth=49, file="./media/assets/button_leave.png", son="button", command=self.window.destroy)
                
        self.backgroundImage = Image.open(os.path.join("./media/assets/carre.png"))
        self.background = ImageTk.PhotoImage(self.backgroundImage)
        self.label = Label(self.mainFrame, image = self.background, bd = 0)   

        self.soundButton: SoundButton = SoundButton(self.window, self, 85, 560)


    def main(self, longueur = 700 ,hauteur = 700):
        _resizeWindow(self.window,longueur,hauteur)
        self._makeFrame()
        self._UI()
        self._placement()

    def close(self):
        _deleteChilds(self.window)