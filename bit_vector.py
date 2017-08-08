import math


class BitVector(object):

    def __init__(self, num):
        self.arr = [0]*(num/32 + 1)

    def set(self, pos):
        v = self.arr[pos/32]
        v |= 1 << pos % 32
        self.arr[pos/32] = v

    def get(self, pos):
        v = self.arr[pos/32]
        v &= 1 << pos % 32
        return v>0


if __name__ == '__main__':
    bv = BitVector(32)
    bv.set(16)
    print bv.get(15)