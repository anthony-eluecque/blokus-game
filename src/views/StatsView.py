from views.View import View
from utils.window_utils import _resizeWindow, _createFrame, _deleteChilds
from utils.data_utils import jsonManager
from customtkinter import CTk, CTkImage, CTkLabel
from PIL import Image,ImageTk
from tkinter import Button, Label, PhotoImage,Scrollbar,Tk,Listbox,END,BOTH,RIGHT,Y,Frame,Canvas,LEFT,font
from components.stats.gamehistorique import gameHistorique
from components.bouton import Bouton
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np 
from components.game.grille import grille
from utils.game_utils import coordsBlocs
from models.Player import Player
            
try:
    from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
except ImportError:
    from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk as NavigationToolbar2TkAgg

class StatsView(View):
    
    def __init__(self,controller,window:CTk,width=1300,heigth=800) -> None:
        super().__init__()
        self.window = window
        self.statsController = controller

    def _makeFrame(self,width,heigth) -> None:
        self.mainFrame = _createFrame(self.window, width, heigth)

    def _makeBackground(self,xsize,ysize,file="./media/assets/bgStats.png")->None:
        self.bgImage = CTkImage(Image.open(file), size=(xsize, ysize))
        self.bg = CTkLabel(self.window, text="", image = self.bgImage)
        self.bg.place(x = 0, y = 0)

    def _makeTitle(self) -> None:
        self.mainTitle = Label( self.mainFrame, text="", image = self.background, bd = 0 )

    def createWidgets(self)->None:
        self.data = jsonManager.readJson()

        self.widgets = []
        xpos = 80
        ypos = 180

        for idPartie in self.data["parties"]:
            widget = gameHistorique(self.scrollableBody,self,xcoord=xpos,ycoord=ypos,idPartie=idPartie,dictPartie=self.data["parties"][idPartie],command=self.statsController.showWidget)
            self.widgets.append(widget)
            ypos += 65

        self.scrollableBody.update()
        
    def backToHomeButton(self)-> None:
        self.backStats: Bouton = Bouton(self.window, self, 560, 700, width=206, heigth=49, file="./media/assets/buttun_rules_return.png", son="button", command=self._leaveStatsMenu)

    
    def openDetailGame(self,idPartie) -> None:

        _deleteChilds(self.window)
        _resizeWindow(self.window,1000,600)
        self._makeFrame(1000,600)
        self._makeBackground(1000,600,"./media/assets/bgDetailPartie.png")
        self.banners = []

        colors = ["bleu","rouge","vert","jaune"]
        y = 100
        for color in colors:
            banner = self.makeBanner(("./media/assets/banner"+color+".png"),xpos=50,ypos=y)
            self.banners.append(banner)
            y+=110

        PARTIE = self.data["parties"][idPartie]
    
        self.labelWidgets = []
        y_joueur = 160
        for color in colors:
            pseudo = PARTIE[color]["pseudo"]
            if not pseudo:
                pseudo = color[0].upper() + color[1:]
            score = PARTIE[color]["score"]
            widget = CTkLabel(self.window,text=f"Pseudo du joueur : {pseudo} | Score : {score}", bg_color="white",fg_color="white",text_color="black")
            widget.configure(font=('Roboto Bold',15))
            widget.place(x=50,y=y_joueur)
            y_joueur+=110
            self.labelWidgets.append(widget)

        x = 500 ; y= 100
        self.cubes = []
        images = {
            'bleu':'./media/pieces/B/1.png',
            'rouge':'./media/pieces/R/1.png',
            'vert':'./media/pieces/V/1.png',
            'jaune':'./media/pieces/J/1.png'}

        self.grille = grille(self.window,400,400,False)
        self.grille.canvas.place(x=500,y=100)
        

        for color in colors:
            
            player = Player(color.upper()[0]+color[1:])
            logPlacements = PARTIE[color]["historique_placement"]
            img = Image.open('./media/pieces/'+color.upper()[0]+'/1.png')
            w,h = img.size
            img = img.resize((20,20))
            img = ImageTk.PhotoImage(img)
            for placement in logPlacements:
                y,x = placement[0]
                piece = player.jouerPiece(placement[1])
                piece = coordsBlocs(piece,x,y)

                for ypos,xpos in piece:
                    print(ypos,xpos)
                    cube = Canvas(self.window,width=20,height=20,bd=0,highlightthickness=0,relief='ridge')
                    cube.create_image(0,0,image=img,anchor = "nw" )
                    cube.place(x=((xpos*20)+500),y=((ypos*20)+100))
                    self.cubes.append([images[color],cube,img])

        self.backStats: Bouton = Bouton(self.window, self, 400, 540, width=206, heigth=49, file="./media/assets/buttun_rules_return.png", son="button", command=self.statsController.backToStats)


    def makeBanner(self,file,xpos,ypos):
        self.img = CTkImage(Image.open(file),size=(400,40))
        label = CTkLabel(master=self.window,text="",image=self.img, fg_color="white", bg_color="white")
        label.place(x=xpos,y=ypos)
        return label
    
    def _leaveStatsMenu(self):
        self.close()
        self.statsController.backToMenu()

    def main(self, width=1300, height=800) -> None:
        _resizeWindow(self.window, width, height)
        self._makeFrame(width,height)
        self._makeBackground(1300,800)

        self.contentFrame = Frame(self.window)
        self.contentFrame.config(
            highlightbackground="black",
            highlightthickness=1,
            bg='white')
        self.scrollableBody = ScrollableFrame(self.contentFrame,width=16)

        self.contentFrame.configure(width=400,height=500)

        self.contentFrame.place(x=100,y=200)


        self.data = jsonManager.readJson()
        PARTIES = self.data["parties"]
        colors = ["bleu","rouge","vert","jaune"]
        Buttons = []
        for idPartie in PARTIES:
            PARTIE = PARTIES[idPartie]
            text = f"Partie du {PARTIE['date']} à {PARTIE['heure']}"
            
            bestScore = 0
            bestCouleur = ""
            for color in colors:
                score = PARTIE[color]["score"]
                if score>bestScore:
                    bestCouleur = color
                    bestScore = score
            text += f" | Pas de gagnant"
            if bestScore != 0:
                text += f" | Gagnant de la partie {bestCouleur} | Score : {bestScore}"
            button = StatsButton(self.scrollableBody,idPartie,text,command=self.statsController.showWidget)
            Buttons.append(button)

        self.scrollableBody.update()
        VictoryGraph(self.mainFrame)
        # self.createWidgets()
        self.backToHomeButton()



    def close(self) -> None:
        _deleteChilds(self.window)

