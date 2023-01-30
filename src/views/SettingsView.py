from tkinter import Label
from views.View import View
from customtkinter import CTk, CENTER, CTkLabel, CTkFont, CTkSlider, IntVar
from PIL import Image, ImageTk
from typing_extensions import Self
from utils.window_utils import _resizeWindow, _deleteChilds, _createFrame
from components.bouton import Bouton
from components.soundclass import Sound
from utils.sounds.sound_utils import _editValue, _getValues


class SettingsView(View):
    """
    Classe qui gère la partie graphique du SettingsController. SettingsView hérite de View
    """

    def __init__(self: Self, controller, window: CTk, width = 1300, heigth = 800):
        super().__init__()
        self.sound: Sound = Sound("testing")
        self.volumes: dict[str, float | int] = _getValues()
        self.settingsController = controller
        self.window = window

    # Main
    def _makeFrame(self):
        self.mainFrame = _createFrame(self.window,1000,1000)

    def _makeWindow(self):
        self.backgroundImage = Image.open("./media/assets/background_rules.png")
        self.background = ImageTk.PhotoImage(self.backgroundImage)
        self.bgSettings: Label = Label(self.mainFrame, text="", image = self.background, bd = 0)

    # Parts
    def _makeTitle(self):
        self.settingsTitle: CTkLabel = CTkLabel(master = self.mainFrame, text="Settings", fg_color="white", font = CTkFont(family="Roboto Medium", size=40), text_color="black")

    def _makeMusicPart(self):
        self.musicBar: CTkSlider = CTkSlider(master = self.mainFrame, width=300, height=20, orientation="horizontal", from_=0, to=100, number_of_steps=100, variable=IntVar(value=50), bg_color="white", fg_color="lightgray", button_color="grey", button_hover_color="grey", progress_color="yellow", command=self._callbackMusicValue)
        self.musicBar.bind("<ButtonRelease-1>", self._playMusicSound)
        self.musicValue: int = int(self.musicBar.get())
        self.musicNumber: CTkLabel =  CTkLabel(master = self.mainFrame, text="Sound: " + str(self.musicValue), fg_color="white", font = CTkFont(family="Roboto Medium", size=35), text_color="black")

    def _makeSFXPart(self):
        self.sfxBar: CTkSlider = CTkSlider(master = self.mainFrame, width=300, height=20, orientation="horizontal", from_=0, to=100, number_of_steps=100, variable=IntVar(value=50), bg_color="white", fg_color="lightgray", button_color="grey", button_hover_color="grey", progress_color="yellow", command=self._callbackSFXValue)
        self.sfxBar.bind("<ButtonRelease-1>", self._playSFXSound)
        self.sfxValue: int = int(self.sfxBar.get())
        self.sfxNumber: CTkLabel =  CTkLabel(master = self.mainFrame, text="SFX: " + str(self.musicValue), fg_color="white", font = CTkFont(family="Roboto Medium", size=35), text_color="black")

    def _makeLanguagesPart(self):
        self.languageTitle: CTkLabel = CTkLabel(master = self.mainFrame, text="Languages", fg_color="white", font = CTkFont(family="Roboto Medium", size=35), text_color="black")
        self.frenchButton: Bouton = Bouton(self.window, self, 378, 500, width=225, heigth=60, file="./media/assets/settings_french.png", son="button")
        self.englishButton: Bouton = Bouton(self.window, self, 378, 500, width=225, heigth=60, file="./media/assets/english_settings.png", son="button")

    def _makeButtonApply(self):
        self.backSettings: Bouton = Bouton(self.window, self, 378, 500, width=225, heigth=60, file="./media/assets/apply_settings.png", son="button", command=self.settingsController.btn_clear)

    # Callbacks
    def _callbackMusicValue(self, value: float):
        self.musicNumber.configure(text="Sound: " + str(int(value)))

    def _callbackSFXValue(self, value: float):
        self.sfxNumber.configure(text="SFX: " + str(int(value)))

    # Sound callbacks
    def _playMusicSound(self, e):
        volume: float|int = self.musicBar.get()/100
        # On récup et modifie la value de sfx pour jouer le son puis on remet à la valeur d'origine (pas d'autre moyen)
        sfx_vol = self.volumes["sfx"]
        _editValue("sfx", volume);  _editValue("music", volume)
        self.sound.play()
        _editValue("sfx", sfx_vol)

    def _playSFXSound(self, e):
        volume: float|int = self.sfxBar.get()/100
        _editValue("sfx", volume)
        self.sound.play()

    # Config
    def _configWidget(self):
        self.bgSettings.place(x = 0,y = 0)
        self.settingsTitle.pack(side="top", pady=40)
        self.musicNumber.pack(side="top", pady=10)
        self.musicBar.place(relx=0.5, rely=0.28, anchor=CENTER)
        self.sfxNumber.pack(side="top", pady=38)
        self.sfxBar.place(relx=0.5, rely=0.405, anchor=CENTER)
        self.languageTitle.pack(side="top", pady=27)
        self.frenchButton.pack()
        self.englishButton.pack()
        self.frenchButton.place(relx=0.30, rely=0.60, anchor=CENTER)
        self.englishButton.place(relx=0.70, rely=0.60, anchor=CENTER)
        self.backSettings.pack()
        self.backSettings.place(relx=0.5, rely=0.89, anchor=CENTER)

    def main(self, longueur = 625, hauteur = 700):
        _resizeWindow(self.window, longueur, hauteur)
        self._makeFrame()
        self._makeWindow()
        self._makeTitle()
        self._makeMusicPart()
        self._makeSFXPart()
        self._makeLanguagesPart()
        self._makeButtonApply()
        self._configWidget()

    def close(self):
        _deleteChilds(self.window)
