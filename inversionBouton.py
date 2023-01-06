from typing_extensions import Self
from tkinter import Button,PhotoImage,Canvas
from PIL import Image, ImageTk,ImageOps

class inversionBouton():

    def __init__(self:Self,master,piece,pngPiece,filePiece,parent) -> None:

        self.master = master
        self.inversion = None 
        self.nbInversion : int = 0 
        self.pngPiece = pngPiece
        self.filePiece = filePiece
        self.piece = piece
        self.parent = parent

        self.UI()

    def UI(self:Self)->None:
        if self.inversion:
            self.inversion.destroy()
        self.bgButton = PhotoImage(file="./assets/button_inversion.png")
        self.inversion = Button(
            master = self.master,
            image = self.bgButton,
            text="",
            bg="white",
            highlightthickness=0,
            bd=0,
            border=0,
            command=lambda:self.inversionImage(self.piece)
        )
        self.inversion.place(x=900,y=665)

    def inversionImage(self,piece:Canvas)->None:
        self.parent.reversePiece(piece)     


        


    


