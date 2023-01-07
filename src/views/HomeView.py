import tkinter as tk
from tkinter import ttk,Label
from views.View import View
from customtkinter import CTk,CTkImage,CENTER,CTkButton,CTkLabel
from PIL import Image,ImageTk
from typing_extensions import Self
from tkinter import Frame
import os
from utils.window_utils import _resizeWindow

class HomeView(View):

    def __init__(self,controller,window, longueur = 700, hauteur = 700):
        
        super().__init__()

        self.window = window
        self.homeController = controller

        _resizeWindow(self.window,longueur,hauteur)
        self._makeFrame()
        self._UI()
        self._placement()
    
    def _makeFrame(self):
        self.mainFrame = Frame(self.window,width= 700,height=1000)
        self.mainFrame.pack()
        self.mainFrame.pack_propagate(0)

    def _placement(self):

        self.label.place(x = 0,y = 0)
        self.playButton.place(relx=0.5, rely=0.48, anchor=CENTER)
        self.rulesButton.place(relx=0.499, rely=0.58, anchor=CENTER)    
        self.statsButton.place(relx=0.493, rely=0.68, anchor=CENTER)    
        self.leaveButton.place(relx=0.493, rely=0.78, anchor=CENTER)   

    def _UI(self : Self):
                
        
        self.backgroundImage = Image.open(os.path.join("./media/assets/carre.png"))
        self.background = ImageTk.PhotoImage(self.backgroundImage)
        self.label = Label(self.mainFrame, image = self.background, bd = 0)   

        self.backgroundButtunPlay = CTkImage(Image.open(os.path.join("./media/assets/button_play.png")), size=(158, 49))
        self.playButton = CTkButton(master=self.mainFrame, text='', image = self.backgroundButtunPlay, command = self.homeController.btnPlay,border_width=0, fg_color="white", bg_color= "white", hover_color="white")

        # Bouton Regles
        self.backgroundButtunRules = CTkImage(Image.open(os.path.join("./media/assets/button_rules.png")), size=(196, 49))
        self.rulesButton = CTkButton(master=self.mainFrame, text='', image = self.backgroundButtunRules, command = self.homeController.btnRules, border_width=0, fg_color="white", bg_color= "white", hover_color="white")
        

        # Bouton Statistiques
        self.backgroundButtunStats = CTkImage(Image.open(os.path.join("./media/assets/button_stats.png")), size=(221, 49))
        self.statsButton = CTkButton(master=self.mainFrame,text='', image = self.backgroundButtunStats, command = self.homeController.btnStats, border_width=0, fg_color="white", bg_color= "white", hover_color="white")

        #Bouton Quitter
        self.backgroundButtunStats = CTkImage(Image.open(os.path.join("./media/assets/button_leave.png")), size=(158, 49))
        self.leaveButton = CTkButton(master=self.mainFrame, text='', image = self.backgroundButtunStats, command = self.window.destroy, border_width=0, fg_color="white", bg_color= "white", hover_color="white")
    
    def _resizeWindow(self,width:int,heigth:int):

        self.window.resizable(width=False, height=False)
        _screen_width : int = self.window.winfo_screenwidth()
        _screen_height : int  = self.window.winfo_screenheight()
        x : float = (_screen_width/2) - (width/2)
        y : float = (_screen_height/2) - (heigth/2)

        self.window.geometry('%dx%d+%d+%d' % (width, heigth, x, y))
        self.window.geometry(str(width) + 'x' + str(heigth))
    
    def main(self):
        pass

    def close(self):
        return
    