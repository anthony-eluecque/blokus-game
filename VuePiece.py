from typing_extensions import Self

from controller.player import Player
import customtkinter
from tkinter import BOTH, Canvas, PhotoImage
from PIL import Image,ImageTk
import tkinter
from VueGestionPiece import VueGestionPiece

class VuePiece():

    def __init__(self,window,player:Player,master):
        
        self.window = window
        self.images_pieces = player.pieces.getImagesPieces()
        self.liste_canvas = []

        print(self.images_pieces)

        self.frame = customtkinter.CTkFrame(master=self.window)

        self.frame.grid(rowspan=2,column=1,sticky='news')

        self.frame.grid_columnconfigure(0,weight=1)
        self.frame.grid_columnconfigure(1,weight=1)
        self.frame.grid_columnconfigure(2,weight=1)
        self.frame.grid_columnconfigure(3,weight=1)

        self.frame.grid_rowconfigure(0,weight=1)
        self.frame.grid_rowconfigure(1,weight=1)
        self.frame.grid_rowconfigure(2,weight=1)
        self.frame.grid_rowconfigure(3,weight=1)
        self.frame.grid_rowconfigure(4,weight=1)
        self.frame.grid_rowconfigure(5,weight=1)


        self.frame.place(x=600,y=0)

        self.gestionPiece = VueGestionPiece(self.window,self.frame,master)

        self.gestionImage()


    def gestionImage(self:Self):
        row = 0
        for i in range(len(self.images_pieces)):
            self.make_image(self.images_pieces[i],i%4,row)
            if i%4==3:
                row+=1
    def getLocation(self,e):
        x = e.x_root - self.frame.winfo_rootx()
        y = e.y_root - self.frame.winfo_rooty()
        return self.frame.grid_location(x,y)
   

    def get_index_of_image(self,e,liste_canvas):
        for i in range(len(liste_canvas)):
            if liste_canvas[i][0]==e.widget:
                self.index_piece_dragdrop = i
                widget_location = [
                    e.x_root,
                    e.y_root
                ]
                print(widget_location)
                self.gestionPiece.addImageToGrid(self.images_pieces[i],widget_location)

                

    def make_image(self:Self,f:str,placementcol,placementrow):
        img=Image.open(f)
        w,h=img.size
        self.canvas = Canvas(self.frame, width=w, height=h, bd=0, highlightthickness=0, relief='ridge')
        self.canvas.grid(row=placementrow,column=placementcol)
        self.img = ImageTk.PhotoImage(file=f)
        self.canvas.create_image(0,0,image=self.img,anchor = "nw" )
        self.liste_canvas.append([self.canvas,self.img])
        self.canvas.bind("<Button-1>",lambda e: self.get_index_of_image(e,self.liste_canvas))

   


if __name__ == "__main__":
    pass