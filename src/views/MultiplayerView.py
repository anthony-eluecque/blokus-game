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


    def waitingScreen(self):
        
        _resizeWindow(self.window,600,300)
        self.mainFrame = _createFrame(self.window, 600, 300)
        self.bgImage = CTkImage(Image.open(APP_PATH + r"/../media/assets/waiting_bg.png"), size=(600, 300))
        self.bg = CTkLabel(self.window, text="", image = self.bgImage)
        self.bg.place(x=0,y=0)
        
        self.updatedConnection = CTkLabel(self.window,text=f"Il y a {self.index} joueur(s) connecté(s) ... \n en attente de {4-self.index} autres",bg_color='white',text_color='black', font=('Roboto Bold', 25))
        self.updatedConnection.place(x=140,y=100)

        self.ipLabel = CTkLabel(self.window,text="Votre code d'acces à partager\n avec vos ami(e)s : " + gethostbyname(gethostname()),bg_color='white',text_color='black', font=('Roboto Bold', 25))
        self.ipLabel.place(x=120,y=180)

    def onConnection(self):
        self.index+=1
        self.updatedConnection.destroy()
        self.updatedConnection = CTkLabel(self.window,text=f"Il y a {self.index} joueur(s) connecté(s) ... \n en attente de {4-self.index} autres",bg_color='white',text_color='black')
        self.updatedConnection.configure(font=('Roboto Bold', 25))
        self.updatedConnection.place(x=140,y=100)

    def onConnectionClient(self):
        self.updatedConnection.destroy()
        self.updatedConnection = CTkLabel(self.window,text=f"En attente du meneur de jeu ... ",bg_color='white',text_color='black')
        self.updatedConnection.configure(font=('Roboto Bold', 25))
        self.updatedConnection.place(x=130,y=100)



    def close(self):
        _deleteChilds(self.window)