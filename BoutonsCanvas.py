from typing_extensions import Self

from controller.player import Player
import customtkinter
from tkinter import BOTH, Canvas
from tkinter import PhotoImage
from PIL import Image,ImageTk
import tkinter


class BoutonCanvas():

    def __init__(self,piece,png_piece,window,file_piece) -> None:
        
        self.window = window
        self.rotate = None
        self.png_piece = png_piece
        self.file_piece = file_piece
        self.angle : int = 0

        self.AjoutBoutons(piece)

    def AjoutBoutons(self,piece:Canvas):
        if self.rotate:
            self.rotate.destroy()

        self.backgroundButtonRotation = PhotoImage(file="./assets/button_rotation.png")

        self.rotate = customtkinter.CTkButton(
            master = self.window,
            image=self.backgroundButtonRotation,
            border_width=0,
            corner_radius=8,
            text="",
            bg_color="white",
            command=lambda:self.rotation_image(piece),
            bd=0
        )
        self.rotate.place(x=700,y=665)
    
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


    
