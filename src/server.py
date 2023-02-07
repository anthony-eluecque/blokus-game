import socket
import os
from _thread import *
from threading import *

host = '127.0.0.1'
port = 2004

class ServerBlokus(Thread):

    server = socket.socket()
    server.bind(('localhost',int(input("Port : "))))
    server.listen(5)
    client,addr = server.accept()

    def __init__(self):
        Thread.__init__(self)
   

    def multi_threaded_client(self,connection):
        connection.send(str.encode('Server is working:'))

        while True:
            data = connection.recv(2048)
            response = 'Server message: ' + data.decode('utf-8')
            if not data:
                break
            connection.sendall(str.encode(response))
        connection.close()

    def run(self):

        while True:
            print(f'Connecté à {self.addr[0]} : {str(self.addr[1])}')
            start_new_thread(self.multi_threaded_client,(self.client,))
        

if __name__ == "__main__":
    # host = '127.0.0.1'
    # port = 2004
    serveur = ServerBlokus()
    # serveur.run()
    