# Imports
import customtkinter
from typing_extensions import Self
import customtkinter
from tkinter import BOTH, Canvas, PhotoImage
from PIL import Image,ImageTk
import tkinter

# Class VueRegles
class vueRegles():

    def __init__(self, master,  window : customtkinter.CTk):
        # Window
        self.master = master
        self.window = window
        self.window.title("Règles du Blokus")
        self.window.geometry("625x700")
        # self.window.resizable(width=False, height=False)

        # Background
        self.backgroundImage = Image.open("./assets/background_rules.png")
        self.background = ImageTk.PhotoImage(self.backgroundImage)
        self.label = tkinter.Label(self.window, image = self.background, bd = 0)
        self.label.place(x = 0,y = 0)

        # Title
        self.rulesTitle = customtkinter.CTkLabel(master = self.window ,
        text="Règles du Blokus", 
        fg_color="white",
        text_font=("Roboto Medium", 40), 
        text_color="black" )

        self.rulesTitle.pack(side="top", pady=40)

        # Rules
        self.rules = customtkinter.CTkTextbox(master = self.window,
        fg_color="white", 
        text_color="black", 
        corner_radius=0, 
        width=450, 
        height=500, 
        text_font=("Roboto Medium", 13))
        self.rules.pack(fill="none", expand=True)

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
        self.backgroundButtun = Image.open("./assets/buttun_rules_return.png")
        self.backgroundB = ImageTk.PhotoImage(self.backgroundButtun)
        self.Button = customtkinter.CTkButton(master = self.window, text="", command=self.CBback, image=self.backgroundB, bd=0)
        self.Button.pack()

        self.window.mainloop()

    # Back button callback
    def CBback(self):
        self.label.destroy()
        self.rules.destroy()
        self.rulesTitle.destroy()
        self.Button.destroy()
        self.master.emitCB()
        



if __name__ == "__main__":
    window = customtkinter.CTk()
    App = vueRegles(window)