# -*- encoding:utf-8 -*-
from controllers.GameController import GameController 
from customtkinter import CTk
from utils.window_utils import _resizeWindow
from config import APP_PATH

class Main: 
    def __init__(self) -> None:
        self.run()

    def run(self):
        try:
            self.window = CTk()
            _resizeWindow(self.window, 700, 700)
            self.window.title("Blokus")
            self.window.iconbitmap(APP_PATH + r'\..\media\Icon\icon.ico')
            self.game = GameController(self.window)
            self.game.main()
            self.window.mainloop()
        except Exception as e:
            print(str(e))

# if __name__ == '__main__':
#     Main.run(Main)
