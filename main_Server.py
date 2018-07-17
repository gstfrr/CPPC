from User import User

import socket

HOST_SOURCE = '127.0.0.1'


def main():
    usuario = User(HOST_SOURCE)

    usuario.receive_message()


if __name__ == '__main__':
    main()
