# -*- encoding:utf-8 -*-
from core.Controller import Controller
from core.Core import Core
from utils.controller_utils import _openController
from components.soundclass import Sound

class HomeController(Controller,Sound):

    def __init__(self,window):
        super().__init__("background")
        self.window = window
        super().play()
        self.homeView = self.loadView("Home",window)
    
    def btnPlay(self):
        _openController(self.homeView,"Game",self.window)

    def btnRules(self):
        _openController(self.homeView,"Rules",self.window)

    def btnStats(self):
        _openController(self.homeView,"Stats",self.window)
      
        
    def main(self):
        self.homeView.main()
