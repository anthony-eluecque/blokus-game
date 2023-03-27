from tkinter import *
from socket import *
from threading import *
from tkinter.scrolledtext import ScrolledText
from MainClient import Main
    
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
            print("C'EST MON TOUR")
            self.gameParam.gameView.waitingLabel.destroy()
            # while self.gameParam.actualPlayer == self.myColor:
            paquet = self.gameParam.paquet
            if paquet != "":
                self.send(paquet)
                  
          else:
              #j'attend les infos de la pièce
              paquet = self.client.recv(1024).decode(encoding="utf8") 
              print("PAS MON TOUR")
              print(paquet)
              if paquet != "":
                  #Je recupère les données
                  path = paquet[0]
                  coord = (paquet[1], paquet[2])
                  rotation = paquet[3]
                  inversion = paquet[4]
                  canvas = self.gameParam.canvas

                  #je l'ajoute à mon tableau
                  self.gameParam.callbackGame(path, coord[0], coord[1], rotation, inversion, canvas)
                
    except ConnectionRefusedError:
      print("Connexion au serveur échouée")
    finally: 
      self.client.close()

app = Client().start()
    