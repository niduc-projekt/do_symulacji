def convBitsToBytes(fileName):
    intTab = []
    output = []

    with open(fileName, 'r') as input:
        while True:
            byte = input.read(8)
            if not byte:
                break;
            intTab.append(byte)
        intTab.pop()

        for oneInt in intTab:
            output.append(int(oneInt, 2))
        intTab.clear()

        intTab = bytearray(output)
        return intTab

def convIntListToBinaryString(byte_arr):
    output=""
    for byte in byte_arr:
        output += "{0:08b}".format(byte)#formatowanie wyjscia aby kazda liczba byla zapisana na 8 znakach
    file = open("binaryOutput.txt","w+")#stworzenie pliku do wypisanania ciagu 0 i 1
    output+='\n'#dodanie znaku nowej linii aby plik w 100% zgadzał się z recznie napisanym plikiem, inaczej jest niepotrzebne
    file.write(output)

def convIntListToBinaryStringV2(byte_arr,file_name):
    output=""
    for byte in byte_arr:
        output += "{0:08b}".format(byte)#formatowanie wyjscia aby kazda liczba byla zapisana na 8 znakach
    file = open(file_name ,"w+")#stworzenie pliku do wypisanania ciagu 0 i 1
    output+='\n'#dodanie znaku nowej linii aby plik w 100% zgadzał się z recznie napisanym plikiem, inaczej jest niepotrzebne
    file.write(output)