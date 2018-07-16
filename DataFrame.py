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
        self.__crc = ""

    def set__crc(self, crc):
        self.__crc = crc

    def get_crc(self):
        return self.__crc

    def get_length(self):
        return self.__length

    def get_sequence(self):
        return self.__sequence

    def get_source_address(self):
        return self.__source_address

    def get_destination_address(self):
        return self.__destination_address

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

    def return_data_frame_to_crc(self):
        frame = ''
        frame += self.__length
        frame += self.__sequence
        frame += self.__destination_address
        frame += self.__source_address
        frame += self.__payload
        return frame

    @staticmethod
    def string_to_DataFrame(string):
        aux = len(string)
        delimiter = string[0:8]
        length = string[8:16]
        sequence = string[16:24]
        destination_address = string[24:56]
        source_address = string[56:88]
        payload = string[88:aux - 16]
        crc = string[aux - 16:aux]
        dataFrame = DataFrame(length, sequence, destination_address, source_address, payload)
        dataFrame.set__crc(crc)

        return dataFrame

    def get_payload(self):
        return self.__payload
