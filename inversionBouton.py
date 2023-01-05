from typing_extensions import Self
from tkinter import Button,PhotoImage,Canvas
from PIL import Image, ImageTk,ImageOps

class inversionBouton():

    def __init__(self:Self,master,piece,pngPiece,filePiece,rotationBouton) -> None:

        self.master = master
        self.inversion = None 
        self.nbInversion : int = 0 
        self.pngPiece = pngPiece
        self.filePiece = filePiece
        self.piece = piece

        self.rotationBouton = rotationBouton

        self.UI()

    def UI(self:Self)->None:

        if self.inversion:
            self.inversion.destroy()
        
        self.bgButton = PhotoImage(file="./assets/button_rotation.png")

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
        self.inversion.place(x=700,y=720)



    def inversionImage(self,piece:Canvas)->None:

        print(self.rotationBouton.angle)
        print(abs(self.rotationBouton.angle)//90)
        nb_rotation = abs(self.rotationBouton.angle)//90
        self.nbInversion+=1

        piece.delete(self.pngPiece)
        self.img = Image.open(self.filePiece)
        self.canvasImage =  ImageTk.PhotoImage(self.img)

        if self.nbInversion%2!=0:
            if nb_rotation == 1 or nb_rotation == 2:
                self.mirrorImg = ImageOps.flip(self.img)
            else:
                self.mirrorImg = ImageOps.mirror(self.img)
            self.canvasImage =  ImageTk.PhotoImage(self.mirrorImg)
    
        w,h = self.mirrorImg.size
        piece.config(width=w,height=h)
        piece.create_image(0,0,image=self.canvasImage,anchor="nw")


        


    


