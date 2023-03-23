from tkinter import *
from socket import *
from threading import *
from tkinter.scrolledtext import ScrolledText
from MainRes import Main
    
class Client(Thread):
  def __init__(self):
    Thread.__init__(self)
    self.myGame : Main
    self.gameParam = self.myGame.game
    self.fin = False
    self.lancement = False
    self.myColor : str

  # Activité du thread
  def run(self):
    self.client = socket()
    try:

      self.client.connect(('localhost', 3000))
      print("client connecté !")
      colorMessage = self.client.recv(1024).decode(encoding="utf8")
      self.myColor = colorMessage
      launchMessage = self.client.recv(1024).decode(encoding="utf8") 
      if launchMessage == "Launch":
        self.myGame = Main()
        

    except ConnectionRefusedError:
      print("Connexion au serveur échouée")
    finally: 
      self.client.close()

app = Client().start()
    