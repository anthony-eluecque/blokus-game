from core.Controller import Controller
from models.Player import Player
from models.Plateau import Plateau
from utils.game_utils import coordsBlocs, isValidMove, playerCanPlay
from testmap import MAP1
from utils.controller_utils import _openController
from utils.config_utils import Configuration
from utils.minmaxIA import medium_automate,gameManager
from utils.automates_utils import easy_automate
from views.GameView import GameView
from config import APP_PATH
import asyncio
import json
from utils.data_utils import dataGame


class GameController(Controller):
    """ 
    Controller gérant le menu héritant de la classe Controller ainsi que de sa méthode abstraite main()
    Hérite également des éléments pour le bon fonctionnement d'une partie.
    """
    
    def __init__(self, window):
        self.config = Configuration.getConfig()
        self.joueurs = [Player("Bleu"), Player("Jaune"), Player("Vert"), Player("Rouge")]
        self.window = window
        self.index = 0
        self.debut = True
        self.actualPlayer: Player = self.joueurs[self.index]
        self.plateau = Plateau(20,20)
        self.gameView = GameView(self, self.window)
        # self.gameView = self.loadView("Game",window)
        self.compteurNbPiecePose = 0
        self.nePeutPlusJouer = []
        self.logsPossibilities = []
        self.cheat = False

        self.db = dataGame()
        conf = Configuration.getConfig()
        for player in conf:
            self.db.addPseudoInData(player['couleur'],player['nom'])

    
    def callbackGame(self, file: str, x: int, y: int, rotation: int, inversion: int, canvas):
        """
        Procédure permettant de placer une pièce et de gérer les rotations/inversions. Si le placement est bon, la pièce se place sur la grille.
        Args:
            file (str) : chemin d'accès de l'image de la pièce.
            x (int) : coordonnées en abscisses de la pièce
            y (int) : coordonnées en ordonnées de la pièce
            rotation (int) : nombre de rotation
            inversion (int) : nombre d'inversion
            canvas : l'affichage de la pièce
        """
        file = file.replace(chr(92), "/") #chr(92) = \
        if "/src/.." in file:
            file = file.replace("/src/..", "")
        numPiece = int(file.split("/")[-1].split(".")[0])
        piece = self.actualPlayer.jouerPiece(numPiece-1)
        couleurJoueur = self.actualPlayer.getCouleur()
        indexJoueur = self.joueurs.index(self.actualPlayer)
        self.paquet = ""
        nb_rotation = abs(rotation) // 90
    
        for i in range(nb_rotation):
            self.actualPlayer.pieces.rotate(numPiece-1)
            piece = self.actualPlayer.jouerPiece(numPiece-1)

        if inversion %2 != 0:
            self.actualPlayer.pieces.reverse(numPiece-1)
            piece = self.actualPlayer.jouerPiece(numPiece-1)

        pieceBlokus = coordsBlocs(piece, x // 30, y // 30)
        cheminFichierPiece = APP_PATH +  r"/../media/pieces/" + couleurJoueur.upper()[0] + r"/1.png"
        # cheminFichierPiece = PIECES_IMAGES_URL[couleurJoueur.upper()[0]][0]

        if isValidMove(piece, y // 30, x // 30, self.plateau, self.actualPlayer):
        # if validPlacement(piece, y // 30, x // 30, self.plateau, self.actualPlayer):
            canvas.destroy()
            self.actualPlayer.removePiece(numPiece-1)

            self.db.addPoints(self.actualPlayer.couleur,len(pieceBlokus))
            self.db.addToHistoriquePlayer(self.actualPlayer.couleur,y//30,x//30,numPiece-1,nb_rotation,inversion)

            for coordY,coordX in pieceBlokus:
                self.gameView._addToGrid(cheminFichierPiece, coordX,coordY)
                self.plateau.setColorOfCase(coordY, coordX, indexJoueur)
            
            self.actualPlayer.hasPlayedPiece(numPiece-1)
            self.paquet = file + "," + str(x) + "," + str(y) + "," + str(rotation) + "," + str(inversion)
            self.canvas = canvas
            self.nextPlayer()
            self.debut = False
            self.compteurNbPiecePose += 1

        if nb_rotation > 0 or inversion%2==1:    
            self.actualPlayer.pieces.resetRotation(numPiece-1)

    def activateCheatMode(self):
        self.clearCheatMode()
        possibilities = gameManager.getBestPossibilities(self.plateau,self.index,self.actualPlayer)
        for possibility in possibilities:
            x,y = possibility
            x = x*30
            y = y*30
            self.gameView.drawCell(y,x,"purple")
            self.logsPossibilities.append([y,x])

    def clearCheatMode(self):
        if len(self.logsPossibilities):
            for possibility in self.logsPossibilities:
                x,y = possibility
                self.gameView.drawCell(x,y,"white")
            self.logsPossibilities.clear()

    def cheatMode(self):
        if self.compteurNbPiecePose > 3:
            if self.cheat:
                self.activateCheatMode()
            else: 
                self.clearCheatMode()

    def nextPlayer(self) -> None:
        """        
        Procédure permettant de gérer les changements de joueur
        """
        playable: bool = False
        joueur: Player = Player("Rouge") 

        for i in range(len(self.joueurs)):
            self.index = (self.index + 1) % 4
            joueur =  self.joueurs[self.index]
            if playerCanPlay(joueur, self.plateau): 
                playable = True
                break
            else:
                if joueur.getCouleur() not in self.nePeutPlusJouer:
                    self.nePeutPlusJouer.append(joueur.getCouleur())
                    self.gameView._makePopup(joueur)
        self.actualPlayer = joueur


        # GESTION DES IA 
        # A MODIFIER POUR QUE CA SOIT + OPTIMISER ET RAPIDE
        # J'ai fais ça pour test
        self.joueursIA = []
        for player in Configuration.getConfig():
            if player["niveau_difficulte"]!=0:
                self.joueursIA.append(player["couleur"])
        if self.actualPlayer.getCouleur() in self.joueursIA:
            asyncio.run(self.IA())

        if not playable:
            print("terminé")
            # makeClassement(self.joueurs)
            _openController(self.gameView, "Score", self.window)
        else:
            self.cheatMode() #Comment for remove cheat mode
            self.gameView.update(self.actualPlayer, self.index)

    def loadMap(self):
        """
        Procédure permettant de chager une grille avec des pièces déjà placées.
        """
        for couleur, pieces in MAP1.items():
            cheminFichierPiece = APP_PATH + r"/../media/pieces/" + couleur.upper()[0] + r"/1.png"
            # cheminFichierPiece = PIECES_IMAGES_URL[couleur.upper()[0]][0]
            
            for piece in pieces :
                p = self.joueurs[self.index].jouerPiece(piece[0]) 
                p = coordsBlocs(p, piece[1][1], piece[1][0])

                for coordx,coordy in p:
                    self.gameView._addToGrid(cheminFichierPiece, coordy, coordx)
                    self.plateau.setColorOfCase(coordx, coordy, self.index)
                
                self.joueurs[self.index].hasPlayedPiece(piece[0])
                self.joueurs[self.index].removePiece(piece[0])

            self.index = (self.index + 1) % 4
        self.gameView.update(self.actualPlayer, self.index)
        # self.nextPlayer()
    
    def startGame(self):
        for player in Configuration.getConfig():
            if player["niveau_difficulte"]!=0 and player["couleur"]=="Bleu":
                asyncio.run(self.IA())
       

    def _newGame(self):
        _openController(self.gameView, "Game", self.window)

    def _backToHome(self):
        _openController(self.gameView, "Home", self.window)

    def main(self):
        self.gameView.main()
        self.startGame()    
        self.gameView.update(self.actualPlayer, self.index)
        self.cheatMode()
        # self.loadMap()

    async def IA(self):
        # easy_automate(self.actualPlayer,self.plateau,self.index,self.gameView)
        with open(APP_PATH + r"\..\gameconfig.json", "r") as outfile:
            gameConfig = json.load(outfile)
        color = self.actualPlayer.getCouleur()
        for confPlayer in gameConfig:
            if confPlayer['couleur'] == self.actualPlayer.getCouleur():
                niveau = confPlayer["niveau_difficulte"]
        if niveau == "Facile":
            easy_automate(self.actualPlayer,self.plateau,self.index,self.gameView,self.db)
        elif niveau == "Moyen":
            result = await medium_automate(self.actualPlayer,self.plateau,self.index,self.gameView,self.db)
        
        self.nextPlayer()