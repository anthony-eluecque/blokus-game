from models.Player import Player
from customtkinter import CTk,CTkFrame
from PIL import Image
from tkinter import Canvas,PhotoImage
from utils.mouse_utils import getMouseX,getMouseY
from utils.game_utils import roundDown
from PIL import ImageOps,ImageTk,Image

class piecesManager:
    

    def __init__(self,window:CTk,player:Player,master):

        self.window = window
        self.master = master
        self.imagesPieces = player.pieces.getImagesPieces()
        self.listeCanvas = []

        self.nbrotation = 0
        self.nbinversion = 0

        self._makeFrame()
        self._displayPieces()


    def _makeFrame(self):

        self.frame = CTkFrame(master=self.master.window,fg_color="white")
        self._configureFrame()

    def _configureFrame(self):

        for i in range(0,7):
            self.frame.grid_columnconfigure(i,weight=2)
            self.frame.grid_rowconfigure(i,weight=2)

        self.frame.grid_propagate(False)
        self.frame.configure(width=550,height=650)
        self.frame.place(x=700,y=10)

    def _displayPieces(self):
        row = 750
        col = 50
        for i in range(len(self.imagesPieces)):
            self._makeImagePiece(self.imagesPieces[i],col,row)
            row+=100
            if i%5==4:
                col+= 160
                row = 750

    def _makeImagePiece(self,fichier,_col,_row):

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

    def _rotatePiece(self,e,canvas):
        self.nbrotation -= 90
        self._displayCanvas(canvas)

    def _reversePiece(self,e,canvas):
        self.nbinversion+=1
        self._displayCanvas(canvas)

    def _displayCanvas(self,canvas):

        for i in range(len(self.listeCanvas)):
            if self.listeCanvas[i][0]==canvas:
                canvas.delete("all")
                self.img = Image.open(self.listeCanvas[i][2]).rotate(self.nbrotation,expand=True)
                if self.nbinversion%2!=0:
                        self.img = ImageOps.mirror(self.img)
                self.imageCanvas =  ImageTk.PhotoImage(self.img)
                w,h = self.img.size
                canvas.config(width=w,height=h)
                canvas.create_image(0,0,image=self.imageCanvas,anchor = "nw")
                if self.nbrotation ==-360:
                    self.nbrotation = 0


    def onMotion(self,e,canvas,width,heigh):
        self.new_x = getMouseX(self.window) - width//2
        self.new_y = getMouseY(self.window) - heigh//2
        canvas.place(x=self.new_x,y=self.new_y)  
 
    def onDrop(self,e,canvas,width,height):
        self.abs_x = getMouseX(self.window) - width//2
        self.abs_y = getMouseY(self.window) - height//2

        if 60<=self.abs_x<=660 and 150<=self.abs_y<=750 :

            x_round = roundDown(self.abs_x)
            y_round = roundDown(self.abs_y)
            self.callbackPiece(canvas,x_round-60,y_round-150)

    def callbackPiece(self,canvas,x,y):
        for i in range(0,len(self.listeCanvas)):
            if len( self.listeCanvas ) - 1 >= i:
                if self.listeCanvas[i][0] == canvas:
                    self.master._callbackOnDrop(self.listeCanvas[i][2],x,y,self.nbrotation,self.nbinversion,canvas)


    def getIndexImage(self,e,listeCanvas):
        for i in range(0,len(listeCanvas)):
            if len( self.listeCanvas ) -1 >= i:
                if listeCanvas[i][0]==e.widget:
                    self.index_piece_dragdrop = i
                    widgetLocation = [getMouseX(self.window),getMouseY(self.window)]
                    # self.selectedPiece.displayPiece(self.imagesPieces[i],widgetLocation)

    
    def update(self,player:Player):
        
        self.imagesPieces = player.pieces.getImagesPieces()
        for piece in self.listeCanvas:
            piece[0].destroy()

        self.nbinversion = 0
        self.nbrotation = 0

        self.listeCanvas = []
        self.frame.destroy()
        self._makeFrame()
        self._displayPieces()