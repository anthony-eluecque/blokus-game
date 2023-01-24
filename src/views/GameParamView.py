from tkinter import Label
from views.View import View
from customtkinter import CTk, CENTER,CTkImage, CTkTextbox, CTkLabel, CTkFont
from PIL import Image, ImageTk
from typing_extensions import Self
from utils.window_utils import _resizeWindow, _deleteChilds, _createFrame
from components.bouton import Bouton

class GameParamView(View):
    """
    Classe qui gère la partie graphique du GameParamController . GamesParamView hérite de View
    """

    def __init__( self: Self, controller, window: CTk, width=1300, heigth=800 )->None:
        super().__init__()
        self.paramController = controller
        self.window = window

        # Values : x positions[key][0] ; y positions[key][1]
        self.positions = {
            "1":{"pos":[200,100],"arrow":{"left":[140,100],"right":[460,100]}},
            "2":{"pos":[850,100],"arrow":{"left":[790,100],"right":[1100,100]}},
            "3":{"pos":[200,460],"arrow":{"left":[140,460],"right":[460,460]}},
            "4":{"pos":[850,460],"arrow":{"left":[790,460],"right":[1100,460]}}
        }

    def _makeFrame(self)->None:
        self.mainFrame = _createFrame( self.window, 1300, 800 )

    def _makeWindow(self)->None:
        self.backgroundImage = Image.open( "./media/assets/background_gameparam.png" )
        self.background = ImageTk.PhotoImage( self.backgroundImage )
        self.gameParamTitle = Label( self.mainFrame, text="", image = self.background, bd = 0 )

    def _configWidget(self)->None:
        self.gameParamTitle.place(x = 0,y = 0)
        
    def __makeButtons(self)->None:
        self.settingsBt: Bouton = Bouton( self.window, self, 56, 12, width=65, heigth=65, file="./media/assets/button_settings.png", son="button" )
        self.launchBt: Bouton = Bouton( self.window, self, 543.5, 345.5, width=207, heigth=105, file="./media/assets/button_launch.png", son="button", command=self.paramController.btn_play )
        self.retourBt: Bouton = Bouton( self.window, self, 40, 743, width=570, heigth=48, file="./media/assets/button_retour.png", son="button", command=self.paramController.btn_retour )
        self.reglesBt: Bouton = Bouton( self.window, self, 695, 743, width=570, heigth=48, file="./media/assets/button_regles.png", son="button", command=self.paramController.btn_regles )

    def __makeCardPlayer(self)->None:
        self.dataCardPlayers = []
        self.bgImage = CTkImage(Image.open("./media/assets/player_frame_param.png"), size=(250,50))

        for items in self.positions.values():

            self.__makeLabelPlayer(self.bgImage,items["pos"][0],items["pos"][1])
            self.__makeDirectionnalsArrows(items["arrow"]["left"][0],items["arrow"]["left"][1],"./media/assets/fleche_gauche.png")
            self.__makeDirectionnalsArrows(items["arrow"]["right"][0],items["arrow"]["right"][1],"./media/assets/fleche_droite.png")

    def __makeLabelPlayer(self,bgimage,xpos,ypos)->None:
        self.labelPlayers = []
        self.player = CTkLabel(master = self.mainFrame,text="" , image=bgimage)
        self.player.place(x=xpos,y=ypos)

    def __makeDirectionnalsArrows(self,x,y,_file)->None:
        self.button = Bouton(self.window,self,width=50,heigth=50,xpos=x,ypos=y,file=_file)

    
    def __makeEntry(self)->None:
        pass

    def main( self, longueur = 1300, hauteur = 800 )->None:
        _resizeWindow( self.window, longueur, hauteur )
        self._makeFrame()
        self._makeWindow()
        self._configWidget()
        self.__makeButtons()
        
        self.__makeCardPlayer()
        
    def close( self ):
        _deleteChilds( self.window )