from core.Controller import Controller
from core.Core import Core
from customtkinter import CTk
from utils.config_utils import Configuration
from utils.controller_utils import _openController

class GameParamController( Controller ):
    """ 
    Controller gérant les paramètres de partie héritant de la classe Controller ainsi que de sa méthode abstraite main()
    """

    def __init__( self, window: CTk ):
        self.window = window
        self.gameParamView = self.loadView( "GameParam", self.window )
        self.core: Core = Core()
        self.config = []
        for i in range( 4 ): 
            self.config.append( { "nom": "", "couleur": "", "niveau_difficulte": 0 } )
    
    def btn_retour( self ):
        self.gameParamView.close()
        c = Core.openController( "home", self.window )
        c.main()    
    
    def btn_regles( self ):
        self.gameParamView.close()
        c = Core.openController( "rules", self.window )
        c.main()
    
    def btn_play( self ):

        if Configuration.saveConfig( self.config ):
            self.gameParamView.close()
            c = Core.openController( "game", self.window )
            c.main()
        else:
            print("Erreur")

    def resetConfig( self, index: int):        
        self.config[ index ] = { "nom": "", "couleur": "", "niveau_difficulte": 0}


    def setConfigAttribute( self, index: int, attribute: str, val: str ):
        self.config[ index ][ attribute ] = val


    def main( self ):
        self.gameParamView.main()
