from DataFrame import DataFrame
from Conversion import Conversion
from MySocket import MySocket
from CRC import CRC


class Enlace:

    def __init__(self, address):
        __destination_address = address[0]
        __source_address = address[1]

    @staticmethod
    def data_request():
        socket = MySocket()
        respostas = socket.receive()
        mensagem = ''
        for r in respostas:
            r = r[1:]
            r2 = DataFrame.string_to_DataFrame(r)
            r2_bin = r2.get_payload()
            mensagem += Conversion.binary_to_string(r2_bin)

        return (mensagem)

    @staticmethod
    def data_indication(destination_address, source_address, l_sdu):

        # Delimitador já é inserido no quadro

        # comprimento do payload
        length = Conversion.decimal_to_binary(len(l_sdu))

        # campo de sequencia TODO
        #          SEQ----ACK
        sequence = '00000000'

        # destino do quadro
        destination_address_frame = Conversion.ip_to_binary(destination_address)

        # origem do quadro
        source_address_frame = Conversion.ip_to_binary(source_address)

        # dados convertidos
        payload = Conversion.string_to_binary(l_sdu)

        frame = DataFrame(
            length,
            sequence,
            destination_address_frame,
            source_address_frame,
            payload)

        MyCRC = CRC.crc(frame.return_data_frame())
        frame.set__crc(MyCRC)

        socket = MySocket(destination_address)
        if l_sdu == 'FIM':
            socket.send('#')
        else:
            print(frame.return_data_frame())
            socket.send(frame.return_data_frame())
