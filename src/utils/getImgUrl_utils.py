import tkinter as tk
import urllib.request
import base64

def getImg(url : str):
    u = urllib.request.urlopen(url)
    raw_data = u.read()
    u.close()
    b64_data = base64.encodebytes(raw_data)
    image = tk.PhotoImage(data=b64_data)
    return image