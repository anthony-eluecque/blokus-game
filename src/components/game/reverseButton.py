from tkinter import Button,PhotoImage,Canvas
from PIL import Image

class reverseButton():

    def __init__(self,master,piece,pngPiece,filePiece,parent) -> None:

        self.master = master
        self.inversion = None 
        self.nbInversion : int = 0 
        self.pngPiece = pngPiece
        self.filePiece = filePiece
        self.piece = piece
        self.parent = parent

        self._makeButton()

    def _makeButton(self)->None:
        
        if self.inversion:
            self.inversion.destroy()
        self.bgButton = PhotoImage(file="./media/assets/button_inversion.png")
        self.inversion = Button(
            master = self.master,image = self.bgButton,text="",bg="white",highlightthickness=0,bd=0,border=0,command=lambda:self.inversionImage(self.piece))
        self.inversion.place(x=1070,y=665)

    def inversionImage(self,piece:Canvas)->None:
        self.parent.reversePiece(piece)     


        


    


