from tkinter import Canvas
from customtkinter import CTk
from PIL import Image
from tkinter import PhotoImage


class grille:

    def __init__(self,window:CTk,largeur:int,hauteur:int):

        self.liste_piece = []
        self.window = window

        self._canvasCreation(largeur,hauteur)
        self._gridCreation(largeur)
        self._playersCorner(largeur,hauteur)
        self._configWidget()

    def _canvasCreation(self,w:int,h:int):
        self.canvas = Canvas(self.window,width=w,height=h,bd=0,highlightthickness=0,bg='white')

    def _gridCreation(self,largeur:int):
        for i in range(0,largeur,largeur//20):
            self.canvas.create_line(0,i,largeur,i)
            self.canvas.create_line(i,0,i,largeur)
        

    def _playersCorner(self,largeur:int,hauteur:int):

        self.depart_bleu = "#%02x%02x%02x" % (100, 149, 237)
        self.depart_vert = "#%02x%02x%02x" % (127, 221, 76)
        self.depart_jaune = "#%02x%02x%02x" % (247, 255, 60)
        self.depart_rouge = "#%02x%02x%02x" % (222, 41, 22)

        self.canvas.create_rectangle(0, hauteur -30, 30, hauteur, fill=self.depart_vert)
        self.canvas.create_rectangle(largeur - 30, 0, largeur, 30, fill=self.depart_jaune)
        self.canvas.create_rectangle(largeur - 30, hauteur - 30, largeur, hauteur, fill=self.depart_rouge)
        self.canvas.create_rectangle(0, 0, 30, 30, fill=self.depart_bleu)


    def _configWidget(self):
        self.canvas.place(x=60,y=150)
        self.canvas.bind('<Motion>',self._callback)

    def _addPieceToGrille(self,f:str,coord_x:int,coord_y:int):
        
        img=Image.open(f)
        w,h=img.size
        piece_canvas = Canvas(self.window, width=w, height=h, bd=0, highlightthickness=0, relief='ridge')
        img = PhotoImage(file=f)
        piece_canvas.create_image(0,0,image=img,anchor = "nw" )
        piece_canvas.place(x=coord_x*30+60,y=coord_y*30+150)
        self.liste_piece.append([f,piece_canvas,img])

    def _callback(self,e):
        x= e.x
        y= e.y        
        # print(f"Pointer is currently at : x:{x}  y:{y}")
