from User import User

import socket

HOST_SOURCE = '127.0.0.1'
HOST_DESTINATION = HOST_SOURCE


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

    cliente = User(HOST_SOURCE)

    cliente.send_message(mensagem, HOST_DESTINATION)


if __name__ == '__main__':
    main()
