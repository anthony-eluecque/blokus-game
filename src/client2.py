from tkinter import *
from socket import *
from threading import *
from tkinter.scrolledtext import ScrolledText
class Receive():
  def __init__(self, server, gettext):

    while 1:
      try:
        text = server.recv(1024)
        if not text: break
        gettext.configure(state='normal')
        gettext.insert(END,'Server >> %s\n'%text)
        gettext.configure(state='disabled')
        gettext.see(END)
      except:
        break
    
class App(Thread):
  client = socket()
  client.connect(('localhost', int(input("Port: "))))

  def __init__(self, master):
    Thread.__init__(self)
    self.master = master

  def run(self):
    text = self.client.recv(1024)
    if text.decode('utf-8') == "start":
        self.client.send(("text").encode('utf-8'))


root = Tk()
root.title('Client Chat')
app = App(root).start()
