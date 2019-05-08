import bchlib
import os
import random
import numpy

from dataConwerterForBCH import convBitsToBytes, convIntListToBinaryStringV2, convIntListToBinaryString


class BCH:
    def __init__(self, p, b):
        self.bch_polynomial = p
        self.bch_bits = b
        self.obj = bchlib.BCH(self.bch_polynomial, self.bch_bits)

    def encode(self, data):
        data = bytearray(data)
        ecc = self.obj.encode(data)
        packet = data + ecc
        return numpy.array(packet)
        # return packet

    def decode(self, packet):
        packet = bytearray(packet)
        data, ecc = packet[:-self.obj.ecc_bytes], packet[-self.obj.ecc_bytes:]

        decoded = self.obj.decode(data, ecc)
        data_decoded = decoded[1]

        return numpy.array(data_decoded)
        # return data+ecc

    def bitflip(self, packet):
        byte_num = random.randint(0, len(packet) - 1)
        bit_num = random.randint(0, 7)
        packet[byte_num] ^= (1 << bit_num)
        return packet


BCH_POLYNOMIAL = 8219
BCH_BITS = 16

my_BCH = BCH(BCH_POLYNOMIAL, BCH_BITS)  # tworzenie obiektu BCH




def part_1():

    data = convBitsToBytes('DataGenerated.txt')


    data_encoded = my_BCH.encode(data)  # kodowanie danych


    convIntListToBinaryStringV2(data_encoded,'DataAfterCodding.txt')




def part_2():
    # with open("DataSent.txt", 'a') as change_a_little:
    #     change_a_little.write('\n')
    data = convBitsToBytes('DataSent.txt')
    data_coruptet=data

    data_decoded = my_BCH.decode((data_coruptet))  # dekodowanie zepsutych danych

    convIntListToBinaryStringV2(data_decoded,'DataRecived.txt')












# data = convBitsToBytes('DataGenerated.txt')
# data_encoded = my_BCH.encode(data)  # kodowanie danych
# convIntListToBinaryStringV2(data_encoded, 'DataAfterCoding.txt')
#
#
# data_coruptet = convBitsToBytes('DataSent.txt')
# data_decoded = my_BCH.decode((data_coruptet))  # dekodowanie zepsutych danych
# convIntListToBinaryStringV2(data_decoded, 'DataRecived.txt')
# #convIntListToBinaryString(data_decoded)








# #def bch_encode():
#
# data = convBitsToBytes('DataGenerated.txt')
# data_encoded = my_BCH.encode(data)  # kodowanie danych
# data_encoded2=numpy.array(bytearray(data_encoded))
# convIntListToBinaryStringV2(data_encoded2, 'DataAfterCoding.txt')
#
#
# #def bch_decode():
# data_coruptet = convBitsToBytes('DataSent.txt')
# data_decoded = my_BCH.decode((data_coruptet))  # dekodowanie zepsutych danych
# data_decoded2=numpy.array(bytearray(data_decoded))
# convIntListToBinaryStringV2(data_decoded2, 'DataRecived.txt')

