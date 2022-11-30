from typing_extensions import Self

from controller.plateau import Plateau
from controller.player import Player
import customtkinter
from PIL import Image,ImageTk
import tkinter
from tkinter import RAISED, Canvas,LEFT


class VueGrilleJeu:

    def __init__(self:Self,window:customtkinter.CTk,wid:int,hei:int):
    
        self.liste_piece = []
        self.window : customtkinter.CTk = window
        self.canvas = Canvas(window, width=wid, height=hei,bd=0,highlightthickness=0, bg='white')
        for i in range(0,wid,wid//20):
            self.canvas.create_line(0,i,wid,i)
            self.canvas.create_line(i,0,i,wid)
        self.depart_bleu = "#%02x%02x%02x" % (100, 149, 237)
        self.depart_vert = "#%02x%02x%02x" % (127, 221, 76)
        self.depart_jaune = "#%02x%02x%02x" % (247, 255, 60)
        self.depart_rouge = "#%02x%02x%02x" % (222, 41, 22)
        self.canvas.create_rectangle(0, hei -30, 30, hei, fill=self.depart_vert)
        self.canvas.create_rectangle(wid - 30, 0, wid, 30, fill=self.depart_jaune)
        self.canvas.create_rectangle(wid - 30, hei - 30, wid, hei, fill=self.depart_rouge)
        self.canvas.create_rectangle(0, 0, 30, 30, fill=self.depart_bleu)
        self.canvas.place(x=60,y=150)
        self.canvas.bind('<Motion>',self.callback)

    def addPieceToGrille(self:Self,f:str,coord_x:int,coord_y:int):
        img=Image.open(f)
        w,h=img.size
        piece_canvas = Canvas(self.window, width=w, height=h, bd=0, highlightthickness=0, relief='ridge')
        img = tkinter.PhotoImage(file=f)
        piece_canvas.create_image(0,0,image=img,anchor = "nw" )
        piece_canvas.place(x=coord_x*30+60,y=coord_y*30+150)
        self.liste_piece.append([f,piece_canvas,img])



    def callback(self:Self,e):
        x= e.x
        y= e.y
        # print(f"Pointer is currently at : x:{x}  y:{y}")

    