from Enlace import Enlace
import math


class User:

    __MAX_SIZE_BITS = 127
    # __MAX_SIZE_BITS = 255

    def __init__(self, host):
        self.__host = host

    def send_message(self, message, destination_address):
        npackets = int(math.ceil(len(message) / self.__MAX_SIZE_BITS))
        listpackets = []
        for i in range(npackets):
            listpackets.append(message[i * self.__MAX_SIZE_BITS:(i + 1) * self.__MAX_SIZE_BITS])

        for segment in listpackets:
            print(segment)
            Enlace.data_indication(destination_address, self.__host, segment)
        Enlace.data_indication(destination_address, self.__host, 'FIM')

    def receive_message(self):
        message = Enlace.data_request()

        print(message)
