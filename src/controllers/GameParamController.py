from core.Controller import Controller
from core.Core import Core
from customtkinter import CTk

class GameParamController( Controller ):
    """ 
    Controller gérant les paramètres de partie héritant de la classe Controller ainsi que de sa méthode abstraite main()
    """

    def __init__( self, window: CTk ):
        self.window = window
        self.gameParamView = self.loadView( "GameParam", self.window )
        self.core: Core = Core()
    
    def btn_retour( self ):
        self.gameParamView.close()
        c = Core.openController( "home", self.window )
        c.main()
    
    def btn_regles( self ):
        self.gameParamView.close()
        c = Core.openController( "rules", self.window )
        c.main()
    
    def btn_play( self ):
        self.gameParamView.close()
        c = Core.openController( "game", self.window )
        c.main()

    def main( self ):
        self.gameParamView.main()
