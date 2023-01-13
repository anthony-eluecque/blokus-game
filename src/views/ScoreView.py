from utils.window_utils import _resizeWindow,_createFrame
from tkinter import Frame,Label
from views.View import View
from PIL import ImageTk,Image
from utils.leaderboard_utils import openJson
from customtkinter import CTk

class ScoreView(View):

    colors = ["#ffb800", "#787878", "#ff5c00", "#110eb8" ]

    def __init__(self,controller,window : CTk,longueur=914,hauteur=606):
        super().__init__()

        self.window = window
        self.scoreController = controller


    def _makeFrame(self):
        self.mainFrame = _createFrame(self.window,914,606)

    def _makeBackground(self):
        
        img = Image.open("./media/assets/bg_score.png")
        self.img = ImageTk.PhotoImage(img)
        self.bgImg = Label(self.mainFrame,image=self.img,text="")
        self.bgImg.place(x=0,y=0,anchor="nw")

    def _makeTitleClassement(self):
        
        self.scoreTbLabel = Label(self.mainFrame, text="Tableau des scores", font="Roboto 30 bold", bg="white" )
        self.scoreTbLabel.place( x=457, y=130, anchor="center" )

    def _makeClassement(self,classement):

        i: int = 1
        for couleur in classement.keys():
            
            podium: str = i == 1 and "1er :" or str( i ) + "ème :"
            podiumPos: Label = Label(self.mainFrame, text=podium, font="Roboto 30 bold", bg="white", fg=self.colors[ i - 1 ])
            podiumPos.place(x=280, y=250 + ( ( i-1) * 50 ), anchor="e")
            podiumScore: Label = Label(self.mainFrame, text=f'{ couleur } avec { classement[ couleur ] } points', font="Roboto 30 bold", bg="white" )
            podiumScore.place(x=285, y=250 + ( ( i-1) * 50 ), anchor="w")
            i += 1


    def main(self,longueur=914,hauteur=606):
        classement = openJson()
        _resizeWindow(self.window,longueur,hauteur)
        self._makeFrame()
        self._makeBackground()
        self._makeTitleClassement()
        self._makeClassement(classement)


    def close(self):
        return
    
