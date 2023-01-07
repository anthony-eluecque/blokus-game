import os
import importlib
from config import APP_PATH

class Core:   
    
    @staticmethod
    def openController(controller,window,classement=1):
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