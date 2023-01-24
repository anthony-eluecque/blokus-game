from tkinter import Label
from views.View import View
from customtkinter import CTk, CENTER, CTkTextbox, CTkLabel, CTkFont
from PIL import Image, ImageTk
from typing_extensions import Self
from utils.window_utils import _resizeWindow, _deleteChilds, _createFrame
from components.bouton import Bouton

class GameParamView(View):
    """
    Classe qui gère la partie graphique du GameParamController . GamesParamView hérite de View
    """

    def __init__( self: Self, controller, window: CTk, width=1300, heigth=800 ):
        super().__init__()
        self.paramController = controller
        self.window = window

    def _makeFrame( self ):
        self.mainFrame = _createFrame( self.window, 1300, 800 )

    def _makeWindow( self ):
        self.backgroundImage = Image.open( "./media/assets/background_gameparam.png" )
        self.background = ImageTk.PhotoImage( self.backgroundImage )
        self.gameParamTitle = Label( self.mainFrame, text="", image = self.background, bd = 0 )

    def _configWidget( self ):
        self.gameParamTitle.place( x = 0,y = 0 )
        
    def __makeButtons( self ):
        self.settingsBt: Bouton = Bouton( self.window, self, 56, 12, width=65, heigth=65, file="./media/assets/button_settings.png", son="button" )
        self.launchBt: Bouton = Bouton( self.window, self, 543.5, 345.5, width=207, heigth=105, file="./media/assets/button_launch.png", son="button" )
        self.retourBt: Bouton = Bouton( self.window, self, 40, 743, width=570, heigth=48, file="./media/assets/button_retour.png", son="button" )
        self.reglesBt: Bouton = Bouton( self.window, self, 695, 743, width=570, heigth=48, file="./media/assets/button_regles.png", son="button" )

    def main( self, longueur = 1300, hauteur = 800 ):
        _resizeWindow( self.window, longueur, hauteur )
        self._makeFrame()
        self._makeWindow()
        self._configWidget()
        self.__makeButtons()
        
    def close( self ):
        _deleteChilds( self.window )