# imports
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # Remove pygame alert
from pygame import mixer

class Sound:
    def __init__(self, sound: str) -> None:
        # Init mixer
        mixer.init()
        # Constant
        self.SOUND_LIST: list[str] = ["background", "select", "drop", "button"]
        # Sound
        self.sound = sound.lower()

    def play(self):
        """Play a sound

        Args:
            sound (str): Sound to play
        """
        # Stop sound if it is already playing
        mixer.music.stop()

        # Verifying if the sound exist
        if(self.sound not in self.SOUND_LIST):
            return "Sound does not exist"

        # Load sound
        mixer.music.load("././media/sounds/" + self.sound + ".wav")

        # If the sound to play is the background music
        if(self.sound == "background"):
            self.setVolume(0.3) # Down the volume
            mixer.music.play(loops=-1) #Play the music indefinitely
        else:
            self.setVolume(1) # Up the volume
            mixer.music.play() # Play the sound

    def setVolume(self, i: float) -> None:
        """Change the volume of the sound

        Args:
            i (int): New volume 
        """
        assert i>=0 and i<=1, "The volume need to be between 0 and 1"
        mixer.music.set_volume(i)

if __name__ == '__main__':
    from customtkinter import CTk 

    w = CTk()
    a = Sound("select")
    a.play()
    w.mainloop()