import tkinter as tk
from tkinter import ttk,Label
from views.View import View
from customtkinter import CTk,CTkImage,CENTER,CTkButton,CTkTextbox,CTkLabel,CTkFont,CTkFrame
from PIL import Image,ImageTk
from typing_extensions import Self
import os
from tkinter import Label,Frame
from utils.window_utils import _resizeWindow

class RulesView(View):

    RULES = [
        "• La première pièce doit être posée dans le coin du plateau correspondant.\n\n",
        "• Pour placer une pièce, elle ne doit pas être adjacente à     une autre pièce de la même couleur.\n\n",
        "• Cependant, elle doit toucher le coin d’une pièce de la même couleur.\n\n",
        "• Il faut placer le plus de pièces possible sur le plateau.\n\n",
        "• Bloquer un adversaire pour l’empêcher de poser ses pièces est autorisé.\n\n",
        "• Quand vous ne pouvez plus placer de pièces, passez votre tour.\n\n",
        "• La partie se termine quand tous les joueurs ne peuvent plus placer de pièces.\n\n",
        "• Le gagnant est la personne ayant le plus de points à la fin de la partie.",
    ]

    def __init__(self,controller,window,width=625,heigth=700):

        super().__init__()
        self.rulesController = controller
        self.window = window

        _resizeWindow(self.window,width,heigth)
        self._makeFrame()
        self._makeWindow()
        self._makeTitle()
        self._makeTextBox()
        self._makeRules()
        self._makeButtonRules()
        self._configWidget()


    def _makeFrame(self):
        self.mainFrame = Frame(self.window,width= 1000,height=1000)
        self.mainFrame.pack()
        self.mainFrame.pack_propagate(0)

    def _makeWindow(self):
        self.backgroundImage = Image.open("./media/assets/background_rules.png")
        self.background = ImageTk.PhotoImage(self.backgroundImage)
        self.bgRules = Label(self.mainFrame,text="",image = self.background, bd = 0)

    def _makeTitle(self):
        self.rulesTitle = CTkLabel(master = self.mainFrame , text="Règles du Blokus", fg_color="white",font=CTkFont(family="Roboto Medium", size=40), text_color="black" )

    def _makeTextBox(self):
        self.rulesBox = CTkTextbox(master = self.mainFrame,fg_color="white", text_color="black", corner_radius=0, width=450, height=500, font=CTkFont(family="Roboto Medium", size=17))

    def _makeRules(self):
        for rule in self.RULES:
            self.rulesBox.insert("end", rule)

    def _makeButtonRules(self):
        self.bgButton = CTkImage(Image.open("./media/assets/buttun_rules_return.png"), size=(206, 49))
        self.backRules = CTkButton(master = self.mainFrame, text="", command=self.rulesController.btn_clear, image=self.bgButton, border_spacing=0,fg_color="white", bg_color="white",corner_radius=0,hover_color="white")

    def _configWidget(self):

        self.bgRules.place(x = 0,y = 0)
        self.rulesTitle.pack(side="top", pady=40)
        self.rulesBox.pack(fill="none", expand=True, side="top")
        self.rulesBox.place(x=80, y=110)
        self.rulesBox.configure(state="disabled")
        self.backRules.pack()
        self.backRules.place(relx=0.5, rely=0.89, anchor=CENTER)

    def main(self):
        pass
        
    def close(self):
        return
    