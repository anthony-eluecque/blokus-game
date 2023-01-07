from core.Controller import Controller
from core.Core import Core
from models.Player import Player
from models.Plateau import Plateau
from utils.game_utils import coordsBlocs,validPlacement,playerCanPlay
from utils.leaderboard_utils import makeClassement
from testmap import MAP1

class GameController(Controller):
    
    def __init__(self,window):
        self.joueurs = [Player("Bleu"),Player("Jaune"),Player("Vert"),Player("Rouge")]
        self.window = window
        self.index = 0
        self.actualPlayer : Player = self.joueurs[self.index]
        self.plateau = Plateau(20,20)
        self.gameView = self.loadView("Game",window)
        # self.loadMap()
    
    def callback(self,file:str,x:int,y:int,rotation:int,inversion:int):

        numPiece = int(file.split("/")[4].split(".")[0])
        
        piece = self.actualPlayer.jouerPiece(numPiece-1)
        couleurJoueur = self.actualPlayer.getCouleur()
        indexJoueur = self.joueurs.index(self.actualPlayer)
        
        nb_rotation = abs(rotation)//90
        for i in range(nb_rotation):
            self.actualPlayer.pieces.rotate(numPiece-1)
            piece = self.actualPlayer.jouerPiece(numPiece-1)

        if inversion%2!=0:
            self.actualPlayer.pieces.reverse(numPiece-1)
            piece = self.actualPlayer.jouerPiece(numPiece-1)
            print(piece)
        pieceBlokus = coordsBlocs(piece,x//30,y//30)
        cheminFichierPiece = "./media/pieces/" + couleurJoueur.upper()[0] + "/1.png"

        if validPlacement(piece,y//30,x//30,self.plateau,self.actualPlayer):
            self.actualPlayer.removePiece(numPiece-1)
            for coordY,coordX in pieceBlokus:
                self.gameView._addToGrid(cheminFichierPiece,coordX,coordY)
                self.plateau.setColorOfCase(coordY,coordX,indexJoueur)
            
            self.actualPlayer.hasPlayedPiece(numPiece-1)
            
            self.nextPlayer()
            self.gameView.update(self.actualPlayer)

        if nb_rotation>0:    
            self.actualPlayer.pieces.resetRotation(numPiece-1)
        

    def nextPlayer(self)->None:
        self.index= (self.index+1)%4
        self.actualPlayer =  self.joueurs[self.index]
        playable = False
        for i in range(0,2):
            if playerCanPlay(self.actualPlayer,self.plateau): 
                playable = True
                break
            self.index = (self.index+1)%4
            self.actualPlayer =  self.joueurs[self.index]

        if not playable:
            for child in self.window.winfo_children():
                child.destroy()
            makeClassement(self.joueurs)
            c = Core.openController("Score",self.window,self.joueurs)
            c.main()

    def loadMap(self):
        
        indexJoueur = 0
        for couleur,pieces in MAP1.items():
            cheminFichierPiece = "./media/pieces/" + couleur.upper()[0] + "/1.png"
            
            for piece in pieces :

                p = self.joueurs[indexJoueur].jouerPiece(piece[0]) 
                p = coordsBlocs(p,piece[1][1],piece[1][0])
                for coordx,coordy in p:
                    self.gameView._addToGrid(cheminFichierPiece,coordy,coordx)
                    self.plateau.setColorOfCase(coordx,coordy,indexJoueur)
                
                self.joueurs[indexJoueur].hasPlayedPiece(piece[0])
                self.joueurs[indexJoueur].removePiece(piece[0])

            indexJoueur +=1
        self.gameView.update(self.actualPlayer)
        # self.nextPlayer()

    def main(self):
        self.gameView.main()
