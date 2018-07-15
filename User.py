from Enlace import Enlace
import math


class User:

    def __init__(self, host, port):
        self.__host = host
        self.__port = port

    def send_message(self, message, destination_address):
        npackets = math.ceil(len(message) / 255)
        listpackets = []
        for i in range(npackets):
            listpackets.append(message[i * 255:(i + 1) * 255])

        for segment in listpackets:
            Enlace.data_indication(destination_address,self.__host, segment)
            #esperar o ack

    def receive_message(self):
        pass
