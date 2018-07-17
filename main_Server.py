from User import User

import socket

HOST_SOURCE = '127.0.0.1'


def main():
    server = User(HOST_SOURCE)

    server.receive_message()


if __name__ == '__main__':
    main()
