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

    def main(self):
        self.scoreView.main()
