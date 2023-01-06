import sys
sys.path.append('./controller/')
import os

from tkinter.messagebox import YES
from typing_extensions import Self
from PIL import Image,ImageTk

from customtkinter import CTk,CTkLabel,CTkImage
from controller.plateau import Plateau
from controller.player import Player
from controller.checkIn import validPlacement,coordsBlocs,playerCanPlay

from testMap import MAP1
from VuePiece import VuePiece
from VueGrilleJeu import VueGrilleJeu
from VueStatsPlayer import VueStatsPlayer
from newGameButton import newGameButton
from stopGameButton import stopGameButton

class VueBlokus():

    def __init__(self,master,menu_window : CTk):

        self.master = master
        self.joueurs : list[Player] = [Player("Bleu"),Player("Jaune"),Player("Vert"),Player("Rouge")]
        self.index : int = 0
        self.actualPlayer : Player = self.joueurs[self.index]
        self.plateau = Plateau(20,20)       
        self.window = menu_window
        self.window.geometry("1300x800")
        self.window.title("Jeu Blokus")
        self.window.iconbitmap('./Icon/icon.ico')
        self.window.resizable(width=False, height=False)

        self.UI()
        self.window.mainloop()

    def UI(self):
        
        self.bgImage = CTkImage(Image.open(os.path.join("./assets/background_game.png")),size=(1300,800))
        self.bg = CTkLabel(self.window,text="",image = self.bgImage)
        self.bg.place(x = 0,y = 0)

        self.grilleJeu = VueGrilleJeu(self.window, 600, 600)
    
        self.vuePiece = VuePiece(self.window,Player('Bleu'),self)

        self.statsPlayer = VueStatsPlayer(self.window,self.actualPlayer)
        
        self.newGameButton = newGameButton(self,self.window)
        self.stopGameButton = stopGameButton(self,self.window)

        # Use a custom map
        # self.loadMap()

    def newGame(self):
        for child in self.window.winfo_children():
            child.destroy()
        VueBlokus(self.master,self.window)
    
    def stopGame(self):
        for child in self.window.winfo_children():
            child.destroy()
        self.master.emitCB()
    
    def loadMap(self:Self):
        
        indexJoueur = 0
        for couleur,pieces in MAP1.items():
            cheminFichierPiece = "./Pieces/" + couleur.upper()[0] + "/1.png"
            for piece in pieces :

                p = self.joueurs[indexJoueur].jouerPiece(piece[0]) 
                p = coordsBlocs(p,piece[1][1],piece[1][0])
                for coordx,coordy in p:
                    self.grilleJeu.addPieceToGrille(cheminFichierPiece,coordy,coordx)
                    self.plateau.setColorOfCase(coordx,coordy,indexJoueur)
                
                self.joueurs[indexJoueur].hasPlayedPiece(piece[0])
                self.joueurs[indexJoueur].removePiece(piece[0])

            indexJoueur +=1

        self.displayPiecesPlayer()

    def callbackPiece(self:Self,file:str,x:int,y:int,rotation:int,inversion:int):


        print(inversion)
        numPiece = int(file.split("/")[3].split(".")[0])
        # -1 car c'est une liste, ici c'est pas des png.

        piece = self.actualPlayer.jouerPiece(numPiece-1)
        couleurJoueur = self.actualPlayer.getCouleur()
        indexJoueur = self.joueurs.index(self.actualPlayer)

        # ----- Partie rotation
        nb_rotation = abs(rotation)//90
        print("nbrotate : ",nb_rotation)
        for i in range(nb_rotation):
            self.actualPlayer.pieces.rotate(numPiece-1)
            piece = self.actualPlayer.jouerPiece(numPiece-1)
        # ----- Partie inversion
        if inversion%2!=0:
            self.actualPlayer.pieces.reverse(numPiece-1)
            piece = self.actualPlayer.jouerPiece(numPiece-1)
            print(piece)
        pieceBlokus = coordsBlocs(piece,x//30,y//30)
        cheminFichierPiece = "./Pieces/" + couleurJoueur.upper()[0] + "/1.png"

        # ---- Vérification du placement
        if validPlacement(piece,y//30,x//30,self.plateau,self.actualPlayer):
            self.actualPlayer.removePiece(numPiece-1)

            for coordY,coordX in pieceBlokus:
                self.grilleJeu.addPieceToGrille(cheminFichierPiece,coordX,coordY)
                self.plateau.setColorOfCase(coordY,coordX,indexJoueur)

            self.actualPlayer.hasPlayedPiece(numPiece-1)    
            self.nextPlayer()
            self.displayPiecesPlayer()
            self.statsPlayer.tourJoueur.setNewColor()
            self.statsPlayer.nbPiecesPlayer.nextPlayer(self.actualPlayer)        
        # Partie reset rotation
        if nb_rotation>0:    
            self.actualPlayer.pieces.resetRotation(numPiece-1)
        
    

    def displayPiecesPlayer(self:Self):
        self.vuePiece.frame.destroy()
        self.vuePiece = VuePiece(self.window,self.actualPlayer,self)

    def nextPlayer(self:Self)->None:
        self.index= (self.index+1)%4
        self.actualPlayer =  self.joueurs[self.index]
        playable = False
        for i in range(0,2):
            if playerCanPlay(self.actualPlayer,self.plateau): 
                playable = True
                break
            self.index= (self.index+1)%4
            self.actualPlayer =  self.joueurs[self.index]

        # Si le joueur est dans l'incapacité de jouer
        if not playable:
            self.master.emitFinishGame(self.joueurs)








