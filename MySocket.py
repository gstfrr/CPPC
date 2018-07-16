import socket


class MySocket:

    __port = 45454

    def __init__(self, host=socket.getfqdn(socket.gethostbyname(socket.gethostname())), port=__port):
        self.__host = host
        self.__port = port

    @staticmethod
    def initsocket():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        return s

    def send(self, msg):
        s = self.initsocket()

        s.connect((self.__host, self.__port))
        s.sendall(msg.encode())
        # data = s.recv(1024)
        s.close()

    def receive(self):
        s = self.initsocket()
        s.bind((self.__host, self.__port))
        s.listen(1)
        data = ''
        received = []
        # recebe mensagem
        while data != b'#':
            # recebe conexao
            conn, addr = s.accept()
            data = conn.recv(3000)
            if not data:
                continue
            conn.close()
            x = data.decode('ascii')
            received.append(x)

        received.pop()
        return received
