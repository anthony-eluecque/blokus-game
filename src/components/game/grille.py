from tkinter import Canvas
from customtkinter import CTk
from PIL import Image
from tkinter import PhotoImage


class grille:
    """
    Classe permettant l'affichage d'une grille de blokus (20x20)
    Ne gère que la partie graphique
    """

    def __init__(self,window:CTk,largeur:int,hauteur:int)->None:

        self.liste_piece = []
        self.window = window

        self._canvasCreation(largeur,hauteur)
        self._gridCreation(largeur)
        self._playersCorner(largeur,hauteur)
        self._configWidget()

    def _canvasCreation(self,w:int,h:int)->None:
        """Fonction permttant de crée un Canvas pour afficher la grille.

        Args:
            w (int): width => largeur du canvas
            h (int): height => hauteur du canvas
        """
        self.canvas = Canvas(self.window,width=w,height=h,bd=0,highlightthickness=0,bg='white')

    def _gridCreation(self,largeur:int)->None:
        """Fonction permettant la création du quadrillage de la grille.

        Args:
            largeur (int): la largeur de la grille
        """
        for i in range(0,largeur,largeur//20):
            self.canvas.create_line(0,i,largeur,i)
            self.canvas.create_line(i,0,i,largeur)
        

    def _playersCorner(self,largeur:int,hauteur:int)->None:
        """Fonction permettant la création des 4 corners pour indiquer ou chaque joueur commence

        Args:
            largeur (int): la largeur de la grille
            hauteur (int): la hauteur de la grille
        """

        self.depart_bleu = "#%02x%02x%02x" % (100, 149, 237)
        self.depart_vert = "#%02x%02x%02x" % (127, 221, 76)
        self.depart_jaune = "#%02x%02x%02x" % (247, 255, 60)
        self.depart_rouge = "#%02x%02x%02x" % (222, 41, 22)

        self.canvas.create_rectangle(0, hauteur -30, 30, hauteur, fill=self.depart_vert)
        self.canvas.create_rectangle(largeur - 30, 0, largeur, 30, fill=self.depart_jaune)
        self.canvas.create_rectangle(largeur - 30, hauteur - 30, largeur, hauteur, fill=self.depart_rouge)
        self.canvas.create_rectangle(0, 0, 30, 30, fill=self.depart_bleu)


    def _configWidget(self)->None:
        """
        Fonction permettant de configurer les widgets et d'initialiser les callbacks
        """
        self.canvas.place(x=60,y=150)
        self.canvas.bind('<Motion>',self._callback)

    def _addPieceToGrille(self,f:str,coord_x:int,coord_y:int)->None:
        """Fonction permettant de placer un cube d'une couleur sur la grille.
        On peut ainsi gérer le soucis de transparence des canvas

        Args:
            f (str): le fichier de l'image 
            coord_x (int): la coordonné en x de la grille entre 0 et 19 
            coord_y (int): la coordonné en y de la grille entre 0 et 19 
        """
        img=Image.open(f)
        w,h=img.size
        piece_canvas = Canvas(self.window, width=w, height=h, bd=0, highlightthickness=0, relief='ridge')
        img = PhotoImage(file=f)
        piece_canvas.create_image(0,0,image=img,anchor = "nw" )
        piece_canvas.place(x=coord_x*30+60,y=coord_y*30+150)
        self.liste_piece.append([f,piece_canvas,img])

    def _callback(self,e)->None:
        """Fonction utilisé pour vérifié un callback
        (Test unitaire)

        Args:
            e (self): évênement
        """
        x= e.x
        y= e.y        
        # print(f"Pointer is currently at : x:{x}  y:{y}")
