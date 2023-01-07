from customtkinter import CTk

def getMouseX(window:CTk)->int:
    return window.winfo_pointerx() - window.winfo_rootx()

def getMouseY(window:CTk)->int:
    return window.winfo_pointery() - window.winfo_rooty()  