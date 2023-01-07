from tkinter import PhotoImage,Canvas,Button
class rotationButton:

    def __init__(self,master,piece,pngPiece,filePiece,parent)->None:

        self.master = master
        self.rotation = None 
        self.angle : int = 0 
        self.pngPiece = pngPiece
        self.filePiece = filePiece
        self.piece = piece,
        self.parent = parent

        self._makeButton()

    def _makeButton(self)->None:

        if self.rotation:
            self.rotation.destroy()
        
        self.bgButton = PhotoImage(file="./media/assets/button_rotation.png")
        self.rotation = Button(master = self.master,image=self.bgButton,text="",bg = 'white',highlightthickness=0,bd=0,border=0,command=lambda:self.rotationImage(self.piece))
        self.rotation.place(x=700,y=665)

    def rotationImage(self,piece:Canvas):
        self.parent.rotationPiece(piece[0])