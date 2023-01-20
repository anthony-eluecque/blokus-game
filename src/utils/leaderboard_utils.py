import json
from models.Player import Player
import os
from datetime import datetime

def makeClassement(joueurs:list[Player]) -> dict:
    """
    Fonction permettant de créer un dictionnaire avec le classement des joueurs
        
    Args:
        joueurs (list[Player]) : Liste des Players

    Returns:
        dict : Classement de la partie
    """
    classement = {}
    for joueur in joueurs:
        for numPiece in joueur.pieces.pieces_joueurs:
            piece = joueur.jouerPiece(numPiece-1)
            for line in piece:
                for square in line:
                    if square == 1:
                        joueur.removeScore()
        classement[joueur.couleur]=joueur.score
    classement = {k: v for k, v in sorted(classement.items(), key=lambda item: abs(item[1]))}
    return classement

def updateClassementFromPlay(joueur : Player, num_piece : int):
    """
    Procédure qui permet de update le classement dans le fichier json (classement.json).

    Args:
        joueurs (Player) : Joueur à qui il faut update le score
    """
    classement = list(openJson())[-1]
    piece = joueur.jouerPiece(num_piece-1)
    for line in piece:
        for square in line:
            if square == 1:
                classement[joueur.getCouleur()] += 1
    date = datetime.now()
    heure = str(date.hour) + "h" + str(date.minute)
    dat = str(date.day) + "-" + str(date.month) + "-" + str(date.year)
    classement["date"] = dat
    classement["heure"] = heure
    if os.path.exists("./src/classement.json"):
        anciennesParties = list(openJson())
        anciennesParties.pop()
        anciennesParties.append(classement)
        writeJson(anciennesParties)
    else:
        writeJson(classement)  

def writeInJson(classement):
    """
    Fonction permettant de écrire à la suite un classement dans un json (classement.json).

    Args:
        classement (dict) : classement d'une partie
    """
    date = datetime.now()
    heure = str(date.hour) + "h" + str(date.minute)
    dat = str(date.day) + "-" + str(date.month) + "-" + str(date.year)
    classement["date"] = dat
    classement["heure"] = heure
    historique = []
    if os.path.exists("./src/classement.json"):
        anciennesParties = openJson()
        for dico in anciennesParties:
            historique.append(dico)
        historique.append(classement)
        writeJson(historique)
    else:
        historique.append(classement)
        writeJson(historique)

def writeJson(classement):
    """
    Fonction permettant d'écrire dans un json (classement.json)

    Args:
        classement (dict) : classement d'une partie
    """
    classement = json.dumps(classement,indent=4)
    with open("./src/classement.json","w") as outfile:
        outfile.write(classement)

def openJson():
    """
    Fonction permettant de lire dans un json (classement.json)

    Returns:
        list[dict] : Historique des classements
    """
    with open("./src/classement.json","r") as file:
        classement = json.load(file)
    return classement