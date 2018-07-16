import random

from ConfirmationFrame import ConfirmationFrame
from DataFrame import DataFrame
from Conversion import Conversion
from MySocket import MySocket
from CRC import CRC
from Fisica import Fisica


class Enlace:

    def __init__(self, address):
        __destination_address = address[0]
        __source_address = address[1]

    @staticmethod  ## Servidor que recebe o frame e responde com o ACK
    def data_request():
        socket_receber = MySocket()
        respostas = socket_receber.receive()

        mensagem = ''
        r = respostas

        r2 = DataFrame.string_to_DataFrame(r)

        r2_payload_bin = r2.get_payload()
        r2_crc_recebido = r2.get_crc()
        crc_novo = CRC.crc(r2.return_data_frame_to_crc())

        source_bin = r2.get_destination_address()

        destination_bin = r2.get_source_address()
        destination = Conversion.binary_to_ip(destination_bin)

        sequence = r2.first_bit_sequence()
        if crc_novo != r2_crc_recebido:
            sequence += '0000000'
            # manda quadro de confirmação com ack = 0
        else:
            sequence += '0000001'

            mensagem += Conversion.binary_to_string(r2_payload_bin)

        ack_frame = ConfirmationFrame(sequence, destination_bin, source_bin)

        print('CONFIRMATION FRAME:   ', ack_frame.return_confirmation_frame())

        ack_socket = MySocket(destination)
        ack_socket.send(ack_frame.return_confirmation_frame())

        return (mensagem)

    @staticmethod  ## Cliente que manda
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

        # cria o frame
        frame = DataFrame(
            length,
            sequence,
            destination_address_frame,
            source_address_frame,
            payload)

        # Calcula o crc
        MyCRC = CRC.crc(frame.return_data_frame_to_crc())
        frame.set__crc(MyCRC)

        # cria a string para enviar
        frame_str = frame.return_data_frame()

        socket_envio = MySocket(destination_address)
        if l_sdu == 'FIM':
            socket_envio.send('#')
        else:
            # Adicionar ruido ao quadro
            # if random.randrange(0, 1):
            #     frame_str = Fisica.add_noise(frame_str)

            # ENVIA!!!
            socket_envio.send(frame_str)

            receive_ack_socket = MySocket()
            got_it = receive_ack_socket.receive()

            print(got_it)
