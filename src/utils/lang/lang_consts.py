RULES_FR: list[str] = [
        "• La première pièce doit être posée dans le coin correspondant du       plateau.\n\n",
        "• Pour placer une pièce, elle ne doit pas être adjacente à une   autre pièce de la même couleur.\n\n",
        "• Cependant, elle doit toucher le coin d’une pièce de la même  couleur.\n\n",
        "• Il faut placer le plus de pièces possible sur le plateau.\n\n",
        "• Bloquer un adversaire pour l’empêcher de poser ses pièces  est autorisé.\n\n",
        "• Quand vous ne pouvez plus placer de pièces, passez votre    tour.\n\n",
        "• La partie se termine quand tous les joueurs ne peuvent plus placer de pièces.\n\n",
        "• Le gagnant est la personne ayant le plus de points à la fin de la partie.",
        ]

RULES_EN: list[str] = [
        "• The first piece must be placed in the corresponding corner of the board.\n\n",
        "• To place a piece, it must not be adjacent to another piece of the same color.\n\n",
        "• However, it must touch the corner of a piece of the same color.\n\n",
        "• You must place as many pieces as possible on the board.\n\n",
        "• Blocking an opponent to prevent him from placing his pieces is allowed.\n\n",
        "• When you can't place any more pieces, skip your turn.\n\n",
        "• The game ends when all players cannot place any more pieces.\n\n",
        "• The winner is the person with the most points at the end of the game.\n\n",
        ]

LANGUAGES: list[str] = ["FR", "EN"]

LANG_CONTENT: dict[str, dict[str | int, str | list[str]]] = {
    "FR" : {
        # PAGE PRINCPALE
        "playButton" : "", # Path
        "rulesButton" : "", # Path
        "statsButton" : "", # Path
        "leaveButton" : "", # Path
        "created" : "Jeu créé par ELUECQUE Anthony, GINIAUX Anatole, DOURNEL Frédéric et LABIT Evan, BUT2 Calais", # Texte

        # BOUTONS
        "returnButton" : "", # Path

        # RÈGLES
        "rules" : RULES_FR,
        "rulesTitle" : "Règles du Blokus", # Texte
        
        # PARAMÈTRES
        "settingsTitle" : "Paramètres", # Texte
        "soundLabel" : "Son : ", # Texte
        "sfxLabel" : "SFX : ", # Texte
        "applyButton" : "", # Path

        # SCORE
        "scoreLabel" : "Tableau des scores", # Text
        1 : "er", # Texte
        2 : "ème", # Texte
        3 : "ème", # Texte
        4 : "ème", # Texte
        "podiumLabel" : [" avec ", " points."], # Textes

        # JEU
        "newGameButton" : "", # Path
        "popup" : ["Le joueur ", " ne peut plus joueur."], # Textes
        "playerList" : ["Bleu", "Jaune", "Vert", "Rouge"], # Textes
        "counterPiece" : " Pièces Restantes", # Texte
        "playerTurn" : "Joueur " # Texte
    },
    "EN" : {
        # MAIN PAGE
        "playButton" : "", # Path
        "rulesButton" : "", # Path
        "statsButton" : "", # Path
        "leaveButton" : "", # Path
        "created" : "Game created by ELUECQUE Anthony, GINIAUX Anatole, DOURNEL Frédéric and LABIT Evan, BUT2 Calais", # Text

        # BUTTONS
        "returnButton" : "", # Path

        # RULES
        "rules" : RULES_EN,
        "rulesTitle" : "Blokus Rules", # Text
        
        # SETTINGS
        "settingsTitle" : "Settings", # Text
        "soundLabel" : "Sound : ", # Text
        "sfxLabel" : "SFX : ", # Text
        "applyButton" : "", # Path

        # SCORE
        "scoreLabel" : "Scoreboard", # Text
        1 : "st", # Text
        2 : "nd", # Text
        3 : "rd", # Text
        4 : "th", # Text
        "podiumLabel" : [" with ", " points."], # Texts

        # GAME
        "newGameButton" : "", # Path
        "popup" : ["Player ", " can't play anymore"], # Texts
        "playerList" : ["Blue", "Yellow", "Green", "Red"], # Texts
        "counterPiece" : " Remaining Pieces", # Text
        "playerTurn" : "Player " # Text
    }
}