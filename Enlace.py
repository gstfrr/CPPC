import random

from ConfirmationFrame import ConfirmationFrame
from DataFrame import DataFrame
from Conversion import Conversion
from MySocketTCP import MySocketTCP
from CRC import CRC
from Fisica import Fisica


class Enlace:

    def __init__(self, address):
        __destination_address = address[0]
        __source_address = address[1]

    @staticmethod  ## Servidor que recebe o frame e responde com o ACK
    def data_request():
        mensagem = ''

        while True:

            socket_receber = MySocketTCP('127.0.0.1')
            resposta = socket_receber.receive()

            if resposta == '#':
                print('CLIENTE DESCONECTOU')
                break

            r2 = DataFrame.string_to_DataFrame(resposta)

            r2_payload_bin = r2.get_payload()
            r2_crc_recebido = r2.get_crc()
            crc_novo = CRC.crc(r2.return_data_frame_to_crc())

            source_bin = r2.get_destination_address()

            destination_bin = r2.get_source_address()
            destination = Conversion.binary_to_ip(destination_bin)

            n_ack = 0
            sequence = r2.first_bit_sequence()
            if crc_novo != r2_crc_recebido:
                sequence += '0000000'
                n_ack = 0
                # manda quadro de confirmação com ack = 0
            else:
                sequence += '0000001'
                n_ack = 1

                mensagem += Conversion.binary_to_string(r2_payload_bin)
                print('MENSAGEM RECEBIDA:', Conversion.binary_to_string(r2_payload_bin))
                print('FRAME OK')

            ack_frame = ConfirmationFrame(sequence, destination_bin, source_bin)



            print('ENVIANDO CONFIRMATION FRAME:   ', ack_frame.return_confirmation_frame())

            ack_socket = MySocketTCP(destination)
            ack_socket.send(ack_frame.return_confirmation_frame())

            print('CONFIRMATION FRAME ENVIADO COM ACK = ', n_ack)

        return(mensagem)

    @staticmethod  ## Cliente que manda
    def data_indication(destination_address, source_address, l_sdu):
        for segment in l_sdu:

            print('MENSAGEM A SER ENVIADA:   ', segment)

            # Delimitador já é inserido no quadro

            # comprimento do payload
            length = Conversion.decimal_to_binary(len(segment))

            # campo de sequencia TODO
            #          SEQ----ACK
            sequence = '00000000'

            # destino do quadro
            destination_address_frame = Conversion.ip_to_binary(destination_address)

            # origem do quadro
            source_address_frame = Conversion.ip_to_binary(source_address)

            # dados convertidos
            payload = Conversion.string_to_binary(segment)

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

            socket_envio = MySocketTCP(destination_address)

            if segment == 'FIM':
                socket_envio.send('#')
            else:
                # Adicionar ruido ao quadro
                # if random.randrange(0, 1):
                #     print('---houve ruido----')
                #     frame_str = Fisica.add_noise(frame_str)

                # ENVIA!!!
                print('FRAME:    ', frame_str)
                socket_envio.send(frame_str)

                print('FRAME ENVIADO')

                receive_ack_socket = MySocketTCP()
                got_it = receive_ack_socket.receive()

                OK = ConfirmationFrame.string_to_ConfirmationFrame(got_it)

                ACK = OK.last_bit_sequence()

                print('ACK RECEBIDO: ', ACK)
