import os
import importlib
from config import APP_PATH

class Core: 
    """
    Classe centrale du jeu , le Main ne connaitra que cette classe et pas le reste du jeu.
    Permet de respecter les principes SOLID.
    """  
    
    @staticmethod
    def openController(controller,window):
        """Fonction permettant de charger le controller.

        Args:
            controller (str): le nom du controller (sans "Controller" à la fin)
            >>> Core.openController("Game",window)
            window (CTk): La fenêtre de jeu

        Returns:
            response : la classe correspondants
        """
        response = None

        controller = controller[0].upper()+controller[1:]
        controllerName = controller+"Controller"
        
        print("----------->")
        print(controllerName)
        if os.path.exists(APP_PATH+"/controllers/"+controllerName+".py"):
            module = importlib.import_module("controllers."+controllerName)
            class_ = getattr(module, controllerName)            
            response = class_(window)
        
        return response