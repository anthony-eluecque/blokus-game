# -*- encoding:utf-8 -*-
from core.Controller import Controller
from core.Core import Core

class HomeController(Controller):

    def __init__(self,window):
        self.window = window
        self.homeView = self.loadView("Home",window)
    
    def btnPlay(self):
        for child in self.window.winfo_children():
            child.destroy()
        c = Core.openController("Game",self.window)
        c.main()

    def btnRules(self):
        for child in self.window.winfo_children():
            child.destroy()
        c = Core.openController("Rules",self.window)
        c.main()

    def btnStats(self):
        c = Core.openController("Stats",self.window)
        c.main()
        
    def main(self):
        self.homeView.main()
