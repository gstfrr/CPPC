from Enlace import Enlace
import math


class User:

    def __init__(self, host):
        self.__host = host

    def send_message(self, message, destination_address):
        npackets = int(math.ceil(len(message) / 255))
        listpackets = []
        for i in range(npackets):
            listpackets.append(message[i * 255:(i + 1) * 255])

        for segment in listpackets:
            Enlace.data_indication(destination_address, self.__host, segment)
        Enlace.data_indication(destination_address, self.__host, 'FIM')

    def receive_message(self):
        message = Enlace.data_request()

        print(message)
