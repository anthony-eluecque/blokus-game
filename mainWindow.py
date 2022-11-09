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
from controller.checkIn import valid_placement,coords_blocs
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
    
    def callbackPiece(self:Self,file:str,x:int,y:int):

        num_piece = int(file.split("/")[3].split(".")[0])
        print("Numéro pièce : ",num_piece)

        # -1 car c'est une liste, ici c'est pas des png.
        piece = self.actual_player.jouerPiece(num_piece-1)
        couleur_joueur = self.actual_player.getCouleur()
        index_joueur = self.joueurs.index(couleur_joueur)

        # print("Position départ :",self.actual_player.getPositionDepart())
        # print("Position voulu par l'input : ",x//30,"-",y//30)

        # if valid_placement(piece,0,0,self.plateau,self.actual_player):
        # Kept for testing (drag & drop bug :c )

        print("Coord bloc : " ,x//30,y//30)


        if valid_placement(piece,x//30,y//30,self.plateau,self.actual_player):
            new_bloc = coords_blocs(piece,x//30,y//30)
            chemin_piece = "./Pieces/" + couleur_joueur.upper()[0] + "/1.png"
            print(new_bloc)
            for y1,x1 in new_bloc:
                self.grille_jeu.addPieceToGrille(chemin_piece,y1,x1)
                self.plateau.setColorOfCase(y1,x1,index_joueur)
            self.nextPlayer()
            self.displayPiecesPlayer()


    def displayPiecesPlayer(self:Self):
        self.vue_piece = VuePiece(self.window,self.actual_player,self)

    def nextPlayer(self:Self)->None:
        self.index= (self.index+1)%4
        self.actual_player =  Player(self.joueurs[self.index])
    


if __name__ ==  "__main__":
    app = VueBlokus()  



