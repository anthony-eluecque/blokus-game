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

        for idPartie in self.data["parties"]:
            print(idPartie)
            # gameHistorique(self.statsController.showWidget)
            
            
            bgImage = CTkImage(Image.open("./media/assets/bg_histo.png"), size=(600, 55))
            self.bg = CTkLabel(self.window, text="", image = bgImage)
            self.bg.place(x = 80, y = 180)

            self.labelTime = CTkLabel(self.window,text=self.data["parties"][idPartie]["date"] + " | " + self.data["parties"][idPartie]["heure"], bg_color='white' ,text_color="black")
            self.labelTime.place(x=120,y=190)

            self.labelWinner = CTkLabel(self.window,text=self.data["parties"][idPartie]["gagnant"],bg_color="white",text_color="black")
            self.labelWinner.place(x=350,y=190)

            self.button = Bouton(self.window,view=self,xpos=560,ypos=180,width=100,heigth=45,file="./media/assets/afficher.png",command=self.statsController.showWidget)




    def main(self,width=1300,heigth=800)->None:
        _resizeWindow(self.window, width, heigth)
        self._makeFrame()
        self._makeBackground()
        self.createWidgets()


    def close(self)->None:
        _deleteChilds(self.window)
