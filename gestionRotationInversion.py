from typing_extensions import Self

from controller.player import Player
import customtkinter
from tkinter import BOTH, Canvas
from tkinter import PhotoImage
from PIL import Image,ImageTk
import tkinter
from tkinter import Button
from rotationBouton import rotationBouton
from inversionBouton import inversionBouton
from PIL import Image, ImageTk,ImageOps

class gestionRotationInversion():

    def __init__(self,window,piece,pngPiece,filePiece) -> None:
        
        self.rotationButton = rotationBouton(window,piece,pngPiece,filePiece,self)
        self.inversionButton = inversionBouton(window,piece,pngPiece,filePiece,self)
    
        self.filePiece = filePiece
        self.piece = piece 
        self.pngPiece = pngPiece
        self.window = window


    def rotationPiece(self,childPiece)->None:
            self.rotationButton.angle-=90    
            self.displayImage(childPiece)

    def reversePiece(self,childPiece)->None:
        self.inversionButton.nbInversion+=1
        self.displayImage(childPiece)

    def displayImage(self,piece)->None:

        piece.delete("all")
        self.img = Image.open(self.filePiece).rotate(self.rotationButton.angle,expand=True)
        nb_rotation = abs(self.rotationButton.angle)//90

        if self.inversionButton.nbInversion%2!=0:
            if nb_rotation == 1 or nb_rotation == 3:
                self.img = ImageOps.mirror(self.img)
            else:
                self.img = ImageOps.flip(self.img)

        self.imageCanvas =  ImageTk.PhotoImage(self.img)
        w,h = self.img.size
        piece.config(width=w,height=h)
        piece.create_image(0,0,image=self.imageCanvas,anchor = "nw")
        if self.rotationButton.angle==-360:
            self.rotationButton.angle = 0


    # def rotationPiece(self,childPiece)->None:

    #     self.rotationButton.angle-=90
    #     childPiece.delete("all")
    #     self.rotated_img = Image.open(self.filePiece).rotate(self.rotationButton.angle,expand=True)
    #     if self.inversionButton.nbInversion%2!=0:
    #         self.rotated_img = ImageOps.flip(self.rotated_img)
    #     self.imageCanvas =  ImageTk.PhotoImage(self.rotated_img)
    #     w,h = self.rotated_img.size
    #     childPiece.config(width=w,height=h)
    #     childPiece.create_image(0,0,image=self.imageCanvas,anchor = "nw")
    #     if self.rotationButton.angle==-360:
    #         self.rotationButton.angle = 0
    
    # def reversePiece(self,childPiece)->None:

    #     nb_rotation = abs(self.rotationButton.angle)//90
    #     self.inversionButton.nbInversion+=1

    #     childPiece.delete("all")
    #     self.img = Image.open(self.filePiece)
    #     self.canvasImage =  ImageTk.PhotoImage(self.img)
    #     if self.inversionButton.nbInversion%2!=0:
    #         if nb_rotation == 1 or nb_rotation == 2:
    #             self.mirrorImg = ImageOps.flip(self.img)
    #         else:
    #             self.mirrorImg = ImageOps.mirror(self.img)
    #             # self.mirrorImg = ImageOps.flip(self.img)
    #         self.canvasImage =  ImageTk.PhotoImage(self.mirrorImg)
    
    #     w,h = self.mirrorImg.size
    #     childPiece.config(width=w,height=h)
    #     childPiece.create_image(0,0,image=self.canvasImage,anchor="nw")


    