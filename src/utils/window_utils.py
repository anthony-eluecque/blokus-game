from customtkinter import CTk
from tkinter import Frame

def _resizeWindow(window:CTk,width:int,heigth:int):
    """Permet de redimmentionner une fenêtre

    Args:
        window (CTk): la fenêtre
        width (int): la largeur souhaité
        heigth (int): la hauteur souhaité
    """
    window.resizable(width=False, height=False)
    _screen_width : int = window.winfo_screenwidth()
    _screen_height : int  = window.winfo_screenheight()
    x : float = (_screen_width/2) - (width/2)
    y : float = (_screen_height/2) - (heigth/2)

    window.geometry('%dx%d+%d+%d' % (width, heigth, x, y))
    window.geometry(str(width) + 'x' + str(heigth))

def _deleteChilds(window : CTk):
    """Permet de détruire tous les enfants d'une fenêtre (donc tous les éléments sur celle-ci)

    Args:
        window (CTk): la fenêtre actuelle
    """
    for child in window.winfo_children():
            child.destroy()

def _createFrame(window: CTk , longueur = 700 , hauteur = 1000) -> Frame:
    """Permet la création d'une frame dans une fenêtre

    Args:
        window (CTk): La fenêtre actuelle
        longueur (int, optional): Defaults to 700.
        hauteur (int, optional): Defaults to 1000.

    Returns:
        La Frame crée
    """
    frame =  Frame(window,width=longueur,height=hauteur)
    frame.pack()
    frame.pack_propagate(False)
    return frame