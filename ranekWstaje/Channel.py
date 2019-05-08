#import sys
def passing():
    with open("DataAfterCodding.txt", 'r') as input:  # sys.argv[1]
        with open("DataSent.txt", 'w') as output:  # sys.argv[2]
            while True:
                byteX = input.read(1)
                if not byteX: break
                #
                #
                #
                #zrob cos z byteX
                #
                #
                #
                output.write(byteX)         #obecnie to jest wylacznie "rurka", która nic nie zmienia

