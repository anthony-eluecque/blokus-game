from typing_extensions import Self
from tkinter import Button,PhotoImage,Canvas
from PIL import Image, ImageTk


class rotationBouton():

    def __init__(self,master,piece,pngPiece,filePiece,parent)->None:

        self.master = master
        self.rotation = None 
        self.angle : int = 0 
        self.pngPiece = pngPiece
        self.filePiece = filePiece
        self.piece = piece,
        self.parent = parent

        self.UI()


    def UI(self)->None:
        if self.rotation:
            self.rotation.destroy()
        self.bgButton = PhotoImage(file="./assets/button_rotation.png")
        self.rotation = Button(
            master = self.master,
            image=self.bgButton,
            text="",
            bg = 'white',
            highlightthickness=0,
            bd=0,
            border=0,
            command=lambda:self.rotationImage(self.piece)
        )
        self.rotation.place(x=700,y=665)
    
    def rotationImage(self,piece:Canvas):
        self.parent.rotationPiece(piece[0])