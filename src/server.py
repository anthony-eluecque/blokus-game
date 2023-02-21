from tkinter import *
from socket import *
from threading import *
from tkinter import scrolledtext

    
class App(Thread):

    def __init__(self):
        
        Thread.__init__(self)
        server = socket()
        server.bind(('0.0.0.0', 3000))
        server.listen(5)
        counter = 0
        self.joueurs = []

        print("En attente de la connection de 2 joueurs..\n")
        while counter<2:
            self.client,self.addr = server.accept()
            self.joueurs.append([self.client,self.addr,counter])
            counter+=1
            print(f"Il y a {counter} joueur(s) connectés")

        print("\nLancement de la partie...\n")

    # Activité du thread
    def run(self):
        # Créez ici l'interraction server / client
        pass

app = App().start()
