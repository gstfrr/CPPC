# from MySocket import MySocket
from User import User

import socket

HOST_SOURCE = socket.getfqdn(socket.gethostbyname(socket.gethostname()))
HOST_DESTINATION = '177.105.2.125'
PORT = 5555


def main():
    mensagem = "O objetivo deste trabalho e implementar" \
               " uma camada de enlace com servico de " \
               "comunicacao confiavel por meio de sockets. " \
               "O protocolo emprega transmissao confiavel " \
               "do tipo Stop-and-Wait." \
               " Alem da experiencia no dsenvolvimento de " \
               "aplicacoes via socket, este trabalho tem " \
               "como meta utilizar o ambiente de computacao " \
               "interativo Jupyter Notebook ??. " \
               "Este ambiente permite desenvolver uma aplicacao " \
               "web que facilita a compreensao e visualizacao " \
               "de dados, resultados e analises."

    usuario = User(HOST_SOURCE, PORT)

    usuario.send_message(mensagem, HOST_DESTINATION)

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
