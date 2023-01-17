from components.soundclass import Sound
from tkinter import Button
from customtkinter import CTk
from tkinter import PhotoImage

class Bouton(Button):

    def __init__(
        self,window:CTk,view,xpos,ypos,
        file:str|None = None,command=None, 
        width = 250, heigth = 250,
        text="template",son:str|None=None,*args,**kwags)->None:

        self.command = command
        if file:
            self.image = PhotoImage(file = file)
            super().__init__(window,image=self.image,text=text,bg="white",highlightthickness=0,bd=0,border=0)
        else:
            super().__init__(window,text=text,bg="white",highlightthickness=0,bd=0,border=0)
        
        self.window = window
        self.view = view 
        self.width = width
        self.heigth = heigth
        super().configure(width=width,height=heigth,command=self.callbackButton)
        super().place(x=xpos,y=ypos)

        if son:
            self.sound = Sound(son)

    def callbackButton(self):
        if self.command:
            if self.sound:
                self.sound.play()
            self.command()
            



        


