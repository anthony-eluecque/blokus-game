import sys
sys.path.append('./controller/')

from tkinter import BOTH, Canvas
from tkinter import Tk
import tkinter
from tkinter.messagebox import YES
from typing_extensions import Self
from PIL import Image,ImageTk
import customtkinter
from PIL import ImageGrab
import customtkinter
from tkinter import Canvas, filedialog

from controller.plateau import Plateau
from controller.player import Player
from controller.checkIn import validPlacement,coordsBlocs
from controller.pieces import Pieces

from VuePiece import VuePiece

from VueGrilleJeu import VueGrilleJeu

class VueBlokus():

    def __init__(self):

        self.joueurs : list[Player] = [Player("Bleu"),Player("Jaune"),Player("Vert"),Player("Rouge")]
        self.index : int = 0
        self.actual_player : Player = self.joueurs[self.index]
        self.plateau = Plateau(20,20)


        self.window = customtkinter.CTk()
        self.window.geometry("1575x900")
        self.window.title("Jeu Blokus")

        self.vue_piece = VuePiece(self.window,Player('Bleu'),self)
        self.grille_jeu = VueGrilleJeu(self.window, 600, 600)
        

        self.saveButton = customtkinter.CTkButton(text="save", command=self.CBsave)
        self.saveButton.place(x=600,y=700)

        self.window.mainloop()
    
    def callbackPiece(self:Self,file:str,x:int,y:int):

        num_piece = int(file.split("/")[3].split(".")[0])

        # -1 car c'est une liste, ici c'est pas des png.
        piece = self.actual_player.jouerPiece(num_piece-1)
        couleur_joueur = self.actual_player.getCouleur()
        index_joueur = self.joueurs.index(self.actual_player)

        if validPlacement(piece,y//30,x//30,self.plateau,self.actual_player):
            new_bloc = coordsBlocs(piece,x//30,y//30)
            chemin_piece = "./Pieces/" + couleur_joueur.upper()[0] + "/1.png"
            self.actual_player.removePiece()
            
            for y1,x1 in new_bloc:
                self.grille_jeu.addPieceToGrille(chemin_piece,x1,y1)
                self.plateau.setColorOfCase(y1,x1,index_joueur)
            self.nextPlayer()
            self.displayPiecesPlayer()


    def displayPiecesPlayer(self:Self):
        self.vue_piece = VuePiece(self.window,self.actual_player,self)

    def nextPlayer(self:Self)->None:
        self.index= (self.index+1)%4
        self.actual_player =  self.joueurs[self.index]
    
    # Save button callback
    def CBsave(self):
        # Getting canvas dimensions
        x = Canvas.winfo_rootx(self.grille_jeu.canvas)
        y = Canvas.winfo_rooty(self.grille_jeu.canvas)
        w = Canvas.winfo_width(self.grille_jeu.canvas) 
        h = Canvas.winfo_height(self.grille_jeu.canvas)

        # Open filedialog and set default extension to .png
        directory = filedialog.asksaveasfilename(defaultextension="png", filetypes=[("PNG", ".png"), ("JPG", ".jpg"), ("JPEG", ".jpeg")])
        # Save file to the directory previously given
        ImageGrab.grab((x, y, x+w, y+h)).save(directory)



if __name__ ==  "__main__":
    app = VueBlokus()  





