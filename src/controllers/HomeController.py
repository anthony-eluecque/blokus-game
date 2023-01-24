# -*- encoding:utf-8 -*-
from core.Controller import Controller
from utils.controller_utils import _openController
from components.soundclass import Sound

class HomeController(Controller,Sound):
    """ 
    Controller gérant le menu héritant de la classe Controller ainsi que de sa méthode abstraite main()
    Hérite aussi de Sound pour jouer la musique de fond.
    """

    def __init__(self, window):
        super().__init__("background")
        self.window = window
        super().play()
        self.homeView = self.loadView("Home", window)
    
    def btnPlay(self):
        _openController(self.homeView, "Game", self.window)

    def btnRules(self):
        _openController(self.homeView, "Rules", self.window)

    def btnStats(self):
        _openController(self.homeView, "Stats", self.window)

    def btnSettings(self):
        _openController(self.homeView, "Settings", self.window)
      
        
    def main(self):
        self.homeView.main()
