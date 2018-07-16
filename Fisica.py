import math
import random


class Fisica:
    __TAXA = 0.1

    @staticmethod
    def add_noise(msg):
        size = len(msg)
        quantidade = math.ceil(Fisica.__TAXA * size)

        for i in range(quantidade):
            pos = random.randrange(0, len(msg))
            l = list(msg)
            l[pos] = Fisica.invert(l[pos])
            msg = ''.join(l)

        return msg

    @staticmethod
    def invert(char):
        if char == '1':
            return '0'
        else:
            return '1'
