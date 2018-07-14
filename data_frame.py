class data_frame:
    __delimiter = None
    __lenght = None
    __sequence = None
    __destination_address = None
    __source_address = None
    __payload = None
    __crc = None

    def __init__(self, lenght, sequence, destination_address, source_address, payload, crc):
        self.__delimiter = "01111110"
        self.__lenght = lenght
        self.__sequence = sequence
        self.__destination_address = destination_address
        self.__source_address = source_address
        self.__payload = payload
        self.__crc = crc

    def last_bit_sequence(self):
        return self.__sequence[7]

    def first_bit_sequence(self):
        return self.__sequence[0]