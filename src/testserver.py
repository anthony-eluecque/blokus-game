from socket import socket
from threading import Thread
from tkinter import DISABLED, END, LEFT, NORMAL, Entry, Frame, Label, Tk
from tkinter.scrolledtext import ScrolledText


class Receive():
  def __init__(self, server, gettext):
    #Thread.__init__(self)
    self.server = server
    self.gettext = gettext
    while 1:
      try:
        text = self.server.recv(1024)
        if not text: break
        self.gettext.configure(state=NORMAL)
        self.gettext.insert(END,'client >> %s\n'%text)
        self.gettext.configure(state=DISABLED)
        self.gettext.see(END)
      except:
        break
      
class App(Thread):
  
  server = socket()
  server.bind(('localhost', int(input("Port: "))))
  server.listen(5)
  client,addr = server.accept()

  def __init__(self, master):

    Thread.__init__(self)
    print("test")
    frame = Frame(master)
    frame.pack()
    self.gettext = ScrolledText(frame, height=10,width=100, state=NORMAL)
    self.gettext.pack()
    sframe = Frame(frame)
    sframe.pack(anchor='w')
    self.pro = Label(sframe, text="Server>>");
    self.sendtext = Entry(sframe,width=80)
    self.sendtext.focus_set()
    self.sendtext.bind(sequence="<Return>", func=self.Send)
    self.pro.pack(side=LEFT)
    self.sendtext.pack(side=LEFT)
    self.gettext.insert(END,'Welcome to Chat\n')
    self.gettext.configure(state=DISABLED)

  def Send(self, args):

    self.gettext.configure(state=NORMAL)
    text = self.sendtext.get()
    if text=="": text=" "
    self.gettext.insert(END,'Me >> %s \n'%text)
    self.sendtext.delete(0,END)
    self.client.send(text.encode())
    self.sendtext.focus_set()
    self.gettext.configure(state=DISABLED)
    self.gettext.see(END)

  def run(self):
    Receive(self.client, self.gettext)
    
root = Tk()
root.title('Server Chat')
app = App(root).start()
root.mainloop()