from utils.mouse_utils import getMouseX,getMouseY
from utils.game_utils import roundDown
from PIL import Image
from tkinter import Canvas,PhotoImage
from components.game.buttonsManager import buttonsManager

class selectedPiece:

    def __init__(self,window,frame,master):

        self.window = window
        self.frame = frame
        self.master = master

        self.canvasPiece = None

    def callbackPiece(self,x,y):
    
        if self.buttonsManager.rotationButton:
            self.master._callbackOnDrop(self.file,x,y,self.buttonsManager.rotationButton.angle,self.buttonsManager.inversionButton.nbInversion)

    def displayPiece(self,file,widgetLocation):

        if self.canvasPiece:
            self.canvasPiece.destroy()

        self.file = file
        img = Image.open(file)
        w,h = img.size
        self._makeCanvas(w,h)

        self.img = PhotoImage(file=self.file)
        self.pngPiece = self.canvasPiece.create_image(0,0,image=self.img,anchor="nw")

        self.canvasPiece.place(x=widgetLocation[0],y=widgetLocation[1])
        self.canvasPiece.bind('<B1-Motion>',lambda e :self.onMotion(e,w,h))
        self.canvasPiece.bind('<ButtonRelease-1>',lambda e : self.onDrop(e,w,h))

        self.buttonsManager = buttonsManager(self.window,self.canvasPiece,self.pngPiece,file)


    def _makeCanvas(self,w,h):
        self.canvasPiece = Canvas(self.window,width=w,height=h,bd=0,highlightthickness=0,bg="white")


    def onMotion(self,e,width,heigh):
        if self.canvasPiece:
            self.new_x = getMouseX(self.window) - width//2
            self.new_y = getMouseY(self.window) - heigh//2
            self.canvasPiece.place(x=self.new_x,y=self.new_y)  
 
    def onDrop(self,e,width,height):
        self.abs_x = getMouseX(self.window) - width//2
        self.abs_y = getMouseY(self.window) - height//2

        if 60<=self.abs_x<=660 and 150<=self.abs_y<=750 :

            x_round = roundDown(self.abs_x)
            y_round = roundDown(self.abs_y)

            if self.canvasPiece:
                self.canvasPiece.destroy()
                
            self.callbackPiece(x_round-60,y_round-150)
