import sys
sys.path.append('./controller/')

from tkinter import BOTH, Canvas
from tkinter import Tk
import tkinter
from tkinter.messagebox import YES
from typing_extensions import Self
from PIL import Image,ImageTk
import customtkinter

from controller.player import Player

from VuePiece import VuePiece

from VueGrilleJeu import VueGrilleJeu

class VueBlokus():

    def __init__(self):
        self.window = customtkinter.CTk()
        self.window.geometry("1575x900")
        self.window.title("Jeu Blokus")

        self.vue_piece = VuePiece(self.window,Player('Vert'),self)
        self.grille_jeu = VueGrilleJeu(self.window, 600, 600)

        self.window.mainloop()
    
    def callbackPiece(self,file,x:int,y:int):
        self.grille_jeu.addPieceToGrille(file,x,y)


if __name__ ==  "__main__":
    app = VueBlokus()  



