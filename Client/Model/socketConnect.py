import socket


class socketConnect:
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.server.bind(('localhost', 1002))
        self.server.listen()
        self.client_socket, self.client_address = self.server.accept()


    def sendDataPC(self, jsonData):
        self.client_socket.send(jsonData.encode("utf-8"))