class StatsButton:

    def __init__(self,master,idGame,text,command=None) -> None:

        style = font.Font(family='Helvetica',size=9)
        self.button = Button(master, text=text)
        if command:
            self.button.configure(command=lambda : command(idGame))
        self.button.configure(height=2,width=80,bd=0,highlightthickness=0)
        self.button.configure(font=style,bg='white')
        self.button.grid()
      
class Graph:
    
    def __init__(self,root) -> None:
        self.frame = Frame()
        self.figure : Figure = Figure(figsize=(5,4.2),dpi=100)
        self.canvas : FigureCanvasTkAgg = FigureCanvasTkAgg(self.figure,self.frame)

        self.frame.place(x=750,y=250)

class VictoryGraph(Graph):

    def __init__(self, root) -> None:
        super().__init__(root)

        self.data = jsonManager.readJson()

        Victories = self.data["overall"]

        yAxesColors = ['Bleu','Rouge','Vert','Jaune']

        xAxesWinrates = []
        for colorVictories in Victories:
            nbGames = Victories[colorVictories]['victoires'] + Victories[colorVictories]['defaites']
            winrate = 0
            if nbGames!=0:
                winrate = round(Victories[colorVictories]['victoires'] / nbGames,2) * 100
            xAxesWinrates.append(int(winrate))

        # plot = self.figure.add_axes([0,0,0,0])
        plot = self.figure.add_subplot(111)
        plot.bar(np.array(yAxesColors),np.array(xAxesWinrates))
        plot.set_xlabel('Couleur')
        plot.set_ylabel('Winrate')
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

    


class ScrollableFrame(Frame):

    def __init__(self,frame,width=16):

        scrollbar = Scrollbar(frame,width=width)
        scrollbar.pack(side=RIGHT,fill=Y,expand=False)

        self.canvas = Canvas(frame,yscrollcommand=scrollbar.set)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.canvas.configure(width=550,height=480)
        self.canvas.configure(bg='white',bd=0,highlightthickness=0)

        scrollbar.config(command=self.canvas.yview)
        self.canvas.bind('<Configure>', self.__fillCanvas)


        Frame.__init__(self, frame)

        self.windows_item = self.canvas.create_window(0,0, window=self, anchor="nw")

    def __fillCanvas(self, event):
        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width = canvas_width)

    def update(self):
        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))
