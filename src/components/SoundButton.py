from tkinter import PhotoImage,Button
from customtkinter import CTk
from components.bouton import Bouton
from components.soundclass import Sound
from config import APP_PATH

class SoundButton(Bouton, Sound):
    """Classe héritant des Classes Bouton et Sound 
    Permet une surcouche pour la création du bouton du menu très particulier et unique
    Respecte les principes SOLID.
    """
    def __init__(self, window: CTk, view, x_coord: int, y_coord: int) -> None:
        self.window = window
        self.button: Button
        self.bgButton: PhotoImage
        self.view = view 
        self.main(x_coord,y_coord)
    
    def _createWidget(self)->None:
        """
        Fonction permettant la création du Bouton
        """
        self.bgButton = PhotoImage(file = APP_PATH + r"/../media/assets/sound_off.png")
        self.img: int = 0 # Current img
        self.button = Button(master = self.window, image = self.bgButton, text="", bg='white', highlightthickness=0, bd=0, border=0, command=self.changeStatus, width=50, height=50)

    def _placeWidget(self, x_pos:int, y_pos:int)->None:
        """Fonction permttant de placer le bouton dans son parent (ici la fenêtre)

        Args:
            x_pos (int): la position en X sur la fenêtre.
            y_pos (int): la position en Y sur la fenêtre.
        """
        self.button.place(x=x_pos, y=y_pos)

    def changeStatus(self)->None:
        """
        Fonction permettant de changer l'affichage de l'image sur le bouton
        ON -> OFF
        OFF -> ON
        """
        if(self.img==1):
            self.bgButton = PhotoImage(file= APP_PATH + r"/../media/assets/sound_off.png")
            self.button.configure(image=self.bgButton)
            self.img=0
            super().setVolume(0)
        else:
            self.bgButton = PhotoImage(file = APP_PATH + r"/../media/assets/sound_on.png")
            self.button.configure(image = self.bgButton)
            self.img=1
            super().setVolume(0.3)

    def main(self, x_pos, y_pos)->None:
        self._createWidget()
        self._placeWidget(x_pos,y_pos)