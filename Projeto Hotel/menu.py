import Usefull

def Initial():
    print("1 - Realizar check-in" ,  "2 - Realizar check-out" ,"3 - Fazer reserva" , "4 - Cancelar Reserva", "5 - Visualizar todas as suítes" , "6 - Filtrar suítes" , "7 - Sair",  "\n" ,sep = "\n")
def Option(option = 0):
    while option == 0:
        option = int(input("Escolha uma opção "))
        if option >7 or option <1:
            option = 0
            print("Opção inválida, coloque apenas o número da operação desejada" , "\n")
    return option
def Suites(suites):
    for suite in range(len(suites)):
        categoria = str(suites[suite])
        categoria = categoria.split(" ")
        print(f"Nome da suíte: {suites[suite]}\nCategoria da suite: {categoria[0]}")
    print("\n")
def Filtro(suites,busySuites):
    print(">>>>>>Digite como filtrar uma suíte<<<<<")
    print("1 - Disponíveis em certa data" ,  "2 - CPF" , "3 - Nome", "4 - Indisponíveis em certa data" , "\n" ,sep = "\n")
    while True:
        option = input("Escolha uma opção ")
        if Usefull.isNumber(option) == True:
            option = int(option)
            if option < 1 or option > 4:
                print("Opção inserida não é válida")
                continue
            else:
                break
        else:
            print("Opção inserida não é um número")
            continue
    if option == 1:
        impossibleSuites = Impossibles(busySuites)
        for suite in suites[::-1]:
            for impossibleSuite in impossibleSuites:
                if suite[0] == impossibleSuite[0]:
                    suites.remove(suite)
        print(">>>>>>Essas são as suítes disponíveis nesse período:  (Se nada aparecer significa que não há suítes disponíveis)<<<<<<")
        Suites(suites)
    elif option == 2:
        while True:
            CPF = input("Insira o CPF:\n")
            if Usefull.validarCPF(CPF) == True:
                break
            else:
                print(">>>>>>CPF inserido está inválido<<<<<<")
        for suite in busySuites:
            if suite[2] == CPF:
                print(f"Suíte {suite[0]}, ocupada por {suite[1]}, cujo possui o CPF {suite[2]} está com a reserva marcada do dia {suite[3]} até o dia {suite[4]}")
    elif option == 3:
        nome = input("Insira o seu nome:\n")
        for suite in busySuites:
            if suite[1] == nome:
                print(f"Suíte {suite[0]}, ocupada por {suite[1]}, cujo possui o CPF {suite[2]} está com a reserva marcada do dia {suite[3]} até o dia {suite[4]}")
    elif option == 4:
        impossibleSuites = Impossibles(busySuites)
        print(">>>>>>Essas são as suítes indisponíveis nesse período:  (Se nada aparecer significa que não há suítes indisponíveis)<<<<<<")
        Suites(impossibleSuites)
        print(impossibleSuites)
        #print(f"Data de checkin do outro cliente: {impossibleSuites[3]}\nData de checkout do outro cliente: {impossibleSuites[4]}")
def Impossibles(suites):
    impossibleSuites = []
    while True:
        while True:
            dataEnter = input("Insira a data de entrada:\n")
            if Usefull.validarData(dataEnter) == True:
                break
            else:
                print(">>>>>>Data inválida<<<<<<")
                continue
        while True:
            dataOut = input("Insira a data de saída:\n")
            if Usefull.validarData(dataOut) == True:
                break
            else:
                print(">>>>>>Data inválida<<<<<<")
                continue
        if Usefull.verifyDays(dataEnter,dataOut) == True:
            break
        else:
            print(">>>>>>Intervalo de tempo inválido<<<<<<")
    for suite in suites:
        if Usefull.collisionChecker(suite[3],suite[4],dataEnter,dataOut) == False:
            print(suite[0])
            impossibleSuites.append(suite[0])
    return impossibleSuites