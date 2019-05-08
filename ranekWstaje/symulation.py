import generator
import Tripling_codder
import Channel
import Tripling_decoder
import ResultsTable
import BSC_Channel
import Gilbert_Channel
import bch_fg

userInputData=300
packet_size=64  #tylko potegi 8ki
if(userInputData> 7):       #7000 #7983
    #zrob paczkami
    iter=0
    with open("AllDataGenerated.txt", 'w') as mainInput:
        with open("AllDataRecived.txt", 'w') as mainOutput:
            while (iter < userInputData):
                    generator.generate_f(packet_size, True)
                    with open("DataGenerated.txt", 'r') as small_input:
                        while True:
                            bitX = small_input.read(1)
                            if not bitX: break
                            if(bitX!='\n'):
                                mainInput.write(bitX)

                    #dodaj paczke do calosci danych AllDataGenerated.txt


                    bch_fg.part_1()
                    #Channel.passing()
                    #BSC_Channel.passing(0.06)
                    Gilbert_Channel.passing(0.10, 0.1, 0, 0.5)
                    bch_fg.part_2()


                    #dodaj plik DataRecived do danych AllDataRecived.txt
                    with open("DataRecived.txt", 'r') as small_output:
                        while True:
                            bitX = small_output.read(1)
                            if not bitX: break
                            if(bitX!='\n'):
                                mainOutput.write(bitX)
                    iter += packet_size

    ResultsTable.scoresV2()

else:
    generator.generate_f(7983, True)       #parametr ilosc generowanych bitow          True/False jesli dodajemy na koncu pliku '\n'


    #coders------------------------------------------------------------
    #Tripling_codder.tripling_code()
    bch_fg.part_1()

    #channels----------------------------------------------------------
    Channel.passing()
    #BSC_Channel.passing(0.01)     #parametr N - prawdopodobienstwo pojedynczego bledu w modelu BSC
    #Gilbert_Channel.passing(0.01, 0.1, 0, 0.5)       #G_B-prawd. GOOD->BAD 0.01 ,B_G-prawd. BAD->GOOD 0.1,
                                    # errorGood-prawd. bledu w stanie Good ok.0%, errorBad prwad. bledu w stanie BAD ok50%
                                #wstepne absorwacja 99,96% przy bledzie 0.01, ok. 50% przy 0.5



     #decoders  -------------------------------------------
    #Tripling_decoder.tripling_decode()
    bch_fg.part_2()



    ResultsTable.scores()

