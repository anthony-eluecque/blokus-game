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
        self.game : Main
        self.server.bind(('0.0.0.0', 3000))
        self.server.listen(5)
        self.counter = 0
        self.players = []
        self.couleurs = ["Bleu", "Jaune", "Vert", "Rouge"]
        self.myColor : str


    def sendAllPeople(self, mess):
        for joueur in self.joueurs:
            joueur[0].send(bytes(mess, encoding="utf8"))
    
    def send(self, joueur, mess):
        joueur.send(bytes(mess, encoding="utf8"))

    # Activité du thread
    def run(self):
        # Créez ici l'interraction server / client
        print("En attente de la connection de 2 joueurs..\n")
        while self.counter < 2:
            self.client,self.addr = self.server.accept()
            couleur = self.couleurs.pop(choice(self.couleurs))
            self.players.append([self.client, self.addr, self.counter, couleur])
            self.counter+=1
            print(f"Il y a {self.counter} joueur(s) connectés")
        print("\nLancement de la partie...\n")
        self.sendAllPeople("lancement")
        self.game = Main()


app = Server().start()
