class ConfirmationFrame:
    __delimiter = None
    __sequence = None
    __destination_address = None
    __source_address = None

    def __init__(self, sequence, destination_address, source_address):
        self.__delimiter = "01111110"
        self.__sequence = sequence
        self.__destination_address = destination_address
        self.__source_address = source_address

    def last_bit_sequence(self):
        return self.__sequence[7]

    def first_bit_sequence(self):
        return self.__sequence[0]

    def return_confirmation_frame(self):
        frame = ''
        frame += self.__delimiter
        frame += self.__sequence
        frame += self.__destination_address
        frame += self.__source_address
        return frame

    @staticmethod
    def string_to_ConfirmationFrame(string):
        delimiter = string[0:8]
        sequence = string[8:16]
        destination_address = string[16:48]
        source_address = string[48:80]
        confirmationFrame = ConfirmationFrame(sequence, destination_address, source_address)

        return confirmationFrame
