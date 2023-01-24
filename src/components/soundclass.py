# imports
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # Retire l'alerte de pygame dans le terminal
from pygame import mixer

class Sound:
    """
    Classe pour jouer un son ainsi que modifier le volume
    """
    def __init__(self, sound: str) -> None:
        # Initialisation du mixer
        mixer.init()
        # Constante
        self.sounds: list[str] = ["background", "select", "drop", "button", "testing"]
        # Son
        self.sound = sound.lower()

    def play(self):
        """Joue un son
        """
        # Coupe le son si il y en a un en train d'être joué
        mixer.music.stop()

        # Verification si le son existe
        if(self.sound not in self.sounds):
            return "Sound does not exist"

        # Chargement du son
        mixer.music.load("././media/sounds/" + self.sound + ".wav")

        # Si le son à jouer est la musique de fond 
        if(self.sound == "background"):
            self.setVolume(0) # On baisse le son
            mixer.music.play(loops=-1) # Et on joue la musique indéfiniment
        else:
            self.setVolume(1) # On monte le son
            mixer.music.play() # On joue le son

    def setVolume(self, i: float) -> None:
        """Changer le volume d'un son

        Args:
            i (int): Nouveau volume
        """
        assert i>=0 and i<=1, "Le volume doit être entre 0 & 1"
        mixer.music.set_volume(i)

    def getVolume(self) -> float|int:
        """Obtenir le volume du son qui se joue actuellement

        Returns:
            float|int: Le volume du son actuel
        """
        return round(mixer.music.get_volume(), 2) # Arrondi pour des questions de simplicité


if __name__ == '__main__':
    from customtkinter import CTk 

    w = CTk()

    a = Sound("background")
    a.play()
    print(a.getVolume())
    
    w.mainloop()