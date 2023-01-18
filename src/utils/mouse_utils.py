from customtkinter import CTk

def getMouseX(window:CTk)->int:
    """Permet d'obtenir la position en X de la souris.

    Args:
        window (CTk): la fenêtre du jeu

    Returns:
        int: La position de la souris en X
    """
    return window.winfo_pointerx() - window.winfo_rootx()

def getMouseY(window:CTk)->int:
    """Permet d'obtenir la position en Y de la souris.

    Args:
        window (CTk): la fenêtre du jeu

    Returns:
        int: La position de la souris en Y
    """
    return window.winfo_pointery() - window.winfo_rooty()  