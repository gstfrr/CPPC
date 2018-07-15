import socket


class MySocket:

    def __init__(self, host=socket.getfqdn(socket.gethostbyname(socket.gethostname())), port=45454):
        self.__host = host
        self.__port = port

    @staticmethod
    def initsocket():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return s

    def send(self, msg):
        s = self.initsocket()

        print(self.__host,self.__port)

        s.connect((self.__host, self.__port))
        s.sendall(msg.encode())
        # data = s.recv(1024)
        s.close()

    def receive(self):
        s = self.initsocket()
        s.bind((self.__host, self.__port))
        s.listen(1)
        # recebe mensagem
        while 1:
            # recebe conexao
            conn, addr = s.accept()
            data = conn.recv(1024)
            if not data:
                break
            conn.close()
            return repr(data)
