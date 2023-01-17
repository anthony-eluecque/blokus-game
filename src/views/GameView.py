from views.View import View
from utils.window_utils import _resizeWindow,_deleteChilds,_createFrame
from tkinter import Frame
from customtkinter import CTk, CTkImage,CTkLabel
from PIL import Image
from components.game.grille import grille
from components.game.score import score
from components.game.piecesManager import piecesManager
from models.Player import Player
from components.bouton import Bouton


class GameView(View):

    def __init__(self,controller,window:CTk,width=1300,heigth=800):

        super().__init__()
        self.gameController = controller
        self.window = window


    def _makeFrame(self):
        self.mainFrame = _createFrame(self.window,1300,800)

    def _callComponents(self):
        self._makeFrame()
        self._makeBackground()

        self.grille = grille(self.window,600,600)
        self.score = score(self.window,Player('Bleu'))
        self.piecesManager = piecesManager(self.window,Player('Bleu'),self)
        
        self.newGameButton = Bouton(self.window,self,700,690,width=250,heigth=125,file="./media/assets/Button_new_game.png",son="button",command=self._newGame)
        self.leaveButton = Bouton(self.window,self,1070,690,width=250,heigth=125,file="./media/assets/button_leave.png",son="button",command=self._leaveGame)

    def _makeBackground(self):
        self.bgImage = CTkImage(Image.open("./media/assets/background_game.png"),size=(1300,800))
        self.bg = CTkLabel(self.window,text="",image = self.bgImage)

    def _callbackOnDrop(self,file:str,x:int,y:int,rotation:int,inversion:int,canvas):
        self.gameController.callbackGame(file,x,y,rotation,inversion,canvas)

    def _addToGrid(self,chemin,x,y):
        self.grille._addPieceToGrille(chemin,x,y)

    def _newGame(self):
        print("test")
        self.close()
        self.gameController._newGame()

    def _leaveGame(self):
        self.close()
        self.gameController._backToHome()

    def update(self,player,index):
        self.score.nextPlayer(index)
        self.piecesManager.update(player)

    def main(self,largeur = 1300,hauteur = 800):
        _resizeWindow(self.window,largeur,hauteur)
        self._callComponents()
        self.bg.place(x = 0,y = 0)

    def close(self):
        _deleteChilds(self.window)