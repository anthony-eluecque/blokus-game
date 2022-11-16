from typing_extensions import Self


import customtkinter
from PIL import Image,ImageTk
from tkinter import RAISED, Canvas
import math
from BoutonsCanvas import BoutonCanvas

class VueGestionPiece:

    def __init__(self:Self,window:customtkinter.CTk,frame,master):

        self.window = window
        self.canvas_piece = None
        self.frame = frame
        self.master = master
    
    def getXSouris(self)->int:
        return self.window.winfo_pointerx() - self.window.winfo_rootx()

    def getYSouris(self)->int:
        return self.window.winfo_pointery() - self.window.winfo_rooty()


    def onMotion(self,e):
        # print("x fenetre :",self.window.winfo_rootx())
        # print("y fenetre :",self.window.winfo_rooty())

        # print([e.x_root,e.x],[e.y_root,e.y])

        if self.canvas_piece:
            # self.new_x = e.x_root 
            # self.new_y = e.y_root 

            self.new_x = self.getXSouris()
            self.new_y = self.getYSouris()
            self.canvas_piece.place(x=self.new_x,y=self.new_y)  
 
    def onDrop(self,e):
        self.abs_x = self.getXSouris()
        self.abs_y = self.getYSouris()

        if 0<=self.abs_x<=600 and 0<=self.abs_y<=600 :
            x_round = self.round_down(self.abs_x)
            y_round = self.round_down(self.abs_y)
            print(self.abs_x,"----",self.abs_y)
            print(x_round," ---- ",y_round)
            # print(x_round,y_round)
            if self.canvas_piece:
                self.canvas_piece.destroy()
            self.emitToGrille(x_round,y_round)

    def emitToGrille(self,x,y):
        self.master.callbackPiece(self.file,x,y)

    def round_down(self,n, decimals=2)->int:
        multiplier = 10 ** decimals
        result =  int(math.floor(n * multiplier) / multiplier)

        # print(result)

        
        # if int(str(n)[1])>5:
        #     result+=50
        # print(result)
        return (result//30)*30


    def addImageToGrid(self,f,widget_location):
        if self.canvas_piece:
            self.canvas_piece.destroy()
        
        self.file = f
        img=Image.open(f)
        w,h=img.size 

        self.canvas_piece = Canvas(self.window, width=w, height=h, bd=0, highlightthickness=0, relief='ridge')
        self.img = ImageTk.PhotoImage(file=f)
        self.png_piece = self.canvas_piece.create_image(0,0,image=self.img,anchor = "nw" )   
       
        self.canvas_piece.place(x=widget_location[0],y=widget_location[1])
        self.canvas_piece.bind('<B1-Motion>',self.onMotion)
        self.canvas_piece.bind('<ButtonRelease-1>',self.onDrop)
        BoutonCanvas(self.canvas_piece,self.png_piece,self.window,f)
