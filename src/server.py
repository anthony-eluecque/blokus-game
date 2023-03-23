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
        self.gameParam = self.myGame.game
        self.server.bind(('0.0.0.0', 3000))
        self.server.listen(5)
        self.counter = 0
        self.players = []
        self.colors = ["Bleu", "Jaune", "Vert", "Rouge"]
        self.myColor : str


    def sendAllPeople(self, mess):
        for joueur in self.joueurs:
            joueur[0].send(bytes(mess, encoding="utf8"))
    
    def send(self, joueur, mess):
        joueur.send(bytes(mess, encoding="utf8"))

    # Activité du thread
    def run(self):
        # Créez ici l'interraction server / client
        print("Waiting for 3 persons...\n")
        while self.counter < 3:
            client,addr = self.server.accept()
            couleur = self.colors.pop(choice(self.colors))
            self.send(client, couleur)
            self.players.append([client, addr, self.counter, couleur])
            self.counter+=1
            print(f"{self.counter} Connected")
        print("\nLaunching game !\n")

        self.myColor = self.colors.pop()

        self.sendAllPeople("Launch")
        self.myGame = Main()

        while self.gameParam.nePeutPlusJouer:
            if self.gameParam.actualPlayer == self.myColor:
                pass



app = Server().start()
