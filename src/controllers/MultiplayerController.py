from socket import SHUT_RDWR, SO_REUSEADDR, SOL_SOCKET, socket,gethostname,AF_INET,SOCK_STREAM,gethostbyname
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
from models.Player import Player

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
    couleurEN = {"Jaune" : "#F9DE2F", "Bleu" : "#3D5ECC", "Vert" : "#45A86B", "Rouge" : "#FF0004"}
    ctx = Network.receiveMessage(self.client)  # ctx = 'color'
    self.color = ctx
    print("Ma couleur est ",self.color,"\n")
    self.controller.multiPlayerView.colorLabel.configure(text="Votre couleur : " + self.color, text_color=couleurEN[self.color.upper()[0] + self.color[1:]])
    ctx = Network.receiveMessage(self.client) # ctx = 'start' || 'stop'd
    if ctx=='stop':
        self.controller.closeConnectionByServer()
    else:
        self.controller.openGame() # On ouvre le jeu
        self.gameController = self.controller.controller
        self.gameController.bindClient(self.client)

        ctx = Network.receiveMessage(self.client)

        if ctx != self.color:
            self.gameController.unbindAllPiecesWhenNotPlay() # On unbind tous les joueurs
            self.gameController.gameView.tourLabel.configure(text="C'est au joueur " + self.gameController.actualPlayer.getCouleur(), text_color="#3D5ECC")
        else:
            self.gameController.gameView.tourLabel.configure(text="C'est à votre Tour !", text_color="#3D5ECC")


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

                self.gameController.nextPlayer()
                # self.gameController.gameView.update(
                #     self.gameController.actualPlayer,
                #     self.gameController.index)
            
                
                
                if nb_rotation > 0 or inversion%2 == 1:    
                    self.gameController.actualPlayer.pieces.resetRotation(numPiece-1)

            # Partie changement de couleur
            ctx = Network.receiveMessage(self.client) # ctx = 'couleur' or fin
            print(ctx,'<---- Couleur')
            
            if ctx == 'fin':
                try:
                    _openController(self.gameController.gameView, "Score", self.gameController.window)
                except : pass
            else:
                if self.color == ctx:
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
        self.server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.players = []
        self.controller = controller

    def closeServer(self):
        Network.sendAllMessage('stop',self.players)

        self.server.close()        

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
        self.db = dataGame()
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
            self.player = Player(COLORS[index])
            piece = self.player.jouerPiece(numPiece)
            nb_rotation = abs(rotation) // 90
            pieceBlokus = coordsBlocs(piece, x // 30, y // 30)

            self.db.addPoints(COLORS[index],len(pieceBlokus))
            self.db.addToHistoriquePlayer(COLORS[index],y//30,x//30,numPiece,nb_rotation,inversion)

            for player in self.players:
                if player != self.players[index]:
                    Network.sendMessage(ctx,player[0])
            Network.sendMessage('attente',self.players[index][0])
            
            # Partie chagement de couleur
            finishGame = False
            logIndex = index
            index = (index + 1 ) % 4
            while COLORS[index] in self.gameController.nePeutPlusJouer:
                index = (index + 1 ) % 4
                if len(self.gameController.nePeutPlusJouer) == 4:
                    finishGame = True
                    break
            if finishGame:
                Network.sendAllMessage('fin',self.players)
            else:
                Network.sendAllMessage(COLORS[index],self.players)
            

class MultiplayerController(Controller):


    def __init__(self,window : CTk) -> None:
        self.window = window
        self.multiPlayerView = self.loadView("Multiplayer", self.window)
        self.core: Core = Core()

    def __initClient(self,ip):
        client = Client(str(ip),self)
        client.start()

    def waitingOthers(self):
        couleurEN = {"Jaune" : "#F9DE2F", "Bleu" : "#3D5ECC", "Vert" : "#45A86B", "Rouge" : "#FF0004"}
        self.multiPlayerView.close()
        self.multiPlayerView.waitingScreen()

    def closeConnectionByServer(self):
        _openController(self.multiPlayerView,"Multiplayer",self.window)
        self.multiPlayerView.invalidServerClientSide()

    def _createServer(self, ip):
        try:
            self.server = Server(gethostbyname(gethostname()),self)
            self.server.start()
            self.waitingOthers()
            print('----> ip du serveur : ',gethostbyname(gethostname()))
            self.__initClient(gethostbyname(gethostname()))
            self.multiPlayerView.backMenuServerSide()
        except:
            self.multiPlayerView.choiseJoinOrNot()
    

    def _joinServer(self,ip):
        couleurEN = {"Jaune" : "#F9DE2F", "Bleu" : "#3D5ECC", "Vert" : "#45A86B", "Rouge" : "#FF0004"}
        try:
            self.multiPlayerView.close()
            self.__initClient(ip)
            self.multiPlayerView.waitingScreen()
            self.multiPlayerView.onConnectionClient()
            self.multiPlayerView.colorLabel.configure(text="Votre couleur : " + self.color, text_color=couleurEN[self.color.upper()[0] + self.color[1:]])
        except:
            self.multiPlayerView.close()
            self.multiPlayerView.invalidServer()
        
    def main(self):
        self.multiPlayerView.main()

    def goBackMenu(self):
        _openController(self.multiPlayerView,"Home",self.window)
    
    def goBackMultiMenu(self):
        _openController(self.multiPlayerView,"Multiplayer",self.window)
    
    def closeServ(self):
        self.server.closeServer()
        _openController(self.multiPlayerView,"Multiplayer",self.window)


    def openGame(self):
        self.multiPlayerView.close()
        self.controller = Core.openController("GameMultiplayer", self.window)
        self.controller.main()

    def callbackBoutonTest(self):
        print("coucou")
