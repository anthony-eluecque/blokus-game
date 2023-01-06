import os
from typing_extensions import Self
from PIL import ImageTk,Image

from tkinter import Label
from customtkinter import CTk,CTkImage,CTkButton,CENTER

from mainWindow import VueBlokus
from VueRegles import VueRegles
from VueScore import VueScore

class Menu():

    def __init__(self: Self,window : CTk, longueur = 700, hauteur = 700):

        self.window : CTk = window
        self.window.title("jeu Blokus")
        self.window.iconbitmap('./Icon/icon.ico')
        self.window.resizable(width=False, height=False)

        self.screen_width : int = self.window.winfo_screenwidth()
        self.screen_height : int  = self.window.winfo_screenheight()
        self.x : float = (self.screen_width/2) - (longueur/2)
        self.y : float = (self.screen_height/2) - (hauteur/2)
        
        self.UI(longueur, hauteur)
        self.window.mainloop()
        
    def UI(self : Self, hauteur : int , longueur :int):
        
        self.window.geometry('%dx%d+%d+%d' % (longueur, hauteur, self.x, self.y))
        self.window.geometry(str(longueur) + 'x' + str(hauteur))
        self.backgroundImage = Image.open("./assets/carre.png")
        self.background = ImageTk.PhotoImage(self.backgroundImage)
        self.label = Label(self.window, image = self.background, bd = 0)
        self.label.place(x = 0,y = 0)
        
        self.backgroundButtunPlay = CTkImage(Image.open(os.path.join("./assets/button_play.png")), size=(158, 49))
        self.button1 = CTkButton(
            master=self.window, 
            text='', 
            image = self.backgroundButtunPlay, 
            command = self.playButton, 
            border_width=0, 
            fg_color="white", 
            bg_color= "white", 
            hover_color="white"
        )
        self.button1.place(relx=0.5, rely=0.48, anchor=CENTER)

        # Bouton Regles
        self.backgroundButtunRules = CTkImage(Image.open(os.path.join("./assets/button_rules.png")), size=(196, 49))
        self.button2 = CTkButton(
            master=self.window, 
            text='', 
            image = self.backgroundButtunRules, 
            command = self.rulesButton, 
            border_width=0, 
            fg_color="white", 
            bg_color= "white", 
            hover_color="white"
        )
        self.button2.place(relx=0.499, rely=0.58, anchor=CENTER)       

        # Bouton Statistiques
        self.backgroundButtunStats = CTkImage(Image.open(os.path.join("./assets/button_stats.png")), size=(221, 49))
        self.button3 = CTkButton(
            master=self.window, 
            text='', 
            image = self.backgroundButtunStats, 
            command = self.statsButton, 
            border_width=0, 
            fg_color="white", 
            bg_color= "white", 
            hover_color="white"
        )
        self.button3.place(relx=0.493, rely=0.68, anchor=CENTER)

        #Bouton Quitter
        self.backgroundButtunStats = CTkImage(Image.open(os.path.join("./assets/button_leave.png")), size=(158, 49))
        self.button3 = CTkButton(
            master=self.window, 
            text='', 
            image = self.backgroundButtunStats, 
            command = self.leaveButton, 
            border_width=0, 
            fg_color="white", 
            bg_color= "white", 
            hover_color="white"
        )
        self.button3.place(relx=0.493, rely=0.78, anchor=CENTER)   

        
    def playButton(self : Self):
        for child in self.window.winfo_children():
            child.destroy()
        VueBlokus(self,self.window)
    
    def rulesButton(self : Self):
        for child in self.window.winfo_children():
            child.destroy()
        VueRegles(self, self.window)

    def statsButton(self : Self):
        for child in self.window.winfo_children():
            child.destroy()

    def emitCB(self : Self):
        self.UI(700, 700)

    def emitFinishGame(self : Self,joueurs):
        # Faire ici
        self.UI(700,700)

        classement = {}

        for joueur in joueurs :
            for numPiece in joueur.pieces.pieces_joueurs:
                piece = joueur.jouerPiece(numPiece-1)
                for line in piece:
                    for square in line:
                        if square == 1:
                            joueur.removeScore()
        
            print(f"Score du joueur {joueur.couleur} : {joueur.score}")

            classement[joueur.couleur]=joueur.score
        VueScore(self,self.window,{k: v for k, v in sorted(classement.items(), key=lambda item: abs(item[1]))})

    def leaveButton(self: Self):
        self.window.quit()

if __name__ == "__main__":
    window = CTk()
    app = Menu(window) 
