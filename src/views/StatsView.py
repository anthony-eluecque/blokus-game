from views.View import View
from utils.window_utils import _resizeWindow, _createFrame, _deleteChilds
from utils.data_utils import jsonManager
from customtkinter import CTk, CTkImage, CTkLabel
from PIL import Image,ImageTk
from tkinter import Label
from components.stats.gamehistorique import gameHistorique
from components.bouton import Bouton

class StatsView(View):
    
    def __init__(self,controller,window:CTk,width=1300,heigth=800) -> None:
        super().__init__()
        self.window = window
        self.statsController = controller

    def _makeFrame(self,width,heigth) -> None:
        self.mainFrame = _createFrame(self.window, width, heigth)

    def _makeBackground(self,xsize,ysize,file="./media/assets/bgStats.png")->None:
        self.bgImage = CTkImage(Image.open(file), size=(xsize, ysize))
        self.bg = CTkLabel(self.window, text="", image = self.bgImage)
        self.bg.place(x = 0, y = 0)

    def _makeTitle(self) -> None:
        self.mainTitle = Label( self.mainFrame, text="", image = self.background, bd = 0 )

    def createWidgets(self)->None:
        self.data = jsonManager.readJson()

        self.widgets = []
        xpos = 80
        ypos = 180

        for idPartie in self.data["parties"]:
            widget = gameHistorique(self.window,self,xcoord=xpos,ycoord=ypos,idPartie=idPartie,dictPartie=self.data["parties"][idPartie],command=self.statsController.showWidget)
            self.widgets.append(widget)
            ypos += 65

    
    def openDetailGame(self,idPartie) -> None:
        _deleteChilds(self.window)
        _resizeWindow(self.window,500,600)
        self._makeFrame(500,600)
        self._makeBackground(500,600,"./media/assets/bgDetailPartie.png")
        self.banners = []

        colors = ["bleu","rouge","vert","jaune"]
        y = 100
        for color in colors:
            banner = self.makeBanner(("./media/assets/banner"+color+".png"),xpos=50,ypos=y)
            self.banners.append(banner)
            y+=110
        self.backStats: Bouton = Bouton(self.window, self, 150, 540, width=206, heigth=49, file="./media/assets/buttun_rules_return.png", son="button", command=self.statsController.backToStats)




    def makeBanner(self,file,xpos,ypos):
        self.img = CTkImage(Image.open(file),size=(400,40))
        label = CTkLabel(master=self.window,text="",image=self.img)
        label.place(x=xpos,y=ypos)
        return label
        
        


    def main(self, width=1300, height=800) -> None:
        _resizeWindow(self.window, width, height)
        self._makeFrame(width,height)
        self._makeBackground(1300,800)
        self.createWidgets()


    def close(self) -> None:
        _deleteChilds(self.window)
