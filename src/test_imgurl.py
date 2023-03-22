from utils.getImgUrl_utils import getImg
import tkinter

URL_BLEU = [
    "https://i.goopics.net/t9htur.png" , "https://i.goopics.net/hf8bny.png", "https://i.goopics.net/bn4d0e.png", "https://i.goopics.net/4uxu23.png", "https://i.goopics.net/cl2x9u.png", "https://i.goopics.net/drdok6.png", "https://i.goopics.net/ad6s8k.png", "https://i.goopics.net/7br0jw.png", "https://i.goopics.net/a977tl.png", "https://i.goopics.net/v6e1vu.png", "https://i.goopics.net/2cc5tl.png", "https://i.goopics.net/i7wa73.png", "https://i.goopics.net/668ilk.png", "https://i.goopics.net/igfxdx.png", "https://i.goopics.net/36byxn.png", "https://i.goopics.net/fg3ltm.png", "https://i.goopics.net/rnms66.png", "https://i.goopics.net/906h6l.png", "https://i.goopics.net/6wy8qa.png", "https://i.goopics.net/52otyq.png", "https://i.goopics.net/s5hc6q.png"]

window = tkinter.Tk()
img = getImg(URL_BLEU[0])
label = tkinter.Label(image=img)
label.pack()
window.mainloop()