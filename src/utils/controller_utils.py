from core.Controller import Controller
from core.Core import Core

def _openController(oldView, controllerName, window):
    oldView.close()
    c = Core.openController(controllerName, window)
    return c.main()

