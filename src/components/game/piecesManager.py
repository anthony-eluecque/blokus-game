from models.Player import Player
from customtkinter import CTk,CTkFrame
from PIL import Image
from tkinter import Canvas,PhotoImage
from utils.mouse_utils import getMouseX,getMouseY
from utils.game_utils import roundDown
from PIL import ImageOps,ImageTk,Image

class piecesManager:
    """
    Classe permettant à un utilisateur de jouer les pièces de sa couleur.
    Celle-ci gère aussi le drag & drop de chaque pièce, ainsi que la rotation et l'inversion
    """

    def __init__(self,window:CTk,player:Player,master)->None:

        self.window = window
        self.master = master
        self.imagesPieces = player.pieces.getImagesPieces()
        self.listeCanvas = []

        self.nbrotation = 0
        self.nbinversion = 0

        self._makeFrame()
        self._displayPieces()


    def _makeFrame(self)->None:
        """
        Fonction permettant la création d'une Frame.
        """

        self.frame = CTkFrame(master=self.master.window,fg_color="white")
        self._configureFrame()

    def _configureFrame(self)->None:
        """
        Fonction permettant la configuration de la frame.
        """

        for i in range(0,7):
            self.frame.grid_columnconfigure(i,weight=2)
            self.frame.grid_rowconfigure(i,weight=2)

        self.frame.grid_propagate(False)
        self.frame.configure(width=550,height=745)
        self.frame.place(x=700,y=10)

    def _displayPieces(self)->None:
        """
        Fonction permettant d'afficher les pièces
        """
        row = 750
        col = 50
        for i in range(len(self.imagesPieces)):
            self._makeImagePiece(self.imagesPieces[i],col,row)
            row+=100
            if i%5==4:
                col+= 160
                if col==690:
                    row = 925
                    col -=40
                else:row = 750

    def _makeImagePiece(self,fichier:str,_col:int,_row:int)->None:
        """Fonction permettant la création de chaque pièce du joueur
        On configure notammet ici le click, le drag et le drop , ainsi que le clique droit pour la rotation
        et la molette de la souris pour l'inversion.

        Args:
            fichier (str): Le fichier de la pièce
            _col (int): Sa position en y
            _row (int): Sa position en x
        """

        img = Image.open(fichier)
        w,h = img.size
        canvas = Canvas(self.master.window, width=w, height=h, bd=0, bg='white',highlightthickness=0, relief='ridge')
        
        canvas.place(x=_row,y=_col)
        
        self.img = PhotoImage(file=fichier)
        canvas.create_image(0,0,image=self.img,anchor = "nw" )
        # self.canvas.bind("<Button-1>",lambda e: self.getIndexImage(e,self.listeCanvas))
        canvas.bind('<B1-Motion>',lambda e :self.onMotion(e,canvas,w,h))
        canvas.bind('<ButtonRelease-1>',lambda e : self.onDrop(e,canvas,w,h))
        canvas.bind('<Button-3>',lambda e: self._rotatePiece(e,canvas))
        canvas.bind('<MouseWheel>',lambda e: self._reversePiece(e,canvas))


        self.listeCanvas.append([canvas,self.img,fichier,_row,_col])

    def _rotatePiece(self,e,canvas:Canvas)->None:
        self.nbrotation -= 90
        self._displayCanvas(canvas)

    def _reversePiece(self,e,canvas:Canvas)->None:
        self.nbinversion+=1
        self._displayCanvas(canvas)

    def _displayCanvas(self,canvas:Canvas)->None:
        """Fonction permettant de mettre à jour la pièce sélectionner lors que l'on va fait tourner ou inverser.

        Args:
            canvas (Canvas): Le calque sous l'image de la pièce.
        """

        for i in range(len(self.listeCanvas)):
            if self.listeCanvas[i][0]==canvas:
                print(canvas)
                canvas.delete("all")
                self.img = Image.open(self.listeCanvas[i][2]).rotate(self.nbrotation,expand=True)
                if self.nbinversion%2!=0:
                        self.img = ImageOps.mirror(self.img)
                self.imageCanvas =  ImageTk.PhotoImage(self.img)
                w,h = self.img.size
                canvas.config(width=w,height=h)
                canvas.create_image(0,0,image=self.imageCanvas,anchor = "nw")
                self.listeCanvas[i][1] = self.imageCanvas
                if self.nbrotation ==-360:
                    self.nbrotation = 0


    def onMotion(self,e,canvas:Canvas,width:int,heigh:int)->None:

        """Callback activé lors du drag à la souris.
        Permet d'afficher la pièce aux nouvelles coordonnées

        Args:
            e : évènement callback
            canvas (Canvas): Le calque sous l'image de la pièce.
            width (int): La largeur de la pièce 
            heigh (int): La hauteur de la pièce
        """
        if self.nbrotation == 0 or self.nbrotation == -270:
            self.new_x = getMouseX(self.window) - width//2
            self.new_y = getMouseY(self.window) - heigh//2
        else: 
            self.new_x = getMouseX(self.window) - heigh//2
            self.new_y = getMouseY(self.window) - width//2
        canvas.place(x=self.new_x,y=self.new_y)  
 
    def onDrop(self,e,canvas:Canvas,width:int,height:int)->None:
        """Callback permettant la gestion du drop lorsque l'on lache la pièce après le drag.


        Args:
            e : évènement callback
            canvas (Canvas): Le calque sous l'image de la pièce.
            width (int): La largeur de la pièce 
            heigh (int): La hauteur de la pièce
        """
        # self.abs_x = getMouseX(self.window) - width//2
        # self.abs_y = getMouseY(self.window) - height//2

        if self.nbrotation == 0 or self.nbrotation == -270:
            self.abs_x = getMouseX(self.window) - width//2
            self.abs_y = getMouseY(self.window) - height//2
        else: 
            self.abs_x = getMouseX(self.window) - height//2
            self.abs_y = getMouseY(self.window) - width//2

        if 60<=self.abs_x<=660 and 150<=self.abs_y<=750 :

            x_round = roundDown(self.abs_x)
            y_round = roundDown(self.abs_y)
            self.callbackPiece(canvas,x_round-60,y_round-150)


    def callbackPiece(self,canvas:Canvas,x:int,y:int)->None:
        """Fonction permettant la transition entre le drop de la souris et l'envoie au parent 

        Args:
            canvas (Canvas): Le calque sous l'image de la pièce.
            x (int): La position en x sur le plateau de jeu entre 0 et 19
            y (int): La position en y sur le plateau de jeu entre 0 et 19
        """
        for i in range(0,len(self.listeCanvas)):
            if len( self.listeCanvas ) - 1 >= i:
                if self.listeCanvas[i][0] == canvas:
                    self.master._callbackOnDrop(self.listeCanvas[i][2],x,y,self.nbrotation,self.nbinversion,canvas)
            

   
    def update(self,player:Player)->None:
        """Fonction permettant de mettre à jour l'affichage lorsque l'on change de joueur
        -> Affiche les nouvelles pièces du joueur
        -> On détruit les anciennes en même temps pour éviter la surchage d'éléments sur la fenêtre

        Args:
            player (Player): _description_
        """
        self.imagesPieces = player.pieces.getImagesPieces()
        for piece in self.listeCanvas:
            piece[0].destroy()

        self.nbinversion = 0
        self.nbrotation = 0

        self.listeCanvas = []
        self.frame.destroy()
        
        self._makeFrame()
        self._displayPieces()