class Conversion:

    @staticmethod
    def decimal_to_binary(decimal):
        temp = ""
        while decimal > 0:
            s = str(int(decimal % 2))
            temp += s
            decimal = int(decimal / 2)
        if len(temp) < 8:
            s = ""
            i = 0
            size = len(temp)
            loop = 8 - size
            while i < loop:
                s += "0"
                i += 1
            temp = temp + s
        binary = ""
        i = 0
        while i < 8:
            binary += str(temp[7 - i])
            i += 1
        return binary

    @staticmethod
    def decimal_to_hexadecimal(decimal):
        pass

    @staticmethod
    def binary_to_decimal(binary):
        decimal = 0
        for bit in binary:
            if bit == "1":
                decimal = decimal * 2 + 1
            else:
                decimal = decimal * 2
        return decimal

    @staticmethod
    def binary_to_hexadecimal(binary):
        return hex(int(binary, 2))

    @staticmethod
    def hexadecimal_to_string(hexadecimal):
        return bytearray.fromhex(hexadecimal).decode('ascii')

    @staticmethod
    def binary_to_string(bin):
        hex = Conversion.binary_to_hexadecimal(bin)
        s = Conversion.hexadecimal_to_string(hex[2:])
        return s

    @staticmethod
    def hexadecimal_to_binary(hexadecimal):
        a = bin(int(hexadecimal, 16))
        return a.replace('b', '')

    @staticmethod
    def string_to_hexadecimal(string):
        return string.encode('ascii').hex()

    @staticmethod
    def string_to_binary(string):
        string = Conversion.string_to_hexadecimal(string)
        return Conversion.hexadecimal_to_binary(string)

    @staticmethod
    def ip_to_binary(ip):
        ip = ip.split('.')
        binary = ""
        for num in ip:
            binary += Conversion.decimal_to_binary(int(num))
        return binary
