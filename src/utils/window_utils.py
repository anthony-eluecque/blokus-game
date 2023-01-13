from customtkinter import CTk
from tkinter import Frame

def _resizeWindow(window,width:int,heigth:int):

    window.resizable(width=False, height=False)
    _screen_width : int = window.winfo_screenwidth()
    _screen_height : int  = window.winfo_screenheight()
    x : float = (_screen_width/2) - (width/2)
    y : float = (_screen_height/2) - (heigth/2)

    window.geometry('%dx%d+%d+%d' % (width, heigth, x, y))
    window.geometry(str(width) + 'x' + str(heigth))

def _deleteChilds(window : CTk):
    for child in window.winfo_children():
            child.destroy()

def _createFrame(window: CTk , longueur = 700 , hauteur = 1000) -> Frame:
    frame =  Frame(window,width=longueur,height=hauteur)
    frame.pack()
    frame.pack_propagate(False)
    return frame