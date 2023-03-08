from tkinter import PhotoImage,Button
from customtkinter import CTk,CTkLabel
from components.bouton import Bouton


class gameHistorique():

    def __init__(self,window,view,xcoord,ycoord,idPartie,dictPartie,command=None) -> None:
    
        self.window = window
        self.view = view
        self.id = idPartie

        self.partie = dictPartie
        
        
        self.labelHeureDate = CTkLabel(self.window,text=self.partie["date"]+ " | " + self.partie["heure"])
        self.button = Bouton(window,view=self.view,xpos=xcoord,ypos=ycoord,width=50,heigth=30,command=command)



