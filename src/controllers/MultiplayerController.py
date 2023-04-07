from socket import socket,gethostname,AF_INET,SOCK_STREAM,gethostbyname
from threading import Thread
from config import APP_PATH
from core.Controller import Controller
from core.Core import Core
from customtkinter import CTk
from time import sleep
from utils.controller_utils import _openController
from constants import COLORS
from utils.data_utils import dataGame
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
        self.gameController.gameView.tourLabel.configure(text="C'est au joueur " + self.gameController.actualPlayer.getCouleur(), text_color="#3D5ECC")
    else:
        self.gameController.gameView.tourLabel.configure(text="C'est à votre Tour !", text_color="blue")


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
        couleurEN = {"Jaune" : "#F9DE2F", "Bleu" : "#3D5ECC", "Vert" : "#45A86B", "Rouge" : "#FF0004"}
        if self.color == ctx:
            self.gameController.bindWhenYouPlay()
            self.gameController.gameView.tourLabel.configure(text="C'est à votre Tour !", text_color=couleurEN[self.gameController.actualPlayer.getCouleur()])
        else:
            self.gameController.unbindAllPiecesWhenNotPlay()
            self.gameController.gameView.tourLabel.configure(text="C'est au joueur " + self.gameController.actualPlayer.getCouleur(), text_color=couleurEN[self.gameController.actualPlayer.getCouleur()])


class Server(Thread):

    def __init__(self,ip,controller):
        
        Thread.__init__(self)
        self.daemon = True
        self.server = socket(AF_INET,SOCK_STREAM)
        self.server.bind((ip, 3000))
        self.server.listen(5)
        self.players = []
        self.controller = controller
        self.db = dataGame()


    def acceptClients(self):
        index = 0

        while 1:

            client,addr = self.server.accept()
            self.players.append([client,addr])
            print(f"Il y a {len(self.players)} joueur(s) connecté(s)")
            Network.sendMessage(COLORS[index],client)
            self.controller.multiPlayerView.onConnection()
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
            ctx_2 = ctx.split(',')
            file = ctx_2[0]
            x = int(ctx_2[1])
            y = int(ctx_2[2])
            rotation = int(ctx_2[3])
            inversion = int(ctx_2[4])
            numPiece = int(file.split("/")[-1].split(".")[0]) - 1

            piece = self.gameController.actualPlayer.jouerPiece(numPiece)
            nb_rotation = abs(rotation) // 90
            for i in range(nb_rotation):
                self.gameController.actualPlayer.pieces.rotate(numPiece)
                piece = self.gameController.actualPlayer.jouerPiece(numPiece)

            if inversion %2 != 0:
                self.gameController.actualPlayer.pieces.reverse(numPiece)
                piece = self.gameController.actualPlayer.jouerPiece(numPiece)
            pieceBlokus = coordsBlocs(piece, x // 30, y // 30)

            self.db.addPoints(COLORS[index],len(pieceBlokus))
            self.db.addToHistoriquePlayer(COLORS[index],y//30,x//30,numPiece,nb_rotation,inversion)
            
            for player in self.players:
                if player != self.players[index]:
                    Network.sendMessage(ctx,player[0])
            Network.sendMessage('attente',self.players[index][0])

            # Partie chagement de couleur
            index = (index + 1 ) % 4
            Network.sendAllMessage(COLORS[index],self.players)
            
# self.db.addPoints(self.gameController.actualPlayer.couleur,len(pieceBlokus))
#             self.db.addToHistoriquePlayer(self.gameController.actualPlayer.couleur,y//30,x//30,numPiece-1,nb_rotation,inversion)



class MultiplayerController(Controller):


    def __init__(self,window : CTk) -> None:
        self.window = window
        self.multiPlayerView = self.loadView("Multiplayer", self.window)
        self.core: Core = Core()


        self.colors = ['Jaune','Vert','Rouge']

    def __initClient(self,ip):
        client = Client(str(ip),self)
        client.start()

    def waitingOthers(self):
        self.multiPlayerView.close()
        self.multiPlayerView.waitingScreen()


    def _createServer(self,ip):
        self.waitingOthers()
        try:
            self.server = Server(gethostbyname(gethostname()),self)
            self.server.start()
        except:
            pass
        # print(gethostbyname(gethostname()))
        # print(self.server.server.getsockname())
        print('----> ip du serveur : ',gethostbyname(gethostname()))
        self.__initClient(gethostbyname(gethostname()))

    def _joinServer(self,ip):
        self.multiPlayerView.close()
        self.multiPlayerView.waitingScreen()
        self.multiPlayerView.onConnectionClient()
        self.__initClient(ip)
        
    def main(self):
        self.multiPlayerView.main()

    def goBackMenu(self):
        _openController(self.multiPlayerView,"Home",self.window)
    
    def openGame(self):
        self.multiPlayerView.close()
        self.controller = Core.openController("GameMultiplayer", self.window)
        self.controller.main()

    def callbackBoutonTest(self):
        print("coucou")
