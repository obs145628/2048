import socket
import threading

class Server:


    def __init__(self, port, host='0.0.0.0', nb_backlog=10):
        self.host = host
        self.port = port
        self.nb_backlog = nb_backlog

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.sock.listen(self.nb_backlog)  # max backlog of connections

        print('XD TCP server listening on {}:{}'.format(self.host, self.port))

        while True:
            csock, address = self.sock.accept()
            print('tt Accepted connection from {}:{}'.format(address[0], address[1]))
            handler = threading.Thread(
                target=self.handle_client_connection,
                args=(csock,)
            )
            handler.start()


    def handle_client_connection(self, csock):
        req = csock.recv(1024)
        print('Received {}'.format(req))
        csock.send('ACK!'.encode())
        csock.close()



class Client:


    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def send(self, barr):
        self.sock.send(barr)

    def recv(self, size):
        return self.sock.recv(size)
    
