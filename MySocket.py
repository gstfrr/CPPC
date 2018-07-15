import socket


class MySocket:

    def __init__(self, host, port=45454):
        self.__host = host
        self.__port = port

    @staticmethod
    def initsocket():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return s

    def send(self, msg):
        s = self.initsocket()
        s.sendall(msg.encode())
        data = s.recv(1024)
        s.close()
        print('cliente enviou: ', data)

    def receive(self):
        s = self.initsocket()
        s.bind((self.__host, self.__port))
        s.listen(1)



        # recebe mensagem
        while 1:
            # recebe conexao
            conn, addr = s.accept()
            print('Connected by', addr)
            data = conn.recv(1024)
            if not data:
                break
            print('servidor recebeu', repr(data))

            # responde
            conn.sendall("valeu".encode())
            conn.close()
            return repr(data)
