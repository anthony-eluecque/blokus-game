from tkinter import *
from socket import *
from threading import *
from tkinter import scrolledtext
from Main import Main
from controllers.GameController import GameController

    
class Server(Thread):

    def __init__(self):
        
        Thread.__init__(self)
        self.server = socket()
        self.server.bind(('0.0.0.0', 3000))
        self.server.listen(5)
        self.counter = 0
        self.joueurs = []

    def sendAllPeople(self, mess):
        for joueur in self.joueurs:
            joueur[0].send(bytes(mess, encoding="utf8"))


    # Activité du thread
    def run(self):
        # Créez ici l'interraction server / client
        print("En attente de la connection de 2 joueurs..\n")
        while self.counter < 2:
            self.client,self.addr = self.server.accept()
            self.joueurs.append([self.client, self.addr, self.counter])
            self.counter+=1
            print(f"Il y a {self.counter} joueur(s) connectés")
        print("\nLancement de la partie...\n")
        self.sendAllPeople("lancement")
        Main.run()
        GameController.IA()


app = Server().start()
