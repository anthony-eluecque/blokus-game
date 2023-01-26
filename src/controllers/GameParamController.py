from core.Controller import Controller
from core.Core import Core
from customtkinter import CTk
from utils.config_utils import Configuration

class GameParamController( Controller ):
    """ 
    Controller gérant les paramètres de partie héritant de la classe Controller ainsi que de sa méthode abstraite main()
    """

    def __init__( self, window: CTk ):
        self.window = window
        self.gameParamView = self.loadView( "GameParam", self.window )
        self.core: Core = Core()
        self.config = []
        for i in range( 4 ): self.config.append( { "nom": "", "couleur": "", "diff": "joueur" } )
    
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
        Configuration.saveConfig( self.config )
        c = Core.openController( "game", self.window )
        c.main()

    def resetConfig( self, index: int, estIa: bool ):
        self.config[ index ] = { "nom": "", "couleur": "", "diff": estIa and "" or "joueur" }

    def setConfigAttribute( self, index: int, attribute: str, val: str ):
        self.config[ index ][ attribute ] = val


    def main( self ):
        self.gameParamView.main()
