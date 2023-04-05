from config import APP_PATH
from utils.window_utils import _resizeWindow, _createFrame, _deleteChilds
from tkinter import Entry, Label
from views.View import View
from PIL import ImageTk, Image
from utils.leaderboard_utils import openJson
from customtkinter import CTk
from components.bouton import Bouton
import os
from customtkinter import CTk, CTkImage, CTkLabel, CTkCanvas


class MultiplayerView(View):


    def __init__(self, controller, window: CTk, longueur=800, hauteur=800):
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
        self.mainFrame = _createFrame(self.window, 800, 800)

    def main(self,largeur = 800,hauteur = 800):
        _resizeWindow(self.window,largeur,hauteur)
        self._makeFrame()
        self._makeBackground()
        self.backHome: Bouton = Bouton(self.window, self, 300, 700, width=206, heigth=49, file=APP_PATH + "/../media/assets/buttun_rules_return.png", son="button", command=self.multiplayerController.goBackMenu)    

        self.entryServer = Entry(self.window,width=15)
        self.entryServer.configure(font=('Roboto Bold', 20))
        self.entryServer.place(x=150,y=235)

        self.entryClient = Entry(self.window,width=15)
        self.entryClient.configure(font=('Roboto Bold', 20))
        self.entryClient.place(x=150,y=505)

        self.createServer : Bouton = Bouton(
            self.window, self, 420, 230, width=206, heigth=49, 
            file=APP_PATH + r"/../media/assets/createMulti_button.png", son="button", 
            command= lambda : self.multiplayerController._createServer('0.0.0.0'))    
        
        self.joinServer : Bouton = Bouton(
            self.window, self, 420, 500, width=206, heigth=49, 
            file=APP_PATH + r"/../media/assets/joinMulti_button.png", son="button", 
            command=lambda : self.multiplayerController._joinServer(self.entryClient.get()))    


    def waitingScreen(self):
        
        _resizeWindow(self.window,600,300)
        self.mainFrame = _createFrame(self.window, 600, 300)
        self.bgImage = CTkImage(Image.open(APP_PATH + r"/../media/assets/waiting_bg.png"), size=(600, 300))
        self.bg = CTkLabel(self.window, text="", image = self.bgImage)
        self.bg.place(x=0,y=0)
        
        self.updatedConnection = CTkLabel(self.window,text=f"Il y a {self.index} joueur(s) connecté(s) ... \n en attente de {4-self.index} autres",bg_color='white',text_color='black')
        self.updatedConnection.configure(font=('Roboto Bold', 25))
        self.updatedConnection.place(x=140,y=100)


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
        self.updatedConnection.place(x=140,y=100)



    def close(self):
        _deleteChilds(self.window)