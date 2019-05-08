def generate_f(countOfNumbers, addEndl):
    import random, sys

    with open("DataGenerated.txt", 'w') as file:

        amount = countOfNumbers       #int(sys.argv[1])
        for i in range(0, amount):
            file.write(str(random.randint(0, 1)))
        if(addEndl):
            file.write('\n')
print("Witam z symulacji");