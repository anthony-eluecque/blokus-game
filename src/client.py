from tkinter import *
from socket import *
from threading import *
from tkinter.scrolledtext import ScrolledText
from MainRes import Main
    
class Client(Thread):
  def __init__(self):
    Thread.__init__(self)
    self.myGame : Main
    self.fin = False
    self.lancement = False
    self.myColor : str

  def send(self, mess):
    self.client.send(bytes(mess, encoding="utf8"))

  # Activité du thread
  def run(self):
    self.client = socket()
    try:
      self.client.connect(('localhost', 3000))
      print("client connecté !")
      colorMessage = self.client.recv(1024).decode(encoding="utf8")
      self.myColor = colorMessage
      print(f"Your color : {self.myColor}")
      launchMessage = self.client.recv(1024).decode(encoding="utf8") 
      if launchMessage == "Launch":
        self.myGame = Main()
        self.gameParam = self.myGame.game
        while self.gameParam.nePeutPlusJouer:
          if self.gameParam.actualPlayer == self.myColor:
              self.gameParam.gameView.waitingLabel.destroy()
              while self.gameParam.actualPlayer == self.myColor:
                  pass
                  #Récupérer les coordonnées de la pièces posée
                  #Envoyé a tous les joueurs les infos de la pièces posée + le joueur suivant (actualPlayer)
                  #On fait apparaite le waitingLabel
              #sinon
                  #j'attend les infos de la pièce
                  #je l'envoie aux autres joueurs
                  #je l'ajoute à mon tableau

    except ConnectionRefusedError:
      print("Connexion au serveur échouée")
    finally: 
      self.client.close()

app = Client().start()
    