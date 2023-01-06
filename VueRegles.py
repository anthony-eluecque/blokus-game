# Imports
import os
import customtkinter
from typing_extensions import Self
import customtkinter
from tkinter import BOTH, Canvas, PhotoImage
from PIL import Image,ImageTk
import tkinter

# Class VueRegles
class VueRegles():

    def __init__(self, master,  window : customtkinter.CTk, longueur = 625, hauteur = 700):
        # Window
        self.master = master
        self.window = window
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()
        self.x = (self.screen_width/2) - (longueur/2)
        self.y = (self.screen_height/2) - (hauteur/2)
        self.window.geometry('%dx%d+%d+%d' % (longueur, hauteur, self.x, self.y))
        self.window.title("Règles du Blokus")
        self.window.geometry("625x700")
        self.window.resizable(width=False, height=False)

        # Background
        self.backgroundImage = Image.open("./assets/background_rules.png")
        self.background = ImageTk.PhotoImage(self.backgroundImage)
        self.label = tkinter.Label(self.window, image = self.background, bd = 0)
        self.label.place(x = 0,y = 0)

        # Title
        self.rulesTitle = customtkinter.CTkLabel(master = self.window ,
        text="Règles du Blokus", 
        fg_color="white",
        font=customtkinter.CTkFont(family="Roboto Medium", size=40), 
        text_color="black" )

        self.rulesTitle.pack(side="top", pady=40)

        # Rules
        self.rules = customtkinter.CTkTextbox(master = self.window,
        fg_color="white", 
        text_color="black", 
        corner_radius=0, 
        width=450, 
        height=500, 
        font=customtkinter.CTkFont(family="Roboto Medium", size=17))
        self.rules.pack(fill="none", expand=True, side="top")
        self.rules.place(x=80, y=110)

        # Texts and inserts
        self.sentence1: str = "• La première pièce doit être posée dans le coin du plateau correspondant.\n\n"; self.rules.insert("end", self.sentence1) 
        self.sentence2: str = "• Pour placer une pièce, elle ne doit pas être adjacente à     une autre pièce de la même couleur.\n\n"; self.rules.insert("end", self.sentence2)
        self.sentence3: str = "• Cependant, elle doit toucher le coin d’une pièce de la même couleur.\n\n"; self.rules.insert("end", self.sentence3)
        self.sentence4: str = "• Il faut placer le plus de pièces possible sur le plateau.\n\n"; self.rules.insert("end", self.sentence4)
        self.sentence5: str = "• Bloquer un adversaire pour l’empêcher de poser ses pièces est autorisé.\n\n"; self.rules.insert("end", self.sentence5)
        self.sentence6: str = "• Quand vous ne pouvez plus placer de pièces, passez votre tour.\n\n"; self.rules.insert("end", self.sentence6)
        self.sentence7: str = "• La partie se termine quand tous les joueurs ne peuvent plus placer de pièces.\n\n"; self.rules.insert("end", self.sentence7)
        self.sentence8: str = "• Le gagnant est la personne ayant le plus de points à la fin de la partie."; self.rules.insert("end", self.sentence8)

        # Setting rules to read-only (putting it here is mandatory otherwise the text is not added)
        self.rules.configure(state="disabled")

        # Back button
        self.backgroundB = customtkinter.CTkImage(Image.open(os.path.join("./assets/buttun_rules_return.png")), size=(206, 49))
        self.Button = customtkinter.CTkButton(
            master = self.window, 
            text="", 
            command=self.CBback, 
            image=self.backgroundB, 
            border_spacing=0,
            fg_color="white", 
            bg_color="white",
            corner_radius=0,
            hover_color="white")
        self.Button.pack()
        self.Button.place(relx=0.5, rely=0.89, anchor=customtkinter.CENTER)
        self.window.mainloop()

    # Back button callback
    def CBback(self):
        self.label.destroy()
        self.rules.destroy()
        self.rulesTitle.destroy()
        self.Button.destroy()
        self.master.emitCB()
