from typing_extensions import Self
from tkinter import Button,PhotoImage,Canvas
from PIL import Image, ImageTk


class rotationBouton():

    def __init__(self,master,piece,png_piece,file_piece)->None:

        self.master = master
        self.rotation = None 
        self.angle : int = 0 
        self.png_piece = png_piece
        self.file_piece = file_piece
        self.piece = piece

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
            command=lambda:self.rotation_image(self.piece)
        )
        # self.rotation.place(x=15,y=15)
        self.rotation.place(x=700,y=665)
    
    def rotation_image(self,piece:Canvas):
                     
        # Add Angle to Simulate rotation
        self.angle-=90
        # First delete png from canvas
        piece.delete(self.png_piece)
        # Open Image rotated by 90,180,270,360 degree
        self.rotated_img = Image.open(self.file_piece).rotate(self.angle,expand=True)
        self.image_canvas =  ImageTk.PhotoImage(self.rotated_img)
        # Longueur & Hauteur de l'image
        w,h = self.rotated_img.size

        # Config du canvas (inversion hauteur & largeur)
        # Ajout de la nouvelle image rotate
        piece.config(width=w,height=h)
        piece.create_image(0,0,image=self.image_canvas,anchor = "nw")
        if self.angle==-360:
            self.angle = 0