from typing_extensions import Self
from controller.player import Player
from customtkinter import CTkFrame,CTkLabel,CTkFont
from VueNbPieceJoueur import VueNbPieceJoueur
from VueTourJoueur import VueTourJoueur

class VueStatsPlayer():

    def __init__(self:Self,window,actualPlayer:Player):

        self.window = window
        self.actualPlayer = actualPlayer
        self.frame = CTkFrame(master=self.window,fg_color="white")
        self.UI()

    def UI(self:Self):

        self.frame.grid_rowconfigure(0,weight=1)
        self.frame.grid_rowconfigure(1,weight=1)
        self.frame.grid_columnconfigure(0,weight=1)

        self.label = CTkLabel(
            master=self.frame,
            text="Joueur ", 
            font= CTkFont(family="Roboto Medium", size=40),
        )
        self.label.grid(row=0,column=0)

        self.tourJoueur = VueTourJoueur(self.frame)
        self.nbPiecesPlayer = VueNbPieceJoueur(self.frame,self.actualPlayer)

        self.frame.grid_propagate(0)
        self.frame.configure(width=600,height=120)
        self.frame.place(x=60,y=10)



    