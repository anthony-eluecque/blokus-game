from core.Controller import Controller
from core.Core import Core
from customtkinter import CTk

def _openController(oldView,controllerName,window:CTk):
    """_summary_

    Args:
        oldView (View): la vue ouverte actuellement
        controllerName (Controller): Le controller à ouvrir
        window (CTk): la fenêtre de jeu 

    Returns:
        response : le main à exécuter.
    """
    oldView.close()
    c = Core.openController(controllerName,window)
    return c.main()

