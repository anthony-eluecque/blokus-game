from typing_extensions import Self

from controller.plateau import Plateau
from controller.player import Player
import customtkinter
from PIL import Image,ImageTk
from tkinter import RAISED, Canvas,LEFT


class VueGrilleJeu:

    def __init__(self:Self,window:customtkinter.CTk,wid:int,hei:int):
    
        self.liste_piece = []
        self.window : customtkinter.CTk = window
        self.canvas = Canvas(window, width=wid, height=hei,bd=0,highlightthickness=0, bg='white')
        for i in range(0,wid,wid//20):
            self.canvas.create_line(0,i,wid,i)
            self.canvas.create_line(i,0,i,wid)

        self.canvas.place(x=0,y=0)
        self.canvas.bind('<Motion>',self.callback)

    def addPieceToGrille(self,f:str,coord_x:int,coord_y:int):
        img=Image.open(f)
        w,h=img.size
        piece_canvas = Canvas(self.window, width=w, height=h, bd=0, highlightthickness=0, relief='ridge')
        img = ImageTk.PhotoImage(file=f)
        piece_canvas.create_image(0,0,image=img,anchor = "nw" )
        piece_canvas.place(x=coord_x*30,y=coord_y*30)
        self.liste_piece.append([f,piece_canvas,img])



    def callback(self,e):
        x= e.x
        y= e.y
        # print(f"Pointer is currently at : x:{x}  y:{y}")

    