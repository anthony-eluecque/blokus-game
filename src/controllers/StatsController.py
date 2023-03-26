from core.Controller import Controller
from core.Core import Core
from customtkinter import CTk
from utils.controller_utils import _openController


class StatsController(Controller):


    def __init__(self,window:CTk) -> None:
        super().__init__()
        self.window = window
        self.statsView = self.loadView("Stats",self.window)
        self.core : Core = Core()

    def backToMenu(self)->None:
        self.statsView.close()
        c = Core.openController("home",self.window)
        c.main()
    
    def showWidget(self,idPartie)->None:
        self.statsView.openDetailGame(idPartie)

    def backToStats(self)->None:
        self.statsView.close()
        c = Core.openController("stats",self.window)
        c.main()

    def main(self)->None:
        self.statsView.main()