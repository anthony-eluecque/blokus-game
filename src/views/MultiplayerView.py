from utils.window_utils import _resizeWindow, _createFrame, _deleteChilds
from tkinter import Label
from views.View import View
from PIL import ImageTk, Image
from utils.leaderboard_utils import openJson
from customtkinter import CTk
from components.bouton import Bouton


class MultiplayerView(View):


    def __init__(self, controller, window: CTk, longueur=914, hauteur=606):
        super().__init__()

        self.window = window
        self.multiplayerController = controller




    def _makeFrame(self):
        self.mainFrame = _createFrame(self.window, 914, 606)

    def main(self,largeur = 914,hauteur = 606):
        _resizeWindow(self.window,largeur,hauteur)
        self._makeFrame()
        self.testBouton: Bouton = Bouton(self.window, self, 165, 510, width=370, heigth=49, file="./media/assets/button_leave.png", son="button", command=self.multiplayerController.callbackBoutonTest)
    
    
    def close(self):
        _deleteChilds(self.window)