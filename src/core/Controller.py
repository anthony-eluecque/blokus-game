import os
import importlib
from config import APP_PATH
import abc
from customtkinter import CTk

class Controller(metaclass=abc.ABCMeta):
    """
    Classe abstraite
    Controller centrale du jeu , permettra d'appeler tous les autres controller 
    Permet de respecter les principes SOLID et de s'assurer que les controllers de chaque vue auront bien
    un main()
    """ 

    @abc.abstractmethod
    def main(self):
        return
    
    def loadView(self, viewName:str,window:CTk):
        """Fonction permettant de charger la vue correspondant au controller.

        Args:
            viewName (str): le nom de la vue (sans View)
            >>> view.loadView("Game",window)
            window (CTk): La fenêtre de jeu

        Returns:
            response : la classe correspondant
        """
        response = None
        viewName = viewName[0].upper()+viewName[1:]+"View"
        # On vérifie que le chemin existe (APP_PATH correspondant à la racine du projet)
        if os.path.exists(APP_PATH+"/views/"+viewName+".py"):
            module = importlib.import_module("views."+viewName)    
            class_ = getattr(module, viewName)
            response = class_(self,window)
        return response
    