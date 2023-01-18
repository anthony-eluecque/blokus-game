from core.Controller import Controller
from core.Core import Core
from customtkinter import CTk

class RulesController(Controller):
    """ 
    Controller gérant la partie des règles héritant de la classe Controller ainsi que de sa méthode abstraite main()
    """

    def __init__(self,window : CTk):
        self.window = window
        self.rulesView = self.loadView("Rules",self.window)
        self.core = Core()
    
    def btn_clear(self):
        self.rulesView.close()
        c = Core.openController("home",self.window)
        c.main()

    def main(self):
        self.rulesView.main()
