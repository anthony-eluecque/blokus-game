from tkinter import PhotoImage,Button
from customtkinter import CTk
from components.game.buttons.bouton import Bouton 

class LeaveButton(Bouton):

    def __init__(self,window:CTk,view,x_coord,y_coord)->None:

        self.window = window
        self.button : Button
        self.bgButton : PhotoImage
        self.view = view 
        self.main(x_coord,y_coord)
    
    def _createWidget(self)->None:

        self.bgButton = PhotoImage(file="./media/assets/button_leave.png")
        self.button = Button(master = self.window, image = self.bgButton,text="",bg='white',highlightthickness=0,bd=0,border=0,command=self.back)

    def _placeWidget(self,x_pos,y_pos)->None:
        self.button.place(x=x_pos,y=y_pos)

    def back(self)->None:
        self.view._leaveGame()

    def main(self,x_pos,y_pos):

        self._createWidget()
        self._placeWidget(x_pos,y_pos)
