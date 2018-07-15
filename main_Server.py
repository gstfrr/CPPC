# from MySocket import MySocket
from User import User

import socket

HOST_SOURCE = socket.getfqdn(socket.gethostbyname(socket.gethostname()))
HOST_DESTINATION = '177.105.2.125'


def main():

    usuario = User(HOST_SOURCE)

    usuario.receive_message()




    # print("MENSAGEM ENVIADA: ", message)

    # def strtobin(input):
    #     input = input.encode('ascii').hex()
    #     input = bin(int(input, 16)).zfill(8)
    #     return input.replace('b','')
    #
    #
    # a = strtobin('mensagem de odio')
    # print(a)

    # cliente = MySocket(HOST_SOURCE, PORT)
    # servidor = MySocket(HOST_SOURCE, PORT)
    # xxx = servidor.receive()
    # cliente.send(message)
    # print(xxx)


if __name__ == '__main__':
    main()
