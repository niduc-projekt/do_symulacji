#import sys
def tripling_code():

    with open("DataGenerated.txt", 'r') as input:   #sys.argv[1]
        with open("DataAfterCodding.txt", 'w') as output:      #sys.argv[2]
            while True:
                i = input.read(1)
                if not i: break
                for n in range(0, 3):
                    output.write(i)