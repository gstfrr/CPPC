from DataFrame import DataFrame
from Conversion import Conversion
import MySocket


class Enlace():

    def __init__(self, address):
        __destination_address = address[0]
        __source_address = address[1]

    def data_request(self, destination_address, l_sdu):
        pass

    @staticmethod
    def data_indication(destination_address, source_address, l_sdu):

        #Delimitador já é inserido no quadro

        # comprimento do payload
        length = Conversion.decimal_to_binary(len(l_sdu))

        # campo de sequencia????
        sequence = '00000000'

        # destino do quadro
        destination_address_frame = Conversion.ip_to_binary(destination_address)

        # origem do quadro
        source_address_frame = Conversion.ip_to_binary(source_address)

        #dados convertidos
        payload = Conversion.string_to_binary(l_sdu)

        frame = DataFrame(
            length,
            sequence,
            destination_address_frame,
            source_address_frame,
            payload)


        # MyCRC = calculacrc(frame.return_data_frame())
        # frame.set__crc(MyCRC)

        print(frame.return_data_frame())



