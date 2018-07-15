import DataFrame
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

        sequence = '00000000'

        destination_address_frame = Conversion.string_to_binary(destination_address)

        source_address_frame = Conversion.string_to_binary(source_address)

        payload = Conversion.string_to_binary(l_sdu)

        length = len(payload)

        crc = '1111111111111111'

        frame = DataFrame(
            length,
            sequence,
            destination_address_frame,
            source_address_frame,
            payload,
            crc)


