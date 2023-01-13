from models.Player import Player
from customtkinter import CTkFrame,CTkLabel,CTkFont

class score:

    liste_player = ["Bleu","Jaune","Vert","Rouge"]
    color_player = ["#3D5ECC","#F9DE2F","#45A86B","#FF0004"]

    def __init__(self,window,player:Player):

        self.window = window
        self.player = player 
        self.frame = CTkFrame(master=self.window,fg_color="white")
        self.index : int
        self._configGrid()
        self._createWidgets()


    def _configGrid(self):
        self.frame.grid_rowconfigure(0,weight=1)
        self.frame.grid_rowconfigure(1,weight=1)
        self.frame.grid_columnconfigure(0,weight=1)

    def _createWidgets(self,index : int = 0):

        self.index = index
        self._createLabel()
        self._createCounterPiecePlayer()
        self._createTourPlayer()
        self._configWidgets()

    def _createCounterPiecePlayer(self):
        self.label_player = CTkLabel(
            master=self.frame,
            text= str(self.player.getNbPieces()) +  " Pièces Restantes", 
            font= CTkFont(family="Roboto Medium", size=40),
            text_color=self.color_player[self.index],
        )
    
    def _createTourPlayer(self):
        self.label_tour = CTkLabel(
            master=self.frame,
            text="Joueur " + self.liste_player[self.index], 
            font= CTkFont(family="Roboto Medium", size=40),
            text_color=self.color_player[self.index],
        )

    def _destroyWidgets(self):
        self.label_player.destroy()
        self.label_tour.destroy()


    def _createLabel(self):
        self.label = CTkLabel(
            master=self.frame,
            text="Joueur ", 
            font= CTkFont(family="Roboto Medium", size=40),
        )
        self.label.grid(row=0,column=0)

    def _configWidgets(self):

        self.label_player.grid(row=1,column=0)
        self.label_tour.grid(row=0,column=0)

        self.frame.grid_propagate(0)
        self.frame.configure(width=600,height=120)
        self.frame.place(x=60,y=10)


    def nextPlayer(self, index : int):
        self._destroyWidgets()
        self._createWidgets(index)