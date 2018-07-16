from DataFrame import DataFrame
from Conversion import Conversion
from MySocket import MySocket
from CRC import CRC
from Fisica import Fisica


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

            r2 = DataFrame.string_to_DataFrame(r)

            r2_payload_bin = r2.get_payload()
            r2_crc_recebido = r2.get_crc()
            crc_novo = CRC.crc(r2.return_data_frame_to_crc())

            if crc_novo == r2_crc_recebido:
                pass

            mensagem += Conversion.binary_to_string(r2_payload_bin)



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

        MyCRC = CRC.crc(frame.return_data_frame_to_crc())
        frame.set__crc(MyCRC)

        frame_str = frame.return_data_frame()

        socket = MySocket(destination_address)
        if l_sdu == 'FIM':
            socket.send('#')
        else:
            print('FRAME ORIGINAL:', str(len(l_sdu)), frame_str)

            # Adicionar ruido ao quadro
            # frame_str = Fisica.add_noise(frame_str)
            socket.send(frame_str)
