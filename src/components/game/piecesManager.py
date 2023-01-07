from models.Player import Player
from customtkinter import CTk,CTkFrame
from PIL import Image
from tkinter import Canvas,PhotoImage
from utils.mouse_utils import getMouseX,getMouseY
from components.game.selectedPiece import selectedPiece

class piecesManager:
    

    def __init__(self,window:CTk,player:Player,master):

        self.window = window
        self.master = master
        self.imagesPieces = player.pieces.getImagesPieces()
        self.listeCanvas = []


        self._makeFrame()
        self._displayPieces()


    def _makeFrame(self):
        self.frame = CTkFrame(master=self.window,fg_color="white")
        self._configureFrame()

    def _configureFrame(self):

        for i in range(0,7):
            self.frame.grid_columnconfigure(i,weight=2)
            self.frame.grid_rowconfigure(i,weight=2)

        self.frame.grid_propagate(0)
        self.frame.configure(width=550,height=650)
        self.frame.place(x=700,y=10)
        self.selectedPiece = selectedPiece(self.window,self.frame,self.master)

    def _displayPieces(self):
        row = 0
        for i in range(len(self.imagesPieces)):
            self._makeImagePiece(self.imagesPieces[i],i%5,row)
            if i%5==4:
                row+=1

    def _makeImagePiece(self,fichier,_col,_row):

        img = Image.open(fichier)
        w,h = img.size
        self.canvas = Canvas(self.frame, width=w, height=h, bd=0, bg='white',highlightthickness=0, relief='ridge')
        self.canvas.grid(row=_row,column=_col)
        self.img = PhotoImage(file=fichier)
        self.canvas.create_image(0,0,image=self.img,anchor = "nw" )
        self.canvas.bind("<Button-1>",lambda e: self.getIndexImage(e,self.listeCanvas))
        self.listeCanvas.append([self.canvas,self.img])
    
    def getIndexImage(self,e,listeCanvas):
        for i in range(len(listeCanvas)):
            if listeCanvas[i][0]==e.widget:
                self.index_piece_dragdrop = i
                widgetLocation = [getMouseX(self.window),getMouseY(self.window)]
                self.selectedPiece.displayPiece(self.imagesPieces[i],widgetLocation)