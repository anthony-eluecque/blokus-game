from tkinter import PhotoImage,Button


class newGameButton():

    def __init__(self,master,window):

        self.master = master
        self.window = window
        self.UI()

    def UI(self):

        self.backgroundButtonNewGame = PhotoImage(
            file="./assets/button_new_game.png"
        )
        self.buttonNewGame = Button(
            master=self.window, 
            text='', 
            image = self.backgroundButtonNewGame, 
            command = self.emitGame, 
            borderwidth=0, 
            bd=0,
            highlightthickness=0,  
            anchor="nw"
        )
        self.buttonNewGame.place(x=1070,y=730)

    def emitGame(self):
        self.master.newGame()
        self.window.destroy()
