class CRC:
    """description of class"""

    @staticmethod
    def crc(msg):

        # Append the code to the message. If no code is given, default to '000'

        div = '11000000000000101'
        code = (len(div) - 1) * '0'
        msg = msg + code

        msg = list(msg)
        div = list(div)

        # Loop over every message bit (minus the appended code)
        for i in range(len(msg) - len(code)):
            # If that messsage bit is 1, perform modulo 2 multiplication
            if msg[i] == '1':
                for j in range(len(div)):
                    # Perform modulo 2 multiplication on each index of the divisor
                    msg[i + j] = str((int(msg[i + j]) + int(div[j])) % 2)

        # Output the last error-checking code portion of the message generated
        return ''.join(msg[-len(code):])
