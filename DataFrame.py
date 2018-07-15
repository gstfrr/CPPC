class DataFrame:
    __delimiter = None
    __length = None
    __sequence = None
    __destination_address = None
    __source_address = None
    __payload = None
    __crc = None

    def __init__(self, length, sequence, destination_address, source_address, payload):
        self.__delimiter = "01111110"
        self.__length = length
        self.__sequence = sequence
        self.__destination_address = destination_address
        self.__source_address = source_address
        self.__payload = payload

    def set__crc(self, crc):
        self.__crc = crc

    def last_bit_sequence(self):
        return self.__sequence[7]

    def first_bit_sequence(self):
        return self.__sequence[0]

    def return_data_frame(self):
        frame = ''
        frame += self.__delimiter
        frame += self.__length
        frame += self.__sequence
        frame += self.__destination_address
        frame += self.__source_address
        frame += self.__payload
        frame += self.__crc
        return frame
