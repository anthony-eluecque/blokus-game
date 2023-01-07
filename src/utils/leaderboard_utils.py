import json
from models.Player import Player
def makeClassement(joueurs:list[Player]):

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
    writeInJson(classement)

def writeInJson(classement):

    classement = json.dumps(classement,indent=4)
    with open("./src/classement.json","w") as outfile:
        outfile.write(classement)

def openJson():
    with open("./src/classement.json","r") as file:
        classement = json.load(file)
    return classement