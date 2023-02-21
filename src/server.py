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

    while counter<2:
        self.client,self.addr = server.accept()
        self.joueurs.append([self.client,self.addr])
        counter+=1

    print("c tipar")
    for client in self.joueurs:
        print(client)
        # text = "start"
        # client[0].send(text.encode('utf-8'))

    # self.clienttext="start"

    while 1:
        try:
            text = server.recv(1024)
            if not text: break
        except:
            break

app = App().start()
