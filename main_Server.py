from User import User

import socket

HOST_SOURCE = socket.getfqdn(socket.gethostbyname(socket.gethostname()))
HOST_DESTINATION = '177.105.2.125'


def main():
    usuario = User(HOST_SOURCE)

    usuario.receive_message()


if __name__ == '__main__':
    main()
