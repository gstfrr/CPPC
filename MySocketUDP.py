import socket


class MySocketUDP:
    __port = 12345

    def __init__(self, host='127.0.0.1', port=__port):
        self.__host = host
        self.__port = port

    def send(self, msg):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(msg.encode(), (self.__host, self.__port))

    def receive(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self.__host, self.__port))
        data, addr = sock.recvfrom(2500)
        return data
