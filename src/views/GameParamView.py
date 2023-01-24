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
            "2":{"pos":[850,100],"arrow":{"left":[790,100],"right":[1110,100]}},
            "3":{"pos":[200,460],"arrow":{"left":[140,460],"right":[460,460]}},
            "4":{"pos":[850,460],"arrow":{"left":[790,460],"right":[1110,460]}}
        }

        self.dataCardPlayers = []
        self.bgImagePlayer = CTkImage(Image.open("./media/assets/player_frame_param.png"), size=(250,50))
        self.bgImageIA = CTkImage(Image.open("./media/assets/IA_frame_param.png"), size=(250,50))

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

        for i in range(len(self.positions)):
            index = str(i+1)
            label = self.__makeLabelPlayer(self.bgImagePlayer,self.positions[index]["pos"][0],self.positions[index]["pos"][1])
            arrow_l = self.__makeDirectionnalsArrows(self.positions[index]["arrow"]["left"][0],self.positions[index]["arrow"]["left"][1],"./media/assets/fleche_gauche.png",index)
            arrow_r = self.__makeDirectionnalsArrows(self.positions[index]["arrow"]["right"][0],self.positions[index]["arrow"]["right"][1],"./media/assets/fleche_droite.png",index)

            self.dataCardPlayers.append([arrow_l,arrow_r,self.bgImagePlayer,label])

    def __makeLabelPlayer(self,bgimage,xpos,ypos):
        player = CTkLabel(master = self.mainFrame,text="" , image=bgimage)
        player.place(x=xpos,y=ypos)
        return player

    def __makeDirectionnalsArrows(self,x,y,_file,index):
        button = Bouton(self.window,self,width=50,heigth=50,xpos=x,ypos=y,file=_file,text=str(index),command=lambda:self.callbackStatus(button),son="button")
        return button

    def callbackStatus(self,button):

        components : list =  self.dataCardPlayers[int(button.cget('text'))-1]
        xpos = self.positions[button.cget('text')]["pos"][0]
        ypos = self.positions[button.cget('text')]["pos"][1]
        image = components[2]
        if image == self.bgImagePlayer:
            components[2] =  self.bgImageIA
            components[3] = self.__makeLabelPlayer(self.bgImageIA,xpos,ypos)
        else:
            components[2] = self.bgImagePlayer
            components[3] = self.__makeLabelPlayer(self.bgImagePlayer,xpos,ypos)




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