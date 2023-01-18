import json
from models.Player import Player
def makeClassement(joueurs:list[Player]):
    """Fonction permettant de réaliser un classement trier du plus bas en point au plus haut.
    Attention , ici nous sommes avec des nombres négatifs pour le score, donc le résultat sera l'inverse
    (Le plus bas en point sera le premier, et le + haut le dernier).

    Args:
        joueurs (list[Player]): la liste des joueurs.
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
    writeInJson(classement)

def writeInJson(classement):
    """Permet d'écrire dans un fichier json le résultat du classement

    Args:
        classement : le classement de la partie
    """
    classement = json.dumps(classement,indent=4)
    with open("./src/classement.json","w") as outfile:
        outfile.write(classement)

def openJson():
    """
    Fonction permettant d'ouvrir un fichier json

    Returns:
        Le classement de la partie
    """
    with open("./src/classement.json","r") as file:
        classement = json.load(file)
    return classement