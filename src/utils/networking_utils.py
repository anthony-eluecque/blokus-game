from typing_extensions import Self
from Thread import thread
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

class Networking():
    def __init__( self: Self, ip, port ):
        self.listener: socket = socket( AF_INET, SOCK_STREAM ) # Création du socket d'écoute du serveur
        self.listener.setsockopt( SOL_SOCKET, SO_REUSEADDR, 1 )
        self.listener.bind( ( ip, port ) )

        # Liste des threads de chaque joueurs
        self.threads: list[ thread ] = []

    # Attente des joueurs
    def waitPlayers( self: Self, numPlayers: int ):
        print( f'En attente de { numPlayers } joueurs' )

        while True:
            self.listener.listen( numPlayers )
            sck, ( ip, port ) = self.listener.accept()
            newPlayer: thread = thread( sck, ip, port ) # On transmet le socket, l'ip et le port du joueur à un thread du serveur
            newPlayer.start() # lancement du thread
            self.threads.append( newPlayer )
            print( f'Arrivée d\'un nouveau joueur { ip }:{ port }' )

    # Fonctionnement des threads de chaque socket d'écriture
    def manageThreads( self: Self ):
        for th in self.threads: 
            th.join()

# Test de networking
if __name__ == "__main__":
    IPADDR: str = "127.0.0.1"
    PORT: int = 2727
    NUMPLAYERS: int = 2

    network: Networking = Networking( IPADDR, PORT )
    print( "Création du serveur peer to peer" )
    network.waitPlayers( NUMPLAYERS )
    print( "Joueurs connectés, début de la partie" )
    network.manageThreads()
    print( "Joueurs déconnectés" )