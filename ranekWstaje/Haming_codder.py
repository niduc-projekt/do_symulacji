#http://programacionits.blogspot.com/2013/05/hamming-code.html
import numpy
import random
import sys

def encode(m, g):
    enc = numpy.dot(m, g)%2
    return enc

def decode(m, h):
    dec = numpy.dot(h, m)%2
    return dec

def hamming(length, n, error, bit):
    g =  numpy.array([[1, 0, 0, 0, 0, 1, 1],[0, 1, 0, 0, 1, 0, 1],[0, 0, 1, 0, 1, 1, 0],[0, 0, 0, 1, 1, 1, 1]])
    h = numpy.array([[0, 0, 0, 1, 1, 1, 1],[0, 1, 1, 0, 0, 1, 1],[1, 0, 1, 0, 1, 0, 1],])
    corrected = 0
    uncorrected = 0
    for i in range(n):
        enc = encode(msg, g)