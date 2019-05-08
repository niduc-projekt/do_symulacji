import random, sys
def passing(n_prob):
    probability = n_prob    #paramter n float(sys.argv[1])

    with open("DataAfterCodding.txt",'r') as input:
        with open("DataSent.txt",'w') as output:
            while True:
                i = input.read(1)
                #if i == '\n': continue  ####
                if not i: break
                if random.random() < probability:
                    if i != '\n':
                        i = str((int(i)+1)%2)   #zamiana bitu 1 na 0 i na odwrot
                output.write(i)