from core.Controller import Controller
from core.Controller import Controller
from core.Core import Core
from customtkinter import CTk, CTkSlider
from utils.controller_utils import _openController

class SettingsController(Controller):
    """ 
    Controller gérant la fin de partie (score) héritant de la classe Controller ainsi que de sa méthode abstraite main()
    """

    def __init__(self, window : CTk):
        
        self.window = window
        self.settingsView = self.loadView("Settings", self.window)

    def callbackSlider(slider : CTkSlider, valeur: int):
        valeur = int(slider.get() *100)

    def btn_clear(self):
        _openController(self.settingsView, "Home", self.window)

    def main(self):
        self.settingsView.main()