from socket import socket
from threading import Thread
from config import APP_PATH
from core.Controller import Controller
from core.Core import Core
from customtkinter import CTk
from time import sleep
from utils.controller_utils import _openController
from constants import COLORS
from utils.game_utils import coordsBlocs

class Network():

    @staticmethod
    def sendMessage(ctx : str , client : socket):
        client.send(bytes(ctx, encoding="utf8"))
        sleep(0.1)

    @staticmethod
    def sendAllMessage(ctx : str , clients : list[socket]):
        for client in clients:
            Network.sendMessage(ctx,client[0])
    
    @staticmethod
    def receiveMessage(client : socket):
        return client.recv(1024).decode()


class Client(Thread):
  
  def __init__(self,ip,controller):
    Thread.__init__(self)
    try:
        self.client = socket()
        self.daemon = True
        self.client.connect((str(ip), 3000))
        self.controller = controller
        self.color = None
        print(f"je suis connecté au serveur")
    except:
        raise Exception

  def run(self):
    ctx = Network.receiveMessage(self.client)  # ctx = 'color'
    self.color = ctx

    print("Ma couleur est ",self.color,"\n")
    ctx = Network.receiveMessage(self.client) # ctx = 'start'
    
    self.controller.openGame() # On ouvre le jeu
    self.gameController = self.controller.controller
    self.gameController.bindClient(self.client)

    ctx = Network.receiveMessage(self.client)

    if ctx != self.color:
        self.gameController.unbindAllPiecesWhenNotPlay() # On unbind tous les joueurs

    while 1: 
        ctx = Network.receiveMessage(self.client) # ctx = logPiece
        if ctx != 'attente':
            ctx = ctx.split(',')
            file = ctx[0]
            x = int(ctx[1])
            y = int(ctx[2])
            rotation = int(ctx[3])
            inversion = int(ctx[4])
            numPiece = int(file.split("/")[-1].split(".")[0])
            piece = self.gameController.actualPlayer.jouerPiece(numPiece-1)
            couleurJoueur = self.gameController.actualPlayer.getCouleur()
            indexJoueur = self.gameController.joueurs.index(self.gameController.actualPlayer)
            nb_rotation = abs(rotation) // 90
            for i in range(nb_rotation):
                self.gameController.actualPlayer.pieces.rotate(numPiece-1)
                piece = self.gameController.actualPlayer.jouerPiece(numPiece-1)

            if inversion %2 != 0:
                self.gameController.actualPlayer.pieces.reverse(numPiece-1)
                piece = self.gameController.actualPlayer.jouerPiece(numPiece-1)
            pieceBlokus = coordsBlocs(piece, x // 30, y // 30)
            cheminFichierPiece = APP_PATH +  r"/../media/pieces/" + couleurJoueur.upper()[0] + r"/1.png"

            # self.gameController.canvas.destroy()
            self.gameController.actualPlayer.removePiece(numPiece-1)

            for coordY,coordX in pieceBlokus:
                self.gameController.gameView._addToGrid(cheminFichierPiece, coordX,coordY)
                self.gameController.plateau.setColorOfCase(coordY, coordX, indexJoueur)
            

            self.gameController.actualPlayer.hasPlayedPiece(numPiece-1)
            # self.gameController.canvas = canvas
            self.gameController.nextPlayer()
            self.gameController.gameView.update(
                self.gameController.actualPlayer,
                self.gameController.index)
            
            if nb_rotation > 0:    
                self.gameController.actualPlayer.pieces.resetRotation(numPiece-1)

        # Partie changement de couleur
        ctx = Network.receiveMessage(self.client) # ctx = 'couleur'
        print(ctx,'<---- Couleur')
        if self.color == ctx:
            self.gameController.bindWhenYouPlay()
        else:
            self.gameController.unbindAllPiecesWhenNotPlay()







class Server(Thread):

    def __init__(self,ip,controller):
        
        Thread.__init__(self)
        self.daemon = True
        self.server = socket()
        self.server.bind((str(ip), 3000))
        self.server.listen(5)
        self.players = []
        self.controller = controller


    def acceptClients(self):
        index = 0

        while 1:
            client,addr = self.server.accept()
            self.players.append([client,addr])
            print(f"Il y a {len(self.players)} joueur(s) connecté(s)")
            Network.sendMessage(COLORS[index],client)
            if len(self.players) == 4 : break
            index+=1

    def run(self):
        index = 0
        self.acceptClients() # Permet de bien check que 4 clients se connectent au serveur
        Network.sendAllMessage('start',self.players)
        # self.controller.openGame()
        self.gameController = self.controller.controller
        # self.gameController.bindServer(self)
        Network.sendAllMessage(COLORS[index],self.players) # le premier tour pour init les joueurs
        while 1:
            ctx = Network.receiveMessage(self.players[index][0]) # On reçoit les infos du joueur qui vient de jouer
            for player in self.players:
                if player != self.players[index]:
                    Network.sendMessage(ctx,player[0])
            Network.sendMessage('attente',self.players[index][0])

            # Partie chagement de couleur
            index = (index + 1 ) % 4
            Network.sendAllMessage(COLORS[index],self.players)
            




class MultiplayerController(Controller):


    def __init__(self,window : CTk) -> None:
        self.window = window
        self.multiPlayerView = self.loadView("Multiplayer", self.window)
        self.core: Core = Core()


        self.colors = ['Jaune','Vert','Rouge']

        try:
            self.server = Server('0.0.0.0',self)
            self.server.start()
        except:
            pass
        
        client = Client('127.0.0.1',self)
        client.start()

        
    def main(self):
        self.multiPlayerView.main()
    
    def openGame(self):
        self.multiPlayerView.close()
        self.controller = Core.openController("GameMultiplayer", self.window)
        self.controller.main()

    def callbackBoutonTest(self):
        print("coucou")
