from components.game.reverseButton import reverseButton
from components.game.rotateButton import rotationButton
from PIL import ImageOps,ImageTk,Image

class buttonsManager:


    def __init__(self,window,piece,pngPiece,filePiece)->None:
        self.rotationButton = rotationButton(window,piece,pngPiece,filePiece,self)
        self.inversionButton = reverseButton(window,piece,pngPiece,filePiece,self)

        self.filePiece = filePiece
        self.piece = piece
        self.pngPiece = pngPiece
        self.window = window

    def rotationPiece(self,childPiece)->None:
        self.rotationButton.angle-=90    
        self._displayImage(childPiece)

    def reversePiece(self,childPiece)->None:
        self.inversionButton.nbInversion+=1
        self._displayImage(childPiece)

    def _displayImage(self,piece)->None:

        piece.delete("all")
        self.img = Image.open(self.filePiece).rotate(self.rotationButton.angle,expand=True)

        if self.inversionButton.nbInversion%2!=0:
            self.img = ImageOps.mirror(self.img)

        self.imageCanvas =  ImageTk.PhotoImage(self.img)
        w,h = self.img.size
        piece.config(width=w,height=h)
        piece.create_image(0,0,image=self.imageCanvas,anchor = "nw")
        if self.rotationButton.angle==-360:
            self.rotationButton.angle = 0
