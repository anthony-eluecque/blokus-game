from typing_extensions import Self

from controller.player import Player
import customtkinter
from tkinter import BOTH, Canvas, PhotoImage
from PIL import Image,ImageTk
import tkinter
from VueGestionPiece import VueGestionPiece

class VueNbPieceJoueur():

    def __init__(self: Self, window: customtkinter.CTkFrame, player : Player):
        self.index : int = 0
        self.window : customtkinter.CTkFrame = window
        self.player : Player = player
        # PASSE PAR DES CONSTANTES DANS LE FICHIER CONSTANTE, TU UTILISES TOUJOURS LES MEME
        self.color_player : list = ["#3D5ECC","#F9DE2F","#45A86B","#FF0004"]
        self.UI()


    def UI(self:Self):
        self.label = customtkinter.CTkLabel(
            master=self.window,
            text= str(self.player.getNbPieces()) +  " Pièces Restantes", 
            text_font=("Roboto Medium", 40), 
            text_color=self.color_player[self.index],
        )
        self.label.grid(row=1,column=0)

    def nextPlayer(self:Self, player:Player):
        self.player = player
        self.index = (self.index+1)%4
        self.label.destroy()
        self.UI()

# if __name__ == "__main__":
#     p1 = Player("Bleu")
#     window = customtkinter.CTkFrame()
#     v = VueNbPieceJoueur(window, p1)
