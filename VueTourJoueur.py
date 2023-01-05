from typing_extensions import Self
import customtkinter
from tkinter import BOTH, Canvas, PhotoImage
from PIL import Image,ImageTk
import tkinter
from VueGestionPiece import VueGestionPiece
from controller.player import Player

class VueTourJoueur():

    def __init__(self: Self,frame: customtkinter.CTkFrame):

        self.index = 0
        # PASSE PAR DES CONSTANTES DANS LE FICHIER CONSTANTE, TU UTILISES TOUJOURS LES MEME 
        self.liste_player = ["Bleu","Jaune","Vert","Rouge"]
        self.color_player = ["#3D5ECC","#F9DE2F","#45A86B","#FF0004"]
        self.frame = frame
        self.UI()

    def UI(self):
        self.label = customtkinter.CTkLabel(
            master=self.frame,
            text="Joueur " + self.liste_player[self.index], 
            text_font=("Roboto Medium", 40), 
            text_color=self.color_player[self.index],
        )

        self.label.grid(row=0,column=0)


    def setNewColor(self):
        self.index = (self.index+1)%4
        self.label.destroy()
        self.UI()


# if __name__ == "__main__":
#     p1 = Player("Rouge")
#     window = customtkinter.CTk()
#     v = VueTourJoueur(window)
