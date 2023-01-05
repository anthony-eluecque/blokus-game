from tkinter import *
import customtkinter
from PIL import ImageTk, Image
from os import path

class VueScore():

    def __init__(self,master,window:customtkinter.CTk,classement:dict):

        couleurs: list = [ "#ffb800", "#787878", "#ff5c00", "#110eb8" ]
        self.master = master
        self.win: Tk = window
        self.win.geometry( "914x606" )

        # Chemin relatif pour trouver l'image
        dirname: str = path.dirname( __file__ )
        img: PhotoImage = ImageTk.PhotoImage( Image.open( dirname + "/assets/bg_score.png" ) )

        # Affichage de la fenêtre
        self.frame: Frame = Frame( self.win, width=914, height=606 )
        self.frame.pack()

        # Affichage de l'image
        bgimg: Label = Label( self.frame, image=img )
        bgimg.pack()

        # Texte "Tableau des scores"
        scoreTbLabel: Label = Label( self.frame, text="Tableau des scores", font="Roboto 30 bold", bg="white" )
        scoreTbLabel.place( x=457, y=130, anchor="center" )


        i: int = 1

        for couleur in classement.keys():
            podium: str = i == 1 and "1er :" or str( i ) + "ème :"

            podiumPos: Label = Label( 
                self.frame, 
                text=podium, 
                font="Roboto 30 bold", 
                bg="white", fg=couleurs[ i - 1 ] )
            podiumPos.place( x=280, y=250 + ( ( i-1) * 50 ), anchor="e" )
            
            podiumScore: Label = Label( 
                    self.frame, 
                    text=f'{ couleur } avec { classement[ couleur ] } points', 
                    font="Roboto 30 bold", 
                    bg="white" )
            podiumScore.place( x=285, y=250 + ( ( i-1) * 50 ), anchor="w" )

            i += 1

        self.win.mainloop()


if __name__ == "__main__":

    # Pour avoir la couleur de chaque position du podium
    couleurs: list = [ "#ffb800", "#787878", "#ff5c00", "#110eb8" ]

    # Points de chaque couleur
    classement: dict = {
        "Bleu": 100,
        "Vert": 150,
        "Rouge": 200,
        "Jaune": 10
    }

    # Tri du classement
    classement = { k: v for k, v in sorted( classement.items(), key = lambda item: item[ 1 ], reverse=True ) }

    win: Tk = Tk()
    win.geometry( "914x606" )

    # Chemin relatif pour trouver l'image
    dirname: str = path.dirname( __file__ )
    img: PhotoImage = ImageTk.PhotoImage( Image.open( dirname + "/assets/bg_score.png" ) )

    # Affichage de la fenêtre
    frame: Frame = Frame( win, width=914, height=606 )
    frame.pack()

    # Affichage de l'image
    bgimg: Label = Label( frame, image=img )
    bgimg.pack()

    # Texte "Tableau des scores"
    scoreTbLabel: Label = Label( frame, text="Tableau des scores", font="Roboto 30 bold", bg="white" )
    scoreTbLabel.place( x=457, y=130, anchor="center" )

    i: int = 1

    for couleur in classement.keys():
        podium: str = i == 1 and "1er :" or str( i ) + "ème :"

        podiumPos: Label = Label( frame, text=podium, font="Roboto 30 bold", bg="white", fg=couleurs[ i - 1 ] )
        podiumPos.place( x=280, y=250 + ( ( i-1) * 50 ), anchor="e" )
        
        podiumScore: Label = Label( frame, text=f'{ couleur } avec { classement[ couleur ] } points', font="Roboto 30 bold", bg="white" )
        podiumScore.place( x=285, y=250 + ( ( i-1) * 50 ), anchor="w" )

        i += 1

    win.mainloop()

