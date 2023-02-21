from tkinter import *
from socket import *
from threading import *
from tkinter.scrolledtext import ScrolledText
from Main import Main
    
class App(Thread):

  client = socket()
  client.connect(('localhost', 3000))

  def __init__(self, master):
    Thread.__init__(self)
    self.master = master

  # Activité du thread
  def run(self):
    # Créez ici l'interraction server / client
    pass



root = Tk()
root.title('Client Chat')
app = App(root).start()
