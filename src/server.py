from tkinter import *
from socket import *
from threading import *
from tkinter import scrolledtext
from MainRes import Main
from controllers.GameController import GameController
from random import choice

    
class Server(Thread):

    def __init__(self):
        
        Thread.__init__(self)
        self.server = socket()
        self.myGame : Main
        self.server.bind(('0.0.0.0', 3000))
        self.server.listen(5)
        self.counter = 0
        self.players = []
        self.colors = ["Bleu", "Jaune", "Vert", "Rouge"]
        self.myColor : str


    def sendAllPeople(self, mess):
        for joueur in self.players:
            joueur[0].send(bytes(mess, encoding="utf8"))
    
    def send(self, player, mess):
        player.send(bytes(mess, encoding="utf8"))

    # Activité du thread
    def run(self):
        print("Waiting for 3 persons...\n")
        while self.counter < 3:
            client,addr = self.server.accept()
            couleur = self.colors.pop(self.colors.index(choice(self.colors)))
            self.send(client, couleur)
            self.players.append([client, addr, self.counter, couleur])
            self.counter+=1
            print(f"{self.counter} Connected")
        print("\nLaunching game !\n")

        self.myColor = self.colors.pop()
        print(f"IA color : {self.myColor}")

        self.sendAllPeople("Launch")
        self.myGame = Main()
        self.gameParam = self.myGame.game

        while self.gameParam.nePeutPlusJouer:
            if self.gameParam.actualPlayer == self.myColor:
                paquet = self.gameParam.paquet
                if paquet != "":
                    self.sendAllPeople(paquet)
                #Récupérer les coordonnées de la pièces posée
                #Envoyé a tous les joueurs les infos de la pièces posée + le joueur suivant (actualPlayer)
                #On fait apparaite le waitingLabel
            else:
                #j'attend les infos de la pièce
                paquet = self.client.recv(1024).decode(encoding="utf8") 

                if paquet != "":
                    #Je recupère les données
                    path = paquet[0]
                    coord = (paquet[1], paquet[2])
                    rotation = paquet[3]
                    inversion = paquet[4]
                    canvas = self.gameParam.canvas

                    #je l'ajoute à mon tableau
                    self.gameParam.callbackGame(path, coord[0], coord[1], rotation, inversion, canvas)

app = Server().start()
