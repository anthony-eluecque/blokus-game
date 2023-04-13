from config import APP_PATH
from utils.window_utils import _resizeWindow, _createFrame, _deleteChilds
from tkinter import Entry, Label
from views.View import View
from PIL import ImageTk, Image
from customtkinter import CTk
from components.bouton import Bouton
import os
from customtkinter import CTk, CTkImage, CTkLabel, CTkCanvas
from socket import gethostname, gethostbyname
import pyperclip as pc

class MultiplayerView(View):


    def __init__(self, controller, window: CTk, longueur=900, hauteur=624):
        super().__init__()

        self.window = window
        self.multiplayerController = controller
        self.index = 0
    
    def _makeBackground(self):
        self.backgroundImage = Image.open(os.path.join(APP_PATH + r"/../media/assets/multiplayer_bg.png"))
        self.background = ImageTk.PhotoImage(self.backgroundImage)
        self.label = Label(self.mainFrame, image = self.background, bd = 0) 
        self.label.place(x=0,y=0)


    def _makeFrame(self):
        self.mainFrame = _createFrame(self.window, 900, 624)

    def main(self,largeur = 900,hauteur = 624):
        _resizeWindow(self.window,largeur,hauteur)
        self._makeFrame()
        self._makeBackground()
        self.backHome: Bouton = Bouton(self.window, self, 350, 520, width=206, heigth=49, file=APP_PATH + "/../media/assets/buttun_rules_return.png", son="button", command=self.multiplayerController.goBackMenu)    

        self.entryClient = Entry(self.window,width=15, fg="grey", bg="grey", relief="sunken", foreground="white")
        self.entryClient.configure(font=('Roboto Bold', 20))
        self.entryClient.place(x=265,y=345)

        self.createServer : Bouton = Bouton(
            self.window, self, 520, 136, width=206, heigth=49, 
            file=APP_PATH + r"/../media/assets/createMulti_button.png", son="button", 
            command= lambda : self.multiplayerController._createServer('0.0.0.0'))    
        
        self.joinServer : Bouton = Bouton(
            self.window, self, 520, 335, width=206, heigth=49, 
            file=APP_PATH + r"/../media/assets/joinMulti_button.png", son="button", 
            command=lambda : self.multiplayerController._joinServer(self.entryClient.get()))    


    def invalidServer(self):
        _resizeWindow(self.window,600,300)
        self.mainFrame = _createFrame(self.window, 600, 300)
        self.bgImage = CTkImage(Image.open(APP_PATH + r"/../media/assets/bg_erreurServ.png"), size=(600, 300))
        self.bg = CTkLabel(self.window, text="", image = self.bgImage)
        self.bg.place(x=0,y=0)

        self.createServer : Bouton = Bouton(
            self.window, self, 320, 255, width=200, heigth=33, 
            file=APP_PATH + r"/../media/assets/createserv_erreur.png", son="button", 
            command= lambda : self.multiplayerController._createServer('0.0.0.0')) 

        self.retourServer : Bouton = Bouton(
            self.window, self, 100, 255, width=200, heigth=33, 
            file=APP_PATH + r"/../media/assets/retour_serveur.png", son="button", 
            command= lambda : self.multiplayerController.goBackMultiMenu()) 


    def invalidServerClientSide(self):
        _resizeWindow(self.window,600,300)
        self.mainFrame = _createFrame(self.window, 600, 300)
        self.bgImage = CTkImage(Image.open(APP_PATH + r"/../media/assets/bg_retour_client.png"), size=(600, 300))
        self.bg = CTkLabel(self.window, text="", image = self.bgImage)
        self.bg.place(x=0,y=0)

        self.retourServer : Bouton = Bouton(
            self.window, self, 200, 255, width=200, heigth=33, 
            file=APP_PATH + r"/../media/assets/retour_serveur.png", son="button", 
            command= lambda : self.multiplayerController.goBackMultiMenu()) 

    def choiseJoinOrNot(self):
        _resizeWindow(self.window,600,300)
        self.mainFrame = _createFrame(self.window, 600, 300)
        self.bgImage = CTkImage(Image.open(APP_PATH + r"/../media/assets/bg_joinserver.png"), size=(600, 300))
        self.bg = CTkLabel(self.window, text="", image = self.bgImage)
        self.bg.place(x=0,y=0)

        self.retourServer : Bouton = Bouton(
            self.window, self, 320, 255, width=200, heigth=33, 
            file=APP_PATH + r"/../media/assets/retour_serveur.png", son="button", 
            command= lambda : self.multiplayerController.goBackMultiMenu())
        
        self.joinServer :  Bouton = Bouton(
            self.window, self, 100, 255, width=200, heigth=33, 
            file=APP_PATH + r"/../media/assets/joinserver.png", son="button", 
            command= lambda : self.multiplayerController._joinServer(gethostbyname(gethostname())) 
        )

    def __copyIp(self):
        pc.copy(gethostbyname(gethostname()))
        return(pc.paste())

    def waitingScreen(self):
        _resizeWindow(self.window,600,300)
        self.mainFrame = _createFrame(self.window, 600, 300)
        self.bgImage = CTkImage(Image.open(APP_PATH + r"/../media/assets/waiting_bg.png"), size=(600, 300))
        self.bg = CTkLabel(self.mainFrame, text="", image = self.bgImage)
        self.bg.place(x=0,y=0)
        self._createLabelPlayer()
        self.ipLabel = CTkLabel(self.mainFrame,text="Votre code d'acces à partager\n avec vos ami(e)s : " + gethostbyname(gethostname()),bg_color='white',text_color='black', font=('Roboto Bold', 25))
        self.ipLabel.place(x=120,y=100)
        self.copyipbutton : Bouton = Bouton(self.window, self, 500, 170, width=40, heigth=40, file=APP_PATH + "/../media/assets/copy_button.png", son="button", command=self.__copyIp)    
        self.colorLabel = CTkLabel(self.mainFrame, text="", bg_color='white',text_color='black', font=('Roboto Bold', 25))
        self.colorLabel.place(x=180, y=200)

    def _createLabelPlayer(self):
        self.updatedConnection = CTkLabel(self.mainFrame,text=f"Il y a {self.index} joueur(s) connecté(s) ... \n en attente de {4-self.index} autres",bg_color='white',text_color='black', font=('Roboto Bold', 25))
        self.updatedConnection.place(x=140,y=30)

    def backMenuServerSide(self):
        self.retourServer : Bouton = Bouton(
            self.window, self, 200, 255, width=200, heigth=33, 
            file=APP_PATH + r"/../media/assets/retour_serveur.png", son="button", 
            command= lambda : self.multiplayerController.closeServ())   

    def onConnection(self):
        self.index+=1
        self.updatedConnection.destroy()
        self._createLabelPlayer()

    def onConnectionClient(self):
        self.updatedConnection.destroy()
        self.updatedConnection = CTkLabel(self.window,text=f"En attente du meneur de jeu ... ",bg_color='white',text_color='black')
        self.updatedConnection.configure(font=('Roboto Bold', 25))
        self.updatedConnection.place(x=140,y=50)


    def close(self):
        _deleteChilds(self.window)