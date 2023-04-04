from typing_extensions import Self
from threading import Thread
from socket import socket, _RetAddress

class thread( Thread ): 
    def __init__( self: Self, sck: socket, address: _RetAddress ):
        Thread.__init__( self ) 
        self.socket: socket = sck
        self.ip, self.port: int = address

        print( f'Nouveau thread pour { self.ip }:{ self.port }' )
 
    def run( self ):
        while True:
            message: bytes = self.socket.recv( 2048 ) 
            print( f'Réception du client: { message }' )

            response: str = input( "Entrez la réponse du serveur ou exit pour sortir:" )

            if response == 'exit':
                break

            self.socket.send( response )