from core.Controller import Controller
from core.Core import Core
from customtkinter import CTk

class RulesController(Controller):

    def __init__(self,window : CTk):
        self.window = window
        self.homeView = self.loadView("Rules",self.window)
        self.core = Core()
    
    def btn_clear(self):
        for child in self.window.winfo_children():
            child.destroy()
        # peut être callback Core avec home
        c = Core.openController("home",self.window)
        c.main()

    def main(self):
        self.homeView.main()
