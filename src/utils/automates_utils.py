import multiprocessing
from random import randint
import threading
from models.Player import Player
from models.Plateau import Plateau
from utils.game_utils import hasAdjacentSameSquare, isInGrid, isValidMove, validPlacement,coordsBlocs,getDiagonals,getAdjacents
from copy import deepcopy
from utils.tree import Tree
from utils.tree import evaluateGame
import math
from time import sleep
import asyncio
import time
from concurrent.futures.thread import ThreadPoolExecutor
import itertools

async def medium_automate(joueurActuel : Player, plateau : Plateau, index : int, view):

    bestMove = await getBestMove(joueurActuel,plateau,index)

    print(bestMove)
    numPiece = bestMove['piece']
    [x,y] = bestMove['position']

    joueurActuel.logPieces.append(numPiece)
    cheminFichierPiece = "./media/pieces/" + joueurActuel.getCouleur().upper()[0] + "/1.png"

    piece = joueurActuel.jouerPiece(numPiece)
    piece = coordsBlocs(piece,y,x)
    for x,y in piece:
        plateau.setColorOfCase(x,y,index)
        view._addToGrid(cheminFichierPiece,y,x)

    return -1

def doMinmax(numPiece: int, plateau: Plateau, possibility:list[int,int], joueur: Player, indexJoueur:int,results):

    x,y = possibility
    check = gameManager.canPlacePiece(numPiece,plateau,x,y,joueur)

    if not check:
        # print(numPiece)
        return None

    if numPiece in joueur.logPieces:
        # print(numPiece)
        return None

    joueur.logPieces.append(numPiece)

    pieceBlokus = coordsBlocs(joueur.jouerPiece(numPiece),y,x)
    for xpos,ypos in pieceBlokus:
        plateau.setColorOfCase(xpos,ypos,indexJoueur)

    score = minmax(joueur,plateau,indexJoueur)

    for xpos,ypos in pieceBlokus:
        plateau.setColorOfCase(xpos,ypos,'X')

    # plateau.undoMove()
    joueur.logPieces.pop()

    # print(numPiece)
    # asyncio.sleep(.5)
    results.put((score,possibility,numPiece))
    return score, possibility, numPiece


async def getBestMove(joueur:Player,plateau:Plateau,indexJoueur:int):
    
    maxScore = -math.inf
    bestMove = None
    bestNumPiece = None

    start_time = time.time()

    possibilities = gameManager.getBestPossibilities(plateau,indexJoueur,joueur)
    print("--------------->",possibilities)
    print("------------> NB POSSIBILITES", len(possibilities))

    from multiprocessing import Queue,Process

    results = Queue()
    processes = []
    for possibility in possibilities:
        for numPiece in joueur.pieces.pieces_joueurs:
            p = Process(target=doMinmax,args=(numPiece,deepcopy(plateau),possibility,deepcopy(joueur),indexJoueur,results))
            processes.append(p)
            p.start()
    for p in processes:
        p.join()
        
    while not results.empty():
        result = results.get()
        if not result:
            continue
        (score,position,numPiece) = result
        if score > maxScore:
            maxScore = score
            bestMove = position
            bestNumPiece = numPiece
    
    end = time.time()
    print("Temps de calcul : ",end-start_time)
    return {'piece':bestNumPiece,'position':bestMove}

def minmax(joueur:Player,plateau:Plateau,indexJoueur,depth=0,maxDepth=3):
    maxScore = -math.inf
    if depth >= maxDepth:
        return gameManager.evaluateGame(plateau,indexJoueur,joueur) 

    possibilities = gameManager.getBestPossibilities(plateau,indexJoueur,joueur)
    for possibility in possibilities:
        for numPiece in joueur.pieces.pieces_joueurs:
            x,y = possibility
            check = gameManager.canPlacePiece(numPiece,plateau,x,y,joueur)

            if not check:
                continue

            if numPiece in joueur.logPieces:
                continue

            joueur.logPieces.append(numPiece)
            pieceBlokus = coordsBlocs(joueur.jouerPiece(numPiece),y,x)
            for xpos,ypos in pieceBlokus:
                plateau.setColorOfCase(xpos,ypos,indexJoueur)
            

            score = minmax(joueur,plateau,indexJoueur,depth+1)
            if score > maxScore:
                maxScore = score 

            for xpos,ypos in pieceBlokus:
                plateau.setColorOfCase(xpos,ypos,'X')

            joueur.logPieces.pop()

    return maxScore


            
TAILLE = 19
class gameManager:

    @staticmethod
    def isInGrid(side:list)->bool:
        if side[0] <= TAILLE and side[1] <= TAILLE and side[0] >= 0 and side[1] >= 0:
            return True
        return False
    
    @staticmethod
    def iterateGrid(plateau:Plateau,indexJoueur:int):
        for i in range(len(plateau.getTab())):
            for j in range(len(plateau.getTab()[0])):
                if plateau.getTab()[i][j] == indexJoueur:
                    yield i,j

    @staticmethod
    def getBestPossibilities(plateau:Plateau, indexJoueur:int, joueur:Player):
        startPos = joueur.getPositionDepart()
        grid = plateau.getTab()
        if grid[startPos[0]][startPos[1]]!=indexJoueur:
            return [startPos]
        
        possibilites = []
        for cell in gameManager.iterateGrid(plateau,indexJoueur):
            possibilites += gameManager.getAdjacents(cell[0],cell[1],plateau,joueur)
        possibilites.sort()
        return list(possibilites for possibilites,_ in itertools.groupby(possibilites))
        # return possibilites

    @staticmethod
    def evaluateGame(plateau:Plateau,indexJoueur:int,joueur:Player):

        grid = plateau.getTab()
        score = 0
        for row in grid:
            for cell in row:
              if cell == indexJoueur:
                score += 1
        return score + len(gameManager.getBestPossibilities(plateau,indexJoueur,joueur))


    @staticmethod
    def canPlacePiece(numPiece:int, plateau:Plateau, x, y, joueur:Player) -> bool:

        piece = joueur.jouerPiece(numPiece)
        return isValidMove(piece,x,y,plateau,joueur)
               
    @staticmethod
    def getAdjacents(y:int , x:int, plateau:Plateau, joueur:Player) ->list:
        possibilites = []
        
        if isInGrid(y - 1, x - 1):
            if not hasAdjacentSameSquare(plateau, joueur, x - 1, y - 1):
                possibilites.append([y - 1, x - 1])

        if isInGrid(y + 1, x - 1):
            if not hasAdjacentSameSquare(plateau, joueur, x - 1, y + 1):
                possibilites.append([y + 1 , x - 1])

        if isInGrid(y - 1, x + 1):
            if not hasAdjacentSameSquare(plateau, joueur, x + 1, y - 1):
                possibilites.append([y - 1 , x + 1])
    
        if isInGrid(y + 1, x + 1):
            if not hasAdjacentSameSquare(plateau, joueur, x + 1, y + 1):
                possibilites.append([y + 1, x + 1])

        return possibilites
    
