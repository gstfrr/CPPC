from Enlace import Enlace
import math


class User:
    __MAX_SIZE_BITS = 127

    # __MAX_SIZE_BITS = 255

    def __init__(self, host):
        self.__host = host

    def send_message(self, message, destination_address):
        n_segments = int(math.ceil(len(message) / self.__MAX_SIZE_BITS))
        fragments = []
        for i in range(n_segments):
            fragments.append(message[i * self.__MAX_SIZE_BITS:(i + 1) * self.__MAX_SIZE_BITS])

        fragments.append('FIM')
        Enlace.data_indication(destination_address, self.__host, fragments)

    def receive_message(self):
        message = Enlace.data_request()

        print('\n\nMENSAGEM RECEBIDA: ', message)
