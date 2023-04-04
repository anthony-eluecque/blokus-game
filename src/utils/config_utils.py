from json import dumps, loads
from config import APP_PATH

class Configuration:
    """
    Classe gérant la configuration des parties afin de lier la configuration de partie aux parties
    (noms des joueurs, couleur des joueurs, et difficulté si ce sont des IAs)
    """
    
    @staticmethod
    def validConfig(config: list) -> bool:
        # { "nom": "", "couleur": "", "diff": estIa and "" or "joueur" }
        
        CHECKIF_PLAYERS = ["Rouge","Bleu","Vert","Jaune"]

        temp = []
        for player in config:
            temp.append(player["couleur"])
            if player["couleur"] not in CHECKIF_PLAYERS:
                return False
        if len(set(temp)) != len(temp):
            return False
        return True


    @staticmethod    
    def saveConfig(config: list) -> bool:

        if not Configuration.validConfig(config): return False
        configJSON: str = dumps(config, indent=4)

        with open(APP_PATH + r"\..\gameconfig.json", "w") as f:
            f.write(configJSON)

        return True

    @staticmethod
    def getConfig() -> list:
        with open(APP_PATH + r"\..\gameconfig.json", "r") as f:
            return loads(f.read())
        
    @staticmethod
    def getConfigServer() -> list:
        with open(APP_PATH + r"\..\gameconfigServer.json", "r") as f:
            return loads(f.read())
        
    @staticmethod
    def getConfigClient() -> list:
        with open(APP_PATH + r"\..\gameconfigClient.json", "r") as f:
            return loads(f.read())

    @staticmethod
    def getColorsOrder() -> list:
        config = Configuration.getConfig() 
        temp = []
        for player in config:
            temp.append(player["couleur"])
        return temp     
