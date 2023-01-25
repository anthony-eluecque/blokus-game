# imports
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # Retire l'alerte de pygame dans le terminal
from pygame import mixer
from utils.sound_utils import SOUND_LIST, SOUND_VOLUME

class Sound:
    """
    Classe pour jouer un son ainsi que modifier le volume
    """
    def __init__(self, sound: str) -> None:
        # Initialisation du mixer
        mixer.init()
        # Son
        self.sound = sound.lower()
        # Vérification si le son existe
        assert self.sound in SOUND_LIST, "Sound does not exist"
        # Volume
        self.volume: int|float

    def play(self):
        """Joue un son
        """
        # Coupe le son si il y en a un en train d'être joué
        mixer.music.stop()        

        # Chargement du son
        mixer.music.load("././media/sounds/" + self.sound + ".wav")

        # Si le son à jouer est la musique de fond 
        if(self.sound == "background"):
            self.volume = SOUND_VOLUME["music"]
            self.setVolume(self.volume) # On baisse le son
            mixer.music.play(loops=-1) # Et on joue la musique indéfiniment
        else:
            self.volume = SOUND_VOLUME["sfx"]
            self.setVolume(self.volume) # On monte le son
            mixer.music.play() # On joue le son

    def setVolume(self, i: int|float) -> None:
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