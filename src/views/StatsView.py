from views.View import View
from utils.window_utils import _resizeWindow, _createFrame, _deleteChilds
from utils.data_utils import jsonManager
from customtkinter import CTk, CTkImage, CTkLabel
from PIL import Image
from tkinter import Label
from components.stats.gamehistorique import gameHistorique
from components.bouton import Bouton

class StatsView(View):
    
    def __init__(self,controller,window:CTk,width=1300,heigth=800) -> None:
        super().__init__()
        self.window = window
        self.statsController = controller

    def _makeFrame(self):
        self.mainFrame = _createFrame(self.window, 1300, 800)

    def _makeBackground(self)->None:
        self.bgImage = CTkImage(Image.open("./media/assets/bgStats.png"), size=(1300, 800))
        self.bg = CTkLabel(self.window, text="", image = self.bgImage)
        self.bg.place(x = 0, y = 0)

    def _makeTitle(self)->None:
        self.mainTitle = Label( self.mainFrame, text="", image = self.background, bd = 0 )

    def createWidgets(self)->None:
        self.data = jsonManager.readJson()

        self.widgets = []
        xpos = 80
        ypos = 180

        for idPartie in self.data["parties"]:
            widget = gameHistorique(self.window,self,xcoord=xpos,ycoord=ypos,idPartie=idPartie,dictPartie=self.data["parties"][idPartie],command=self.statsController.showWidget)
            self.widgets.append(widget)
            ypos += 100


    def main(self,width=1300,heigth=800)->None:
        _resizeWindow(self.window, width, heigth)
        self._makeFrame()
        self._makeBackground()
        self.createWidgets()


    def close(self)->None:
        _deleteChilds(self.window)
