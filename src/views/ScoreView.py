from utils.window_utils import _resizeWindow
from tkinter import Frame,Label
from views.View import View
from PIL import ImageTk,Image

class ScoreView(View):

    colors = ["#ffb800", "#787878", "#ff5c00", "#110eb8" ]

    def __init__(self,controller,window,longueur=914,hauteur=606):
        super().__init__()

        self.window = window
        self.scoreController = controller
        _resizeWindow(self.window,longueur,hauteur)

        self._makeFrame()
        self._makeBackground()
        self._makeTitleClassement()

    def _makeFrame(self):
        
        self.mainFrame = Frame(self.window,width=914,height=606)
        self.mainFrame.pack()
        self.mainFrame.pack_propagate(0)

    def _makeBackground(self):
        
        img = ImageTk.PhotoImage(Image.open("./media/assets/bg_score.png"))
        self.bgImg = Label(self.mainFrame,image=img,text="")
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
            podiumScore: Label = Label(self.mainFrame, text=f'{ couleur } avec { self.classement[ couleur ] } points', font="Roboto 30 bold", bg="white" )
            podiumScore.place(x=285, y=250 + ( ( i-1) * 50 ), anchor="w")
            i += 1


    def main(self):
        pass
        
    def close(self):
        return
    
