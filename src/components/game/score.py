from models.Player import Player
from customtkinter import CTkFrame,CTkLabel,CTkFont,CTk

class score:
    """
    Classe gérant la partie du jeu sur l'affichage des éléments externes au drag & drop
    (affichage du tour du joueur, nombre de pièce du joueur)
    """

    liste_player = ["Bleu","Jaune","Vert","Rouge"]
    color_player = ["#3D5ECC","#F9DE2F","#45A86B","#FF0004"]

    def __init__(self,window:CTk,player:Player)->None:

        self.window = window
        self.player = player 
        self.frame = CTkFrame(master=self.window,fg_color="white")
        self.index : int
        self._configGrid()
        self._createWidgets()


    def _configGrid(self)->None:
        """
        Fonction permettant de configurer la frame
        """
        self.frame.grid_rowconfigure(0,weight=1)
        self.frame.grid_rowconfigure(1,weight=1)
        self.frame.grid_columnconfigure(0,weight=1)

    def _createWidgets(self,index : int = 0)->None:
        """
        Fonction permettant la création de tous les widgets ainsi que leur configuration

        Args:
            index (int, optional): Defaults to 0.
        """
        self.index = index
        self._createCounterPiecePlayer()
        self._createTourPlayer()
        self._configWidgets()

    def _createCounterPiecePlayer(self)->None:
        """
        Création du label du nombre de pièce pour un joueur 
        """
        self.label_player = CTkLabel(
            master=self.frame,
            text= str(self.player.getNbPieces()) +  " Pièces Restantes", 
            font= CTkFont(family="Roboto Medium", size=40),
            text_color=self.color_player[self.index],
        )
    
    def _createTourPlayer(self)->None:
        """
        Création du label pour savoir c'est au tour de quel joueur de jouer.
        """
        self.label_tour = CTkLabel(
            master=self.frame,
            text="Joueur " + self.liste_player[self.index], 
            font= CTkFont(family="Roboto Medium", size=40),
            text_color=self.color_player[self.index],
        )

    def _destroyWidgets(self)->None:
        """
        Fonction permettant la destruction des widgets afin de les mettre à jour 
        """
        self.label_player.destroy()
        self.label_tour.destroy()

    def _configWidgets(self)->None:
        """
        Fonction permettant la configuration de chaque Widget de la Frame
        """

        self.label_player.grid(row=1,column=0)
        self.label_tour.grid(row=0,column=0)

        self.frame.grid_propagate(False)
        self.frame.configure(width=600,height=120)
        self.frame.place(x=60,y=10)


    def nextPlayer(self, index : int)->None:
        """Fonction permettant de mettre à jour l'affichage

        Args:
            index (int): C'est à quel joueur de jouer.
        """
        self._destroyWidgets()
        self._createWidgets(index)