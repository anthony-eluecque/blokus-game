import tkinter as tk
from tkinter import ttk,Label
from views.View import View
from customtkinter import CTk,CTkImage,CENTER,CTkButton,CTkLabel
from PIL import Image,ImageTk
from typing_extensions import Self
from tkinter import Frame
import os
from utils.window_utils import _resizeWindow,_deleteChilds,_createFrame
from components.bouton import Bouton
from components.SoundButton import SoundButton

class HomeView(View):

    def __init__(self,controller,window:CTk, longueur = 700, hauteur = 700):
        
        super().__init__()

        self.window = window
        self.homeController = controller

    def _makeFrame(self):
        self.mainFrame = _createFrame(self.window,700,1000)

    def _placement(self):

        self.label.place(x = 0,y = 0)
        # self.playButton.place(relx=0.5, rely=0.48, anchor=CENTER)
        # self.rulesButton.place(relx=0.499, rely=0.58, anchor=CENTER)    
        # self.statsButton.place(relx=0.493, rely=0.68, anchor=CENTER)    
        # self.leaveButton.place(relx=0.493, rely=0.78, anchor=CENTER)   

    def _UI(self : Self):
        self.playButton = Bouton(self.window, self, 271, 315, width=158, heigth=49, file="./media/assets/button_play.png", son="button", command=self.homeController.btnPlay)

        self.rulesButton = Bouton(self.window, self, 252, 380, width=196, heigth=49, file="./media/assets/button_rules.png", son="button", command=self.homeController.btnRules)
        
        self.statsButton = Bouton(self.window, self, 239.5, 440, width=221, heigth=49, file="./media/assets/button_stats.png", son="button", command=self.homeController.btnStats)

        self.leaveButton = Bouton(self.window, self, 271, 500, width=158, heigth=49, file="./media/assets/button_leave.png", son="button", command=self.window.destroy)
                
        self.backgroundImage = Image.open(os.path.join("./media/assets/carre.png"))
        self.background = ImageTk.PhotoImage(self.backgroundImage)
        self.label = Label(self.mainFrame, image = self.background, bd = 0)   


        self.soundButton = SoundButton(self.window,self,85,560)

    

    def main(self, longueur = 700 ,hauteur = 700):
        _resizeWindow(self.window,longueur,hauteur)
        self._makeFrame()
        self._UI()
        self._placement()

    def close(self):
        _deleteChilds(self.window)