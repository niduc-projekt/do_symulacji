import generator
import Tripling_codder
import Channel
import Tripling_decoder
import ResultsTable
import BSC_Channel
import Gilbert_Channel

n=0.00
#with open("manyRecordsGil.txt", 'a') as outputStorage:
while n<1:
    n1 = 0.00
    while n1 < 1:
        n2 = 0.00
        while n2 < 1:
            n3 = 0.00
            while n3 < 1:
                with open("manyRecords.txt", 'a') as outputStorage:
                    outputStorage.write('{:.2f}'.format(n) + "\t")
                    outputStorage.write('{:.2f}'.format(n1) + "\t")
                    outputStorage.write('{:.2f}'.format(n2) + "\t")
                    outputStorage.write('{:.2f}'.format(n3) + "\t")
                    outputStorage.close();
                generator.generate_f(10000)       #parametr ilosc generowanych bitów
                Tripling_codder.tripling_code()
                #Channel.passing()
                #BSC_Channel.passing(n)     #parametr N - prawdopodobienstwo pojedynczego bledu w modelu BSC
                Gilbert_Channel.passing(0.01, 0.1, 0, 0.5)       #G_B-prawd. GOOD->BAD 0.01 ,B_G-prawd. BAD->GOOD 0.1,
                                                # errorGood-prawd. bledu w stanie Good ok.0%, errorBad prwad. bledu w stanie BAD ok50%
                                            #wstepne absorwacja 99,96% przy bledzie 0.01, ok. 50% przy 0.5
                Tripling_decoder.tripling_decode()
                ResultsTable.scores()
                n3 +=1.0
            n2 +=1.0
        n1 +=0.10
    n +=0.10