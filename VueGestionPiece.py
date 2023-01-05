from typing_extensions import Self


import customtkinter
from PIL import Image,ImageTk
from tkinter import RAISED, Canvas
import math
from rotationBouton import rotationBouton
from inversionBouton import inversionBouton
import tkinter

class VueGestionPiece:

    def __init__(self:Self,window:customtkinter.CTk,frame,master):

        self.window = window
        self.canvas_piece = None
        self.frame = frame
        self.master = master
        self.rotateButton = None
        self.inversionButton = None
    
    def getXSouris(self:Self)->int:
        return self.window.winfo_pointerx() - self.window.winfo_rootx()

    def getYSouris(self:Self)->int:
        return self.window.winfo_pointery() - self.window.winfo_rooty()


    def onMotion(self:Self,e,width,heigh):
        if self.canvas_piece:
            self.new_x = self.getXSouris() - width//2
            self.new_y = self.getYSouris() - heigh//2
            self.canvas_piece.place(x=self.new_x,y=self.new_y)  
 
    def onDrop(self:Self,e,width,heigh):
        self.abs_x = self.getXSouris() - width//2
        self.abs_y = self.getYSouris() - heigh//2

        if 60<=self.abs_x<=660 and 150<=self.abs_y<=750 :

            x_round = self.round_down(self.abs_x)
            y_round = self.round_down(self.abs_y)

            if self.canvas_piece:
                self.canvas_piece.destroy()
            self.emitToGrille(x_round-60,y_round-150)

    def emitToGrille(self:Self,x,y):
        if self.rotateButton:
            self.master.callbackPiece(self.file,x,y,self.rotateButton.angle)

    def round_down(self:Self,n, decimals=2)->int:
        multiplier = 10 ** decimals
        result =  int(math.floor(n * multiplier) / multiplier)
        return (result//30)*30

    def addImageToGrid(self:Self,f,widget_location):
        if self.canvas_piece:
            self.canvas_piece.destroy()
        if self.rotateButton:
            if self.rotateButton.rotation:
                self.rotateButton.rotation.destroy()
        if self.inversionButton:
            if self.inversionButton.inversion :
                self.inversionButton.inversion.destroy()
                
        
        self.file = f
        img=Image.open(f)
        w,h=img.size 


        self.canvas_piece = Canvas(
            self.window, 
            width=w, 
            height=h, 
            bd=0, 
            highlightthickness=0, 
            bg="white"
        )
        self.img = tkinter.PhotoImage(file=f)
        self.png_piece = self.canvas_piece.create_image(0,0,image=self.img,anchor = "nw" )   
       
        self.canvas_piece.place(x=widget_location[0],y=widget_location[1])
        self.canvas_piece.bind('<B1-Motion>',lambda e :self.onMotion(e,w,h))
        self.canvas_piece.bind('<ButtonRelease-1>',lambda e : self.onDrop(e,w,h))
        
        self.rotateButton = rotationBouton(
            self.window,
            self.canvas_piece,
            self.png_piece,
            f
        )

        self.inversionButton = inversionBouton(
            self.window,
            self.canvas_piece,
            self.png_piece,
            f,
            self.rotateButton
        )

        # self.rotateButton = rotationBouton(
        #     self.canvas_piece,
        #     self.png_piece,
        #     self.window,
        #     f
        # )
