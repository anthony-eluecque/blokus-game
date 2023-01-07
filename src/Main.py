# -*- encoding:utf-8 -*-
from core.Core import Core
from customtkinter import CTk

"""
    Main class. Responsible for running the application.
"""
class Main:
    @staticmethod    
    def run():
        # try:

            window = CTk()
            print(window)
            Main._resizeWindow(window,700,700)
            app = Core.openController("Home",window)
            app.main()
            window.mainloop()
        # except Exception as e:
        #     print(str(e))

    @staticmethod
    def _resizeWindow(window,width : int, heigth : int):
        
        window.resizable(width=False, height=False)
        _screen_width : int = window.winfo_screenwidth()
        _screen_height : int  = window.winfo_screenheight()
        x : float = (_screen_width/2) - (width/2)
        y : float = (_screen_height/2) - (heigth/2)

        window.geometry('%dx%d+%d+%d' % (width, heigth, x, y))
        window.geometry(str(width) + 'x' + str(heigth))

if __name__ == '__main__':
    Main.run()