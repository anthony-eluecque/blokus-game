from core.Controller import Controller
from core.Core import Core
from customtkinter import CTk


class StatsController(Controller):


    def __init__(self,window:CTk) -> None:
        super().__init__()
        self.window = window
        self.statsView = self.loadView("Stats",self.window)
        self.core : Core = Core()

    def backToMenu(self):
        self.statsView.close()
        c = Core.openController("home",self.window)
        c.main()
    
    def showWidget(self):
        self.statsView.close()
        c = Core.openController("DetailGame",self.window)
        c.main()

    def main(self):
        self.statsView.main()