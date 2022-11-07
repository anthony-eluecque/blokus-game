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

        self.frame = customtkinter.CTkFrame(master=self.window,     
                    width=600,height=300)

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

    #  Drag & Drop
    # def moveCanvas(self,place_x,place_y,canvas):
    #     canvas.place(x=place_x,y=place_y)   

    # def getMotion(self,e,liste_widget):
        
    #     x = e.x_root - self.frame.winfo_rootx()
    #     y = e.y_root - self.frame.winfo_rooty()
    #     self.moveCanvas(x,y,liste_widget[self.index_piece_dragdrop][0])

    #     z = self.frame.grid_location(x,y)

    def getLocation(self,e):
        x = e.x_root - self.frame.winfo_rootx()
        y = e.y_root - self.frame.winfo_rooty()
        return self.frame.grid_location(x,y)

    def getXinRoot(self,e):
        return e.x_root

    def getXinParent(self,e):
        return e.x_root - self.frame.winfo_rootx()

    def getYinRoot(self,e):
        return e.y_root

    def getYinParent(self,e):
        return e.y_root - self.frame.winfo_rooty()
    

    def get_index_of_image(self,e,liste_canvas):
        for i in range(len(liste_canvas)):
            if liste_canvas[i][0]==e.widget:
                print(i,"piece numero : ",i+1)
                self.index_piece_dragdrop = i
                widget_location = [self.getXinRoot(e),self.getYinRoot(e)]
                self.gestionPiece.addImageToGrid(self.images_pieces[i],widget_location)

                

    def make_image(self:Self,f:str,placementcol,placementrow):
        img=Image.open(f)
        w,h=img.size
        # print(placementcol,placementrow)
        # print(w,h)
        self.canvas = Canvas(self.frame, width=w, height=h, bd=0, highlightthickness=0, relief='ridge')
        self.canvas.grid(row=placementrow,column=placementcol)
        self.img = ImageTk.PhotoImage(file=f)
        self.canvas.create_image(0,0,image=self.img,anchor = "nw" )
        self.liste_canvas.append([self.canvas,self.img])
        self.canvas.bind("<Button-1>",lambda e: self.get_index_of_image(e,self.liste_canvas))
        # self.canvas.bind("<B1-Motion>",lambda e:self.getMotion(e,self.liste_canvas))

   


if __name__ == "__main__":
    pass