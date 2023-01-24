from tkinter import Label
from views.View import View
from customtkinter import CTk, CENTER, CTkLabel, CTkFont, CTkSlider
from PIL import Image, ImageTk
from typing_extensions import Self
from utils.window_utils import _resizeWindow, _deleteChilds, _createFrame
from components.bouton import Bouton


class SettingsView(View):
    """
    Classe qui gère la partie graphique du SettingsController. SettingsView hérite de View.
    """

    def __init__(self,controller,window:CTk,width=1300,heigth=800):

        super().__init__()

        self.gameController = controller
        self.window = window

    def _makeFrame(self):
        self.mainFrame = _createFrame(self.window,1000,1000)

    def _makeWindow(self):
        self.backgroundImage = Image.open("./media/assets/background_rules.png")
        self.background = ImageTk.PhotoImage(self.backgroundImage)
        self.bgSettings = Label(self.mainFrame, text="", image = self.background, bd = 0)

    def _makeTitle(self):
        self.settingsTitle = CTkLabel(master = self.mainFrame , text="Settings", fg_color="white",font=CTkFont(family="Roboto Medium", size=40), text_color="black")

    def _makeSoundPart(self):
        self.soundBar = CTkSlider(master = self.mainFrame, width=300, height=20, orientation="horizontal", number_of_steps=100, bg_color="white", fg_color="white", button_color="grey", button_hover_color="grey", progress_color="yellow")
        self.valeur = int(self.soundBar.get() * 100)
        self.soundTitle = CTkLabel(master = self.mainFrame , text="Sound", fg_color="white",font=CTkFont(family="Roboto Medium", size=35), text_color="black")
        self.soundNumber =  CTkLabel(master = self.mainFrame , text=str(self.valeur), fg_color="white",font=CTkFont(family="Roboto Medium", size=25), text_color="black")

    def _makeLanguagesPart(self):
        self.languageTitle = CTkLabel(master = self.mainFrame , text="Languages", fg_color="white",font=CTkFont(family="Roboto Medium", size=35), text_color="black")
        self.frenchButton = Bouton(self.window, self, 378, 500, width=225, heigth=60, file="./media/assets/settings_french.png", son="button")
        self.englishButton = Bouton(self.window, self, 378, 500, width=225, heigth=60, file="./media/assets/english_settings.png", son="button")

    def _makeButtonApply(self):
        self.backSettings: Bouton = Bouton(self.window, self, 378, 500, width=225, heigth=60, file="./media/assets/apply_settings.png", son="button")

    def _callbackValeur():
        pass

    def _configWidget(self):
        self.bgSettings.place(x = 0,y = 0)
        self.settingsTitle.pack(side="top", pady=40)
        self.soundTitle.pack(side="top", pady=38)
        self.soundTitle.place(relx=0.5, rely=0.20, anchor=CENTER)
        self.soundNumber.pack(side="top", pady=38)
        self.soundBar.pack(side="top", pady=38)
        self.soundBar.place(relx=0.5, rely=0.30, anchor=CENTER)
        self.languageTitle.pack(side="top", pady=27)
        self.frenchButton.pack()
        self.englishButton.pack()
        self.frenchButton.place(relx=0.30, rely=0.50, anchor=CENTER)
        self.englishButton.place(relx=0.70, rely=0.50, anchor=CENTER)
        self.backSettings.pack()
        self.backSettings.place(relx=0.5, rely=0.89, anchor=CENTER)

    def main(self, longueur = 625, hauteur = 700):
        _resizeWindow(self.window, longueur, hauteur)
        self._makeFrame()
        self._makeWindow()
        self._makeTitle()
        self._makeSoundPart()
        self._makeLanguagesPart()
        self._makeButtonApply()
        self._configWidget()

    def close(self):
        _deleteChilds(self.window)