#import sys
def tripling_decode():
    with open("DataSent.txt",'r') as input:        #sys.argv[1]
        with open("DataRecived.txt",'w') as output:   #sys.argv[2]
            while True:
                triple = input.read(3)
                if not triple: break
                ones = triple.count('1')
                if ones >= 2:
                    output.write('1')   # 111, 110, 011, 101 --> 1
                else:
                    output.write('0')   # 000, 001, 010, 100 --> 0
