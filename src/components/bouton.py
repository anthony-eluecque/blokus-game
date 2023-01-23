from components.soundclass import Sound
from tkinter import Button
from customtkinter import CTk
from tkinter import PhotoImage
from PIL.Image import ANTIALIAS
from PIL.Image import open as openImg
from PIL.ImageTk import PhotoImage as PhotoImg

class Bouton(Button):
    """
    Classe qui hérite de la classe Button de tkinter et de la classe Sound
    Permet de passer par paramètre le son , ainsi que tous les attributs d'un bouton tkinter.
    Respecte notamment les principes SOLID.
    """
    
    def __init__(
        self,window:CTk,view,xpos,ypos,
        file:str|None = None,command=None, 
        width = 250, heigth = 250,
        text="template",son:str|None=None,*args,**kwags)->None:
        self.command = command

        if file:
            self.image = PhotoImage(file = file)
            self.imagesized = openImg( file )
            self.imagesized = self.imagesized.resize( ( width - 30, heigth - 10 ), ANTIALIAS )
            self.imagesized = PhotoImg( self.imagesized )
            super().__init__(window,image=self.image,text=text,bg="white",highlightthickness=0,bd=0,border=0)
        else:
            super().__init__(window,text=text,bg="white",highlightthickness=0,bd=0,border=0)
        
        self.window = window
        self.view = view 
        self.xpos = xpos
        self.ypos = ypos
        self.width = width
        self.heigth = heigth
        super().configure(width=width,height=heigth,command=self.callbackButton)
        super().bind( "<Enter>", self.MouseEnter )
        super().bind( "<Leave>", self.MouseExit )
        super().place(x=self.xpos,y=self.ypos)

        if son:
            self.sound = Sound(son)

    def callbackButton(self):
        """
        Callback permettant d'appeler la commande associé au bouton si elle existe
        Ainsi que de jouer un son si celui-ci a été associé au bouton.
        """
        if self.command:
            if self.sound:
                self.sound.play()
            self.command()
            
    def MouseEnter( self, e ):
        super().configure( width = self.width - 30, height = self.heigth - 10, image = self.imagesized )
        super().place( x = self.xpos + 15, y = self.ypos + 5 )

    def MouseExit( self, e ):
        super().configure( width = self.width, height = self.heigth, image = self.image )
        super().place( x = self.xpos, y = self.ypos )