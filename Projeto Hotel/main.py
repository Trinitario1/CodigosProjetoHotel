import menu , Checkin , Checkout , Usefull , Reserva

suites = []
busySuites = []

while True:
    print(">>>>>>Catalogue as suites com o modelo categoria espaço número, exemplo: Standard 1 (Para sair digite 0)<<<<<<")
    newSuite = input("Digite o nome da suite CORRETAMENTE:\n")
    if newSuite == "0":
        break
    elif newSuite.find(" ") == -1:
        print("Suite no modelo incorreto")
    else:
        suites.append(newSuite)
        print("Suíte inserida corretamente!!")

print(">>> Bem-vindo ao sistema de reserva de suítes do hotel!" , "\n")
while True:
    menu.Initial()
    option = menu.Option()
    choosed = 0
    if option == 1:
        choosed = Checkin.Suite(suites) - 1
        busySuites.append([suites[choosed],'0','0','0','0'])
        print(busySuites)
        choosed = len(busySuites) - 1
        print(len(busySuites))
        busySuites[choosed][1] = Checkin.Name()
        busySuites[choosed][2] = Checkin.CPF()
        while True:
            busySuites[choosed][3] = Checkin.DayIn()
            busySuites[choosed][4] = Checkin.DayOut()
            if Usefull.verifyDays(busySuites[choosed][3] , busySuites[choosed][4]) == True:
                break
            print(">>>>>>>Intervalo de tempo inválido, data checkin maior que data de checkout<<<<<<\n")
        print(busySuites[choosed])
    elif option == 2:
        CPF = Checkout.CPF()
        for suite in range(len(busySuites)):
            if busySuites[suite][2] == CPF:
                busySuites.pop(suite)
                print(">>>>>>Check-out realizado com sucesso!<<<<<")
                break
            elif suite == len(busySuites) - 1:
                print(">>>>>>CPF informado não possui suite no momento, faça check-in primeiro<<<<<<")
    elif option == 3:
        suite = Checkin.Suite(suites)
        reserved = Reserva.reservas(suite, busySuites)
        if  reserved != str:
            reserved[0] = suites[suite]
            busySuites.extend([reserved])
            print(">>>>>>Reserva confirmada com sucesso<<<<<<")
        else:
            print(reserved)
    elif option == 4:
        CPF = Checkout.CPF()
        for suite in range(len(busySuites)):
            if busySuites[suite][2] == CPF:
                busySuites.pop(suite)
                print(">>>>>>Reserva cancelada com sucesso!<<<<<")
                break
            elif suite == len(busySuites) - 1:
                print(">>>>>>CPF informado não possui suite no momento, faça reserva primeiro<<<<<<")
        
    elif option == 5:
        print(">>>>>>Todas as suites catalogadas<<<<<\n")
        menu.Suites(suites)
    elif option == 6:
        menu.Filtro(suites,busySuites)
    elif option == 7:
        break