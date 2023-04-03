from socket import socket
from threading import Thread
from core.Controller import Controller
from core.Core import Core
from customtkinter import CTk
from time import sleep
from utils.controller_utils import _openController
from constants import COLORS

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
    self.gameController.unbindAllPiecesWhenNotPlay() # On unbind tous les joueurs
    ctx = Network.receiveMessage(self.client) # ctx = 'couleur'
    



class Server(Thread):

    def __init__(self,ip,controller,color):
        
        Thread.__init__(self)
        self.daemon = True
        self.server = socket()
        self.server.bind((str(ip), 3000))
        self.server.listen(5)
        self.players = []
        self.color = color 
        self.controller = controller


    def acceptClients(self):
        index = 0
        while 1:
            client,addr = self.server.accept()
            self.players.append([client,addr])
            print(f"Il y a {len(self.players) + 1 } joueur(s) connecté(s)")
            Network.sendMessage(COLORS[index],client)
            if len(self.players) == 3 : break
            index+=1

    def run(self):
        self.acceptClients() # Permet de bien check que 3 clients se connectent au serveur
        Network.sendAllMessage('start',self.players)
        self.controller.openGame()
        self.gameController = self.controller.controller
        self.gameController.bindServer(self)

        couleur = self.gameController.actualPlayer.getCouleur()
        




class MultiplayerController(Controller):


    def __init__(self,window : CTk) -> None:
        self.window = window
        self.multiPlayerView = self.loadView("Multiplayer", self.window)
        self.core: Core = Core()

        self.erreur = True

        self.colors = ['Jaune','Vert','Rouge']

        try:
            self.server = Server('0.0.0.0',self,'Bleu')
            self.server.start()
            self.erreur = False
        except:
            pass
        
        if self.erreur:
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
