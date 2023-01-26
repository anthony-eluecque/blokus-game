from json import dumps, loads

class Configuration:
    """
    Classe gérant la configuration des parties afin de lier la configuration de partie aux parties
    (noms des joueurs, couleur des joueurs, et difficulté si ce sont des IAs)
    """
    
    @staticmethod
    def validConfig( config: list ) -> True:
        { "nom": "", "couleur": "", "diff": estIa and "" or "joueur" }
        for player in config:
            for col in player:
                if player[ col ] == "":
                    return False
        return True

    @staticmethod    
    def saveConfig( config: list ) -> None:
        if not Configuration.validConfig( config ): return
        configJSON: str = dumps( config, indent=4 )

        with open( "gameconfig.json", "w" ) as f:
            f.write( configJSON )

    @staticmethod
    def getConfig() -> list:
        with open( "gameconfig.json", "r" ) as f:
            return loads( f.read() )