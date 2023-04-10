import customtkinter
from PIL import Image
from components.bouton import Bouton
from config import APP_PATH

class CommandesView(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("900x624")
        self.title("Blokus")
        self.iconbitmap(APP_PATH + r'\..\media\Icon\icon.ico')

        self.bgImage = customtkinter.CTkImage(Image.open(APP_PATH + r"/../media/assets/commands_bg.png"), size=(900, 624))
        self.bg = customtkinter.CTkLabel(self, text="", image = self.bgImage)
        self.bg.place(x = 0, y = 0)

        self.backHome: Bouton = Bouton(self, self, 350, 520, width=206, heigth=49, file=APP_PATH + "/../media/assets/buttun_rules_return.png", son="button", command=self._closeWindow)

    def _closeWindow(self) -> None:
        self.destroy()