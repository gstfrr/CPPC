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
        return 0

    @staticmethod
    def hexadecimal_to_decimal(hexadecimal):
        return 0

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
