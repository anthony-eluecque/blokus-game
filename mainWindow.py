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

from VuePiece import VuePiece

from VueGrilleJeu import VueGrilleJeu

class VueBlokus():

    def __init__(self):

        self.joueurs : list[Player] = [Player("Bleu"),Player("Jaune"),Player("Vert"),Player("Rouge")]
        self.index : int = 0
        self.actualPlayer : Player = self.joueurs[self.index]
        self.plateau = Plateau(20,20)


        self.window = customtkinter.CTk()
        self.window.geometry("1575x900")
        self.window.title("Jeu Blokus")

        self.vuePiece = VuePiece(self.window,Player('Bleu'),self)
        self.grilleJeu = VueGrilleJeu(self.window, 600, 600)
        

        self.saveButton = customtkinter.CTkButton(text="save", command=self.callbackSave)
        self.saveButton.place(x=600,y=700)

        self.window.mainloop()
    
    def callbackPiece(self:Self,file:str,x:int,y:int,rotation:int):

        numPiece = int(file.split("/")[3].split(".")[0])
        # -1 car c'est une liste, ici c'est pas des png.

        piece = self.actualPlayer.jouerPiece(numPiece-1)
        couleurJoueur = self.actualPlayer.getCouleur()
        indexJoueur = self.joueurs.index(self.actualPlayer)

        # ----- Partie rotation
        nb_rotation = abs(rotation)//90
        for i in range(nb_rotation):
            self.actualPlayer.pieces.rotate(numPiece-1)
            piece = self.actualPlayer.jouerPiece(numPiece-1)

        pieceBlokus = coordsBlocs(piece,x//30,y//30)
        cheminFichierPiece = "./Pieces/" + couleurJoueur.upper()[0] + "/1.png"
        
        # ---- Vérification du placement
        if validPlacement(piece,y//30,x//30,self.plateau,self.actualPlayer):
            self.actualPlayer.removePiece()

            for coordY,coordX in pieceBlokus:
                self.grilleJeu.addPieceToGrille(cheminFichierPiece,coordX,coordY)
                self.plateau.setColorOfCase(coordY,coordX,indexJoueur)

            self.actualPlayer.hasPlayedPiece(numPiece-1)            
            self.nextPlayer()
            self.displayPiecesPlayer()
        # Partie reset rotation
        if nb_rotation>0:    
            self.actualPlayer.pieces.resetRotation(numPiece-1)

    def displayPiecesPlayer(self:Self):
        self.vuePiece.frame.destroy()
        self.vuePiece = VuePiece(self.window,self.actualPlayer,self)

    def nextPlayer(self:Self)->None:
        self.index= (self.index+1)%4
        self.actualPlayer =  self.joueurs[self.index]
    
    def callbackSave(self):
        x = Canvas.winfo_rootx(self.grilleJeu.canvas)
        y = Canvas.winfo_rooty(self.grilleJeu.canvas)
        w = Canvas.winfo_width(self.grilleJeu.canvas) 
        h = Canvas.winfo_height(self.grilleJeu.canvas)
        directory = filedialog.asksaveasfilename(defaultextension="png", filetypes=[("PNG", ".png"), ("JPG", ".jpg"), ("JPEG", ".jpeg")])
        ImageGrab.grab((x, y, x+w, y+h)).save(directory)



if __name__ ==  "__main__":
    app = VueBlokus()  





