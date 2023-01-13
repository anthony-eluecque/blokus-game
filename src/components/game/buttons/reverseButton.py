from tkinter import Button,PhotoImage,Canvas
from components.game.buttons.bouton import Bouton

class reverseButton(Bouton):

    def __init__(self,master,piece,pngPiece,filePiece,parent,x_pos=1070,y_pos=665) -> None:

        self.master = master
        self.inversion = None 
        self.nbInversion : int = 0 
        self.pngPiece = pngPiece
        self.filePiece = filePiece
        self.piece = piece
        self.parent = parent

        self.main(x_pos,y_pos)

   
    def inversionImage(self,piece:Canvas)->None:
        self.parent.reversePiece(piece)     

    def _createWidget(self):
        if self.inversion:
            self.inversion.destroy()
        self.bgButton = PhotoImage(file="./media/assets/button_inversion.png")
        self.inversion = Button(master = self.master,image = self.bgButton,text="",bg="white",highlightthickness=0,bd=0,border=0,command=lambda:self.inversionImage(self.piece))

    def _placeWidget(self, x_pos: int, y_pos: int):
        if self.inversion:
            self.inversion.place(x=x_pos,y=y_pos)
        # self.inversion.place(x=1070,y=665)


    def main(self,x_coord,y_coord):
    
        self._createWidget()
        self._placeWidget(x_coord,y_coord)
        


    


