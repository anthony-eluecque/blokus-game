import sys
sys.path.append('./controller/')

from tkinter import BOTH, Canvas
from tkinter import Tk
import tkinter
from tkinter.messagebox import YES
from typing_extensions import Self
from PIL import Image,ImageTk
import customtkinter

from controller.plateau import Plateau
from controller.player import Player
from controller.checkIn import *
from controller.pieces import Pieces

from VuePiece import VuePiece

from VueGrilleJeu import VueGrilleJeu

class VueBlokus():

    def __init__(self):

        self.joueurs = ["Bleu","Jaune","Vert","Rouge"]
        self.index = 0
        self.actual_player = Player(self.joueurs[self.index])

        self.plateau = Plateau(20,20)


        self.window = customtkinter.CTk()
        self.window.geometry("1575x900")
        self.window.title("Jeu Blokus")

        self.vue_piece = VuePiece(self.window,Player('Bleu'),self)
        self.grille_jeu = VueGrilleJeu(self.window, 600, 600)

        self.window.mainloop()
    
    def callbackPiece(self,file,x:int,y:int):
        self.grille_jeu.addPieceToGrille(file,x,y)
        self.nextPlayer()
        self.displayPiecesPlayer()
        

    def displayPiecesPlayer(self:Self):
        self.vue_piece = VuePiece(self.window,self.actual_player,self)

    def nextPlayer(self:Self)->None:
        self.index= (self.index+1)%4
        self.actual_player =  Player(self.joueurs[self.index])
    


if __name__ ==  "__main__":
    app = VueBlokus()  



