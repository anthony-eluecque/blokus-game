from typing_extensions import Self

from controller.player import Player
import customtkinter
from tkinter import BOTH, Canvas, PhotoImage,Label
from PIL import Image,ImageTk
import tkinter
from VueGestionPiece import VueGestionPiece

class VuePiece():

    def __init__(self,window:customtkinter.CTk,player:Player,master):
        
        self.window = window
        self.images_pieces = player.pieces.getImagesPieces()
        self.liste_canvas = []


        self.frame = customtkinter.CTkFrame(
            master=self.window,
            fg_color="white"
        )

        # self.frame.grid(rowspan=2,column=1,sticky='news')

        self.frame.grid_columnconfigure(0,weight=2)
        self.frame.grid_columnconfigure(1,weight=2)
        self.frame.grid_columnconfigure(2,weight=2)
        self.frame.grid_columnconfigure(3,weight=2)
        self.frame.grid_columnconfigure(4,weight=2)
        self.frame.grid_columnconfigure(5,weight=2)
        self.frame.grid_columnconfigure(6,weight=2)

        self.frame.grid_rowconfigure(0,weight=2)
        self.frame.grid_rowconfigure(1,weight=2)
        self.frame.grid_rowconfigure(2,weight=2)
        self.frame.grid_rowconfigure(3,weight=2)
        self.frame.grid_rowconfigure(4,weight=2)
        self.frame.grid_rowconfigure(5,weight=2)
        self.frame.grid_rowconfigure(6,weight=2)

        self.frame.grid_propagate(0)
        self.frame.configure(width=550,height=650)


        self.frame.place(x=700,y=10)
        # self.frame.config(width=750)

        self.gestionPiece = VueGestionPiece(self.window,self.frame,master)

        self.gestionImage()


    def gestionImage(self:Self):
        row = 0
        for i in range(len(self.images_pieces)):
            self.make_image(self.images_pieces[i],i%5,row)
            if i%5==4:
                row+=1

    def getXSouris(self:Self)->int:
        return self.window.winfo_pointerx() - self.window.winfo_rootx()

    def getYSouris(self:Self)->int:
        return self.window.winfo_pointery() - self.window.winfo_rooty()  

    def get_index_of_image(self,e,liste_canvas):
        for i in range(len(liste_canvas)):
            if liste_canvas[i][0]==e.widget:
                self.index_piece_dragdrop = i
                widget_location = [
                    self.getXSouris(),
                    self.getYSouris()
                ]
                self.gestionPiece.addImageToGrid(self.images_pieces[i],widget_location)

                

    def make_image(self:Self,f:str,placementcol,placementrow):
        img=Image.open(f)
        w,h=img.size

        self.canvas = Canvas(
            self.frame, 
            width=w, 
            height=h, 
            bd=0, 
            bg='white',
            highlightthickness=0, 
            relief='ridge'
        )
        self.canvas.grid(row=placementrow,column=placementcol)
        self.img = tkinter.PhotoImage(file=f)
        self.canvas.create_image(0,0,image=self.img,anchor = "nw" )
        self.canvas.bind("<Button-1>",lambda e: self.get_index_of_image(e,self.liste_canvas))
        self.liste_canvas.append([self.canvas,self.img])

        # self.window.wm_attributes('-transparentcolor','#000000')
        # self.window.wm_attributes('-topmost', True)

    #     self.label = Label(
    #         master=self.frame,
    #         # text="click-me")
    #         image=self.img)
    #     self.label.grid(row=placementrow,column=placementcol)
    #     self.label.bind('<Button-1>',self.prep)
    #     self.liste_canvas.append([self.label,self.img])

    # def prep(self,event):
    #     # event.widget.config(bg='light blue')    
    #     event.widget.focus_set()
    #     event.widget.bind('<Button-1>',lambda e: self.get_index_of_image(e,self.liste_canvas))
        


   


if __name__ == "__main__":
    pass