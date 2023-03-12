from tkinter import PhotoImage,Button
from customtkinter import CTk,CTkLabel,CTkImage
from components.bouton import Bouton
from PIL import Image


class gameHistorique():

    def __init__(self,window,view,xcoord,ycoord,idPartie,dictPartie,command=None) -> None:
    
        self.window = window
        self.view = view
        
        self.id = str(idPartie)

        self.partie = dictPartie
        bgImage = CTkImage(Image.open("./media/assets/bg_histo.png"), size=(600, 55))
        self.bg = CTkLabel(self.window, text="", image = bgImage, fg_color="white")
        self.bg.place(x = xcoord, y = ycoord)

        self.labelTime = CTkLabel(self.window,text=self.partie["date"]+ " | " + self.partie["heure"], bg_color="white", fg_color="#%02x%02x%02x" % (244, 244, 244), text_color="black")
        self.labelTime.place(x=xcoord+40,y=ycoord+10)

        self.labelWinner = CTkLabel(self.window,text=self.partie["gagnant"],bg_color="white",text_color="black", fg_color="#%02x%02x%02x" % (244, 244, 244))
        self.labelWinner.place(x=xcoord+270,y=ycoord+10)

        self.button = Bouton(self.window,view=self.view,file="./media/assets/afficher.png",xpos=xcoord+480,ypos=ycoord,width=100,heigth=48,command= lambda : command(self.id),son="button")



    # x_pos+40 , y_pos+ 10 , i+

