from core.Controller import Controller
from models.Player import Player
from models.Plateau import Plateau
from utils.game_utils import coordsBlocs, validPlacement, playerCanPlay
from utils.leaderboard_utils import makeClassement, writeInJson, updateClassementFromPlay
from testmap import MAP1
from utils.controller_utils import _openController
from utils.config_utils import Configuration
from utils.automates_utils import medium_automate

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
        self.gameView = self.loadView("Game",window)
        self.nePeutPlusJouer = []
    
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
        print("test")
        numPiece = int(file.split("/")[4].split(".")[0])
        
        piece = self.actualPlayer.jouerPiece(numPiece-1)
        couleurJoueur = self.actualPlayer.getCouleur()
        indexJoueur = self.joueurs.index(self.actualPlayer)
        
        nb_rotation = abs(rotation) // 90
    
        for i in range(nb_rotation):
            self.actualPlayer.pieces.rotate(numPiece-1)
            piece = self.actualPlayer.jouerPiece(numPiece-1)

        if inversion %2 != 0:
            self.actualPlayer.pieces.reverse(numPiece-1)
            piece = self.actualPlayer.jouerPiece(numPiece-1)
            print(piece)
        pieceBlokus = coordsBlocs(piece, x // 30, y // 30)
        cheminFichierPiece = "./media/pieces/" + couleurJoueur.upper()[0] + "/1.png"

        if validPlacement(piece, y // 30, x // 30, self.plateau, self.actualPlayer):
            canvas.destroy()
            self.actualPlayer.removePiece(numPiece-1)
            if self.debut == False:
                self.classement = updateClassementFromPlay(self.actualPlayer, numPiece)
            else:
                self.classement = makeClassement(self.joueurs)
                writeInJson(self.classement)  
            print(self.classement)
            for coordY,coordX in pieceBlokus:
                self.gameView._addToGrid(cheminFichierPiece, coordX,coordY)
                self.plateau.setColorOfCase(coordY, coordX, indexJoueur)
            
            self.actualPlayer.hasPlayedPiece(numPiece-1)
            
            self.nextPlayer()
            self.debut = False
            self.gameView.update(self.actualPlayer, self.index)

        if nb_rotation > 0:    
            self.actualPlayer.pieces.resetRotation(numPiece-1)

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
            self.IA()

        if not playable:
            print("terminé")
            makeClassement(self.joueurs)
            _openController(self.gameView, "Score", self.window)

    def loadMap(self):
        """
        Procédure permettant de chager une grille avec des pièces déjà placées.
        """
        for couleur, pieces in MAP1.items():
            cheminFichierPiece = "./media/pieces/" + couleur.upper()[0] + "/1.png"
            
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
                self.IA()
       

    def _newGame(self):
        _openController(self.gameView, "Game", self.window)

    def _backToHome(self):
        _openController(self.gameView, "Home", self.window)

    def main(self):
        self.gameView.main()
        self.startGame()    
        self.gameView.update(self.actualPlayer, self.index)
        #self.loadMap()

    def IA(self):
        # easy_automate(self.actualPlayer,self.plateau,self.index,self.gameView)
        medium_automate(self.actualPlayer,self.plateau,self.index,self.gameView)
        self.nextPlayer()