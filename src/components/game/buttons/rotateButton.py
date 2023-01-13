from tkinter import PhotoImage,Canvas,Button
from components.game.buttons.bouton import Bouton

class rotationButton(Bouton):

    def __init__(self,master,piece,pngPiece,filePiece,parent,coord_x=700,coord_y=665)->None:

        self.master = master
        self.rotation = None 
        self.angle : int = 0 
        self.pngPiece = pngPiece
        self.filePiece = filePiece
        self.piece = piece,
        self.parent = parent

        self.main(coord_x,coord_y)

    def _createWidget(self):
        if self.rotation:
            self.rotation.destroy()
        self.bgButton = PhotoImage(file="./media/assets/button_rotation.png")
        self.rotation = Button(master = self.master,image=self.bgButton,text="",bg = 'white',highlightthickness=0,bd=0,border=0,command=lambda:self.rotationImage(self.piece))

    def _placeWidget(self, x_pos: int, y_pos: int):
        if self.rotation:
            self.rotation.place(x=x_pos,y=y_pos)

    def rotationImage(self,piece:Canvas):
        self.parent.rotationPiece(piece[0])


    def main(self,x_coord,y_coord):
        
        self._createWidget()
        self._placeWidget(x_coord,y_coord)