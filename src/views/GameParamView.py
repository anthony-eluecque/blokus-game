from tkinter import Label,Entry
from tkinter.ttk import Combobox
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
        
        self.logWidgets = []

        # Values : x positions[key][0] ; y positions[key][1]
        self.positions = {
            "1":{"pos":[200,100],"arrow":{"left":[140,100],"right":[460,100]}},
            "2":{"pos":[850,100],"arrow":{"left":[790,100],"right":[1110,100]}},
            "3":{"pos":[200,460],"arrow":{"left":[140,460],"right":[460,460]}},
            "4":{"pos":[850,460],"arrow":{"left":[790,460],"right":[1110,460]}}
        }

        self.posWidgetsPlayer = {
            "1":{"nom_joueur":[80,180],"couleur_joueur":[80,260],"choix_couleur":[380,260],"saisi_clavier":[320,180]},
            "2":{"nom_joueur":[735,180],"couleur_joueur":[735,260],"choix_couleur":[1035,260],"saisi_clavier":[975,180]},
            "3":{"nom_joueur":[80,540],"couleur_joueur":[80,620],"choix_couleur":[380,620],"saisi_clavier":[320,540]},
            "4":{"nom_joueur":[735,540],"couleur_joueur":[735,620],"choix_couleur":[1035,620],"saisi_clavier":[975,540]},
        }

        self.posWidgetsIA = {
            "1":{"nom_IA":[80,180],"couleur_IA":[80,240],"choix_couleur":[380,240],"saisi_clavier":[320,180],"difficulte_IA":[80,300],"selecteur_difficulte":[380,300]},
            "2":{"nom_IA":[735,180],"couleur_IA":[735,240],"choix_couleur":[1035,240],"saisi_clavier":[975,180],"difficulte_IA":[735,300],"selecteur_difficulte":[1035,300]},
            "3":{"nom_IA":[80,540],"couleur_IA":[80,600],"choix_couleur":[380,600],"saisi_clavier":[320,540],"difficulte_IA":[80,660],"selecteur_difficulte":[380,660]},
            "4":{"nom_IA":[735,540],"couleur_IA":[735,600],"choix_couleur":[1035,600],"saisi_clavier":[975,540],"difficulte_IA":[735,660],"selecteur_difficulte":[1035,660]},
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
            
            childs = self.__makeEntryPlayer(index)
            self.dataCardPlayers.append([arrow_l,arrow_r,self.bgImagePlayer,label,childs])


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
            components[3].destroy()
            components[3] = self.__makeLabelPlayer(self.bgImageIA,xpos,ypos)
            components[2] =  self.bgImageIA
            
            for childs in components[4]:
                childs.destroy()
            components[4] = self.__makeEntryIA(button.cget('text'))

        else:
            components[3].destroy()
            components[3] = self.__makeLabelPlayer(self.bgImagePlayer,xpos,ypos)
            components[2] = self.bgImagePlayer
            for childs in components[4]:
                childs.destroy()
            components[4] = self.__makeEntryPlayer(button.cget('text'))      

    def __makeEntryPlayer(self,index)->list:

        label = CTkLabel(self.window,text="Nom du joueur : ",bg_color='white',text_color='black')
        label.configure(font=('Roboto Bold', 25))
        label.place(x=self.posWidgetsPlayer[index]["nom_joueur"][0],y=self.posWidgetsPlayer[index]["nom_joueur"][1])


        label2 = CTkLabel(self.window,text="La couleur du joueur : ",bg_color='white',text_color='black')
        label2.configure(font=('Roboto Bold', 25))
        label2.place(x=self.posWidgetsPlayer[index]["couleur_joueur"][0],y=self.posWidgetsPlayer[index]["couleur_joueur"][1])

        selecteur = Combobox(self.window,values=["Blue","Rouge","Vert","Jaune"])
        selecteur.configure(width=10,height=10,font=('Roboto Bold', 20))
        selecteur.place(x=self.posWidgetsPlayer[index]["choix_couleur"][0],y=self.posWidgetsPlayer[index]["choix_couleur"][1])

        entryy = Entry(self.window,width=15)
        entryy.configure(font=('Roboto Bold', 20))
        entryy.place(x=self.posWidgetsPlayer[index]["saisi_clavier"][0],y=self.posWidgetsPlayer[index]["saisi_clavier"][1])
        return [label,label2,selecteur,entryy]

    def __makeEntryIA(self,index)->list:

        label = Label(self.window,text="Nom de l'IA : ",bg='white')
        label.config(font=('Roboto Bold', 20))
        label.place(x=self.posWidgetsIA[index]["nom_IA"][0],y=self.posWidgetsIA[index]["nom_IA"][1])

        label2 = Label(self.window,text="La couleur de l'IA : ",bg='white')
        label2.config(font=('Roboto Bold', 20))
        label2.place(x=self.posWidgetsIA[index]["couleur_IA"][0],y=self.posWidgetsIA[index]["couleur_IA"][1])

        selecteur = Combobox(self.window,values=["Blue","Rouge","Vert","Jaune"])
        selecteur.config(width=10,height=10,font=('Roboto Bold', 20))
        selecteur.place(x=self.posWidgetsIA[index]["choix_couleur"][0],y=self.posWidgetsIA[index]["choix_couleur"][1])

        label3 = Label(self.window,text="La difficulté de l'IA : ",bg='white')
        label3.config(font=('Roboto Bold', 20))
        label3.place(x=self.posWidgetsIA[index]["difficulte_IA"][0],y=self.posWidgetsIA[index]["difficulte_IA"][1])

        selecteur2 = Combobox(self.window,values=["Facile","Moyen","Difficile","Impossible"])
        selecteur2.config(width=10,height=10,font=('Roboto Bold', 20))
        selecteur2.place(x=self.posWidgetsIA[index]["selecteur_difficulte"][0],y=self.posWidgetsIA[index]["selecteur_difficulte"][1])

        entryy = Entry(self.window,width=15)
        entryy.configure(font=('Roboto Bold', 20))
        entryy.place(x=self.posWidgetsIA[index]["saisi_clavier"][0],y=self.posWidgetsIA[index]["saisi_clavier"][1])

        return [label,label2,label3,selecteur,selecteur2,entryy]



    def main( self, longueur = 1300, hauteur = 800 )->None:
        _resizeWindow( self.window, longueur, hauteur )
        self._makeFrame()
        self._makeWindow()
        self._configWidget()
        self.__makeButtons()
        
        self.__makeCardPlayer()
        
    def close( self ):
        _deleteChilds( self.window )