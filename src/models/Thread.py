from __future__ import annotations
from threading import Thread
from utils.difficultIA import getSolutions
from models.Player import Player
from models.Plateau import Plateau

class PossibilityThread( Thread ):
    def __init__( self: PossibilityThread, possibilities, joueur, plate, score, x, y, pieceID, nbRota, nbReverse ) -> None:
        Thread.__init__( self )
        self.possibilities: list = possibilities
        self.joueur: Player = joueur
        self.plate: Plateau = plate
        self.score: int = score
        self.x: int = x
        self.y: int = y
        self.pieceID: int = pieceID
        self.nbRota: int = nbRota
        self.nbReverse: int = nbReverse

        self.result: list = []

    def run( self: PossibilityThread ) -> None:
        self.result = getSolutions( self.possibilities, self.joueur, self.predictedPlate, self.score, self.x, self.y, self.pieceID, self.nbRota, self.nbReverse )