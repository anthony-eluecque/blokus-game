from tkinter import PhotoImage,Button
from customtkinter import CTk
from components.bouton import Bouton
from components.soundclass import Sound

class SoundButton(Bouton, Sound):
    def __init__(self, window: CTk, view, x_coord: int|float, y_coord: int|float) -> None:
        self.window = window
        self.button: Button
        self.bgButton: PhotoImage
        self.view = view 
        self.main(x_coord,y_coord)
    
    def _createWidget(self)->None:
        self.bgButton = PhotoImage(file = "./media/assets/sound_on.png")
        self.img: int = 1 # Current img
        self.button = Button(master = self.window, image = self.bgButton, text="", bg='white', highlightthickness=0, bd=0, border=0, command=self.changeStatus, width=50, height=50)

    def _placeWidget(self, x_pos, y_pos)->None:
        self.button.place(x=x_pos, y=y_pos)

    def changeStatus(self) -> None:
        """Change the status of the sound
        """
        # If the sound is on
        if(self.img==1):
            # New button image
            self.bgButton = PhotoImage(file = "./media/assets/sound_off.png")
            # Changing button image
            self.button.configure(image=self.bgButton)
            # Changing current img
            self.img=0
            # Set the volume to 0
            super().setVolume(0)
        # If the sound is off
        else:
            self.bgButton = PhotoImage(file = "./media/assets/sound_on.png")
            self.button.configure(image = self.bgButton)
            self.img=1
            super().setVolume(0.3)

    def main(self, x_pos, y_pos):
        self._createWidget()
        self._placeWidget(x_pos,y_pos)