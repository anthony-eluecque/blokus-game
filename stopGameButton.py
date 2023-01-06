from tkinter import PhotoImage,Button

class stopGameButton():

    def __init__(self,master,window):
        self.master = master
        self.window = window
        self.UI()

    def UI(self):

        self.backgroundButtonStop = PhotoImage(file="./assets/button_stop.png")
        self.buttonStop = Button(
            master=self.window, 
            text='', 
            image = self.backgroundButtonStop, 
            command = self.callbackStop, 
            borderwidth=0, 
            bd=0,
            highlightthickness=0,  
            anchor="nw")
        self.buttonStop.place(x=700,y=730)

    def callbackStop(self):
        self.master.stopGame()
        self.window.destroy()