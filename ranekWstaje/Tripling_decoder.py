#import sys
def tripling_decode():
    with open("DataSent.txt",'r') as input:        #sys.argv[1]
        with open("DataRecived.txt",'w') as output:   #sys.argv[2]
            while True:

                firstTriple = input.read(1)
                if not firstTriple: break
                if (firstTriple=='\n'):
                    break
                secondTriple = input.read(2)
                #triple = input.read(3)
                triple = firstTriple + secondTriple
                #triple.strip('\n')      #dziwne cos co ma pozbyc sie \n
                if not triple: break
                ones = triple.count('1')
                if ones >= 2:
                    output.write('1')   # 111, 110, 011, 101 --> 1
                else:
                    output.write('0')   # 000, 001, 010, 100 --> 0
