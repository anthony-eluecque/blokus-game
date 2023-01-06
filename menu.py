import tkinter
from unicodedata import name
import customtkinter as ctk
from customtkinter import CTkImage
from PIL import ImageTk
from PIL import Image
from tkinter import BOTH, Canvas, PhotoImage
from tkinter import Tk
import tkinter
from tkinter.messagebox import YES
from typing_extensions import Self
from PIL import Image,ImageTk
from mainWindow import VueBlokus
from VueRegles import VueRegles
import os
from VueScore import VueScore

import sys
sys.path.append('./controller/')
from controller.plateau import Plateau



class Menu():

    def __init__(self: Self,window : ctk.CTk, longueur = 700, hauteur = 700):

        self.window = window
        self.window.title("jeu Blokus")
        self.window.iconbitmap('./Icon/icon.ico')
        self.window.resizable(width=False, height=False)

        self.UI(700, 700)
        self.window.mainloop()
        
    def UI(self :Self, hauteur, longueur):
        self.window.geometry(str(longueur) + 'x' + str(hauteur))
        self.backgroundImage = Image.open("./assets/carre.png")
        self.background = ImageTk.PhotoImage(self.backgroundImage)
        self.label = tkinter.Label(self.window, image = self.background, bd = 0)
        self.label.place(x = 0,y = 0)
        
        # Bouton jouer
        self.backgroundButtunPlay = CTkImage(Image.open(os.path.join("./assets/button_play.png")),size=(158,49))
        self.button1 = ctk.CTkButton(
            master=self.window, 
            text='', 
            image = self.backgroundButtunPlay, 
            command = self.playButton, 
            border_width=0, 
            fg_color="white", 
            bg_color= "white", 
            hover_color="white"
        )
        self.button1.place(relx=0.5, rely=0.55, anchor=ctk.CENTER)

        # Bouton Règles
        self.backgroundButtunRules = CTkImage(Image.open(os.path.join("./assets/button_rules.png")),size=(196,49))
        self.button2 = ctk.CTkButton(
            master=self.window, 
            text='', 
            image = self.backgroundButtunRules, 
            command = self.rulesButton, 
            border_width=0, 
            fg_color="white", 
            bg_color= "white", 
            hover_color="white"
        )
        self.button2.place(relx=0.499, rely=0.65, anchor=ctk.CENTER)       

        # Bouton Statistiques
        self.backgroundButtunStats = CTkImage(Image.open(os.path.join("./assets/button_stats.png")),size=(221,49))
        self.button3 = ctk.CTkButton(
            master=self.window, 
            text='', 
            image = self.backgroundButtunStats, 
            command = self.statsButton, 
            border_width=0, 
            fg_color="white", 
            bg_color= "white", 
            hover_color="white"
        )
        self.button3.place(relx=0.493, rely=0.75, anchor=ctk.CENTER)   

        
    def playButton(self: Self):

        self.label.destroy()
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()

        plateau = Plateau(20,20)

        VueBlokus(self,self.window,plateau)
    
    def rulesButton(self: Self):
        self.label.destroy()
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        VueRegles(self, self.window)

    def statsButton(self: Self):
        self.label.destroy()
        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()

    def emitCB(self : Self):
        self.UI(700, 700)

    def emitFinishGame(self:Self,joueurs):
        # Faire ici
        self.UI(700,700)

        classement = {}

        for joueur in joueurs :
            for numPiece in joueur.pieces.pieces_joueurs:
                piece = joueur.jouerPiece(numPiece-1)
                for line in piece:
                    for square in line:
                        if square == 1:
                            joueur.removeScore()
        
            print(f"Score du joueur {joueur.couleur} : {joueur.score}")

            classement[joueur.couleur]=joueur.score
        VueScore(self,self.window,{k: v for k, v in sorted(classement.items(), key=lambda item: abs(item[1]))})


if __name__ == "__main__":
    window = ctk.CTk()
    app = Menu(window) 
