#import sys
#from typing import TextIO
def scoresV2():
    dataNumber = 0
    correctData = 0
    failData = 0
    with open("AllDataGenerated.txt", 'r') as inputX:
        with open("AllDataRecived.txt", 'r') as inputY:

            while True:
                byteX = inputX.read(1)
                byteY = inputY.read(1)
                if not byteX:
                    break
                if byteX=='\n': continue
                if byteX == byteY:
                    correctData += 1
                else:
                    failData += 1
                dataNumber += 1

    procOfGood = ((float(100) * float(correctData)) / float(dataNumber))
    print("Procent poprawnych bitów: ", procOfGood, " %")
    print("Ilość niepoprawnych bitów: ", failData)
    print("Ilość poprawnych bitów: ", correctData)
    print("Ilość wszystkich bitów: ", dataNumber)
    dataBitInNumber = 0
    with open("AllDataGenerated.txt", 'r') as input:
        while True:
            i = input.read(1)
            if not i: break
            if i=='\n': continue
            dataBitInNumber += 1
    print("Ilość bitów informacji: ", str(dataBitInNumber))





def scores():
    dataNumber=0
    correctData=0
    failData=0

    with open("manyRecords.txt",'a') as outputStorage:
        with open("Stats.txt",'w') as output:
            with open("DataGenerated.txt",'r') as inputX:
                with open("DataRecived.txt",'r') as inputY:

                        while True:
                            byteX= inputX.read(1)
                            byteY= inputY.read(1)
                            if not byteX: break
                            if byteX=='\n': continue
                            if byteX==byteY:
                               correctData +=1
                            else:
                                failData +=1
                            dataNumber +=1

            procOfGood = ((float(100) * float(correctData)) / float(dataNumber))
            print("Procent poprawnych bitów: ",procOfGood," %")
            print("Ilość niepoprawnych bitów: ",failData)
            print("Ilość poprawnych bitów: ",correctData)
            print("Ilość wszystkich bitów: ",dataNumber)

            output.write("Procent poprawnych bitów: "+str(procOfGood)+" %"+"\n")
            output.write("Ilość złych bitów: "+str(failData)+"\n")
            output.write("Ilość dobrych bitów: "+str(correctData)+"\n")
            output.write("Ilość wszystkich bitów: "+str(dataNumber)+"\n")
            outputStorage.write(str(procOfGood)+"\t"+str(failData)+"\t"+str(correctData)+"\t"+str(dataNumber)+"\t")

            dataBitInNumber = 0
            with open("DataGenerated.txt", 'r') as input:
                while True:
                    i = input.read(1)
                    if not i: break
                    if i=='\n': continue
                    dataBitInNumber += 1

            codeBitNumber = 0
            with open("DataAfterCodding.txt", 'r') as input:
                while True:
                    i = input.read(1)
                    if not i: break
                    if i=='\n': continue
                    codeBitNumber += 1

            #print("\n")
            print("Ilość bitów informacji: ", str(dataBitInNumber))
            print("Ilość bitów po zakodowaniu: ", str(codeBitNumber))
            print("Ilosc bitow nadmiarowych", str(codeBitNumber-dataBitInNumber))
            print("Procent danych w sygnale :", str(dataBitInNumber*100/codeBitNumber)+" %")
            print("Procent nadmiarowych bitów w sygnale", str((codeBitNumber-dataBitInNumber)*100/codeBitNumber)+" %"+"\n")

            output.write("Ilość bitów informacji: "+ str(dataBitInNumber) + "\n")
            output.write("Ilość bitów po zakodowaniu: "+ str(codeBitNumber) + "\n")
            output.write("Ilosc bitow nadmiarowych"+ str(codeBitNumber - dataBitInNumber) + "\n")
            output.write("Procent danych w sygnale :"+ str(dataBitInNumber * 100 / codeBitNumber) + " %" + "\n")
            output.write("Procent nadmiarowych bitów w sygnale"+ str((codeBitNumber - dataBitInNumber) * 100 / codeBitNumber) + " %" + "\n")
            outputStorage.write(str(dataBitInNumber)+"\t"+str(codeBitNumber)+"\t"+str(codeBitNumber - dataBitInNumber)+"\t"+str(dataBitInNumber * 100 / codeBitNumber)+"\t"
                                +str((codeBitNumber - dataBitInNumber) * 100 / codeBitNumber)+"\n")



def scoresPacket():
    dataNumber=0
    correctData=0
    failData=0

    with open("StatsOfOnePacket.txt",'w') as output:



        #procOfGood = ((float(100) * float(correctData)) / float(dataNumber))
        #print("Procent poprawnych bitów: ",procOfGood," %")
        #print("Ilość niepoprawnych bitów: ",failData)
        #print("Ilość poprawnych bitów: ",correctData)
        #print("Ilość wszystkich bitów: ",dataNumber)

        dataBitInNumber = 0
        with open("DataGenerated.txt", 'r') as input:
            while True:
                i = input.read(1)
                if not i:
                    break
                if i!='\n':
                    dataBitInNumber += 1

        codeBitNumber = 0
        with open("DataAfterCodding.txt", 'r') as input:
            while True:
                i = input.read(1)
                if not i:
                    break
                if i!='\n':
                    codeBitNumber += 1

        #print("\n")
        print("Ilość bitów informacji przed kodowaniem: ", str(dataBitInNumber))
        print("Ilość bitów po zakodowaniu w paczce: ", str(codeBitNumber))
        print("Ilosc bitow nadmiarowych", str(codeBitNumber-dataBitInNumber))
        print("Procent danych w sygnale :", str(dataBitInNumber*100/codeBitNumber)+" %")
        print("Procent nadmiarowych bitów w sygnale", str((codeBitNumber-dataBitInNumber)*100/codeBitNumber)+" %"+"\n")

        output.write( str(dataBitInNumber) + "\n")   #"Ilość bitów informacji
        output.write(str(codeBitNumber) + "\n")     #"Ilość bitów po zakodowaniu: "+
        output.write(str(codeBitNumber - dataBitInNumber) + "\n")       #"Ilosc bitow nadmiarowych"+
       # output.write("Procent danych w sygnale :"+ str(dataBitInNumber * 100 / codeBitNumber) + " %" + "\n")
       # output.write("Procent nadmiarowych bitów w sygnale"+ str((codeBitNumber - dataBitInNumber) * 100 / codeBitNumber) + " %" + "\n")
        #outputStorage.write(str(dataBitInNumber)+"\t"+str(codeBitNumber)+"\t"+str(codeBitNumber - dataBitInNumber)+"\t"+str(dataBitInNumber * 100 / codeBitNumber)+"\t"
        #                    +str((codeBitNumber - dataBitInNumber) * 100 / codeBitNumber)+"\n")