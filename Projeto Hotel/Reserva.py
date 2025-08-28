import menu , Checkin , Checkout , Usefull , Reserva
def reservas(suite, reservedSuites):
    verificar = False
    nome = Checkin.Name()
    CPF = Checkin.CPF()
    checkInData = Checkin.DayIn()
    checkOutData = Checkin.DayOut()
    for i in range(len(reservedSuites)):
        if suite in reservedSuites[i]:
            verificar = True
    if verificar:
        for s in range(len(reservedSuites)):
            linha = str(reservedSuites[s][0]).find(f'{suite}')
        diaCheckIn = int(checkInData [:2])
        mesCheckIn = int(checkInData [3:5])
        anoCheckIn = int(checkInData [6:])
        diaCheckOut = int(checkOutData [:2])
        mesCheckOut = int(checkOutData [3:5])
        anoCheckOut = int(checkOutData [6:])
        
        if anoCheckIn == int(reservedSuites[linha][3][6:]) or anoCheckIn == int(reservedSuites[linha][4][6:]):
            if mesCheckIn == int(reservedSuites[linha][3][3:5]) or mesCheckIn == int(reservedSuites[linha][4][3:5]):
                if diaCheckIn == int(reservedSuites[linha][3][:2]) or diaCheckIn == int(reservedSuites[linha][4][:2]):
                    return 'Está reservado!'
                else:
                    if diaCheckIn < int(reservedSuites[linha][3][:2]) or diaCheckIn > int(reservedSuites[linha][4][:2]) and diaCheckOut < int(reservedSuites[linha][3][:2]) or diaCheckOut > int(reservedSuites[linha][4][:2]):
                        lista = [suite, nome, CPF, checkInData, checkOutData]
                        return lista
                    else:
                        return 'Está reservado!'
            else:
                if mesCheckIn < int(reservedSuites[linha][3][:2]) or mesCheckIn > int(reservedSuites[linha][4][:2]) and mesCheckOut < int(reservedSuites[linha][3][:2]) or mesCheckOut > int(reservedSuites[linha][4][:2]):
                    if diaCheckIn < int(reservedSuites[linha][3][:2]) or diaCheckIn > int(reservedSuites[linha][4][:2]) and diaCheckOut < int(reservedSuites[linha][3][:2]) or diaCheckOut > int(reservedSuites[linha][4][:2]):
                        lista = [suite, nome, CPF, checkInData, checkOutData]
                        return lista
                    else:
                        return 'Está reservado!'
                else:
                    return 'Está reservado!'
        else:
            if anoCheckIn < int(reservedSuites[linha][3][:2]) or anoCheckIn > int(reservedSuites[linha][4][:2]) and anoCheckOut < int(reservedSuites[linha][3][:2]) or anoCheckOut > int(reservedSuites[linha][4][:2]):
                if mesCheckIn < int(reservedSuites[linha][3][:2]) or mesCheckIn > int(reservedSuites[linha][4][:2]) and mesCheckOut < int(reservedSuites[linha][3][:2]) or mesCheckOut > int(reservedSuites[linha][4][:2]):
                    if diaCheckIn < int(reservedSuites[linha][3][:2]) or diaCheckIn > int(reservedSuites[linha][4][:2]) and diaCheckOut < int(reservedSuites[linha][3][:2]) or diaCheckOut > int(reservedSuites[linha][4][:2]):
                        lista = [suite, nome, CPF, checkInData, checkOutData]
                        return lista
                    else:
                        return 'Está reservado!'
                else:
                    return 'Está reservado!'
            else:
                return 'Está reservado!'
    else:
        lista = [suite, nome, CPF, checkInData, checkOutData]
        return lista
    
def checkinReserva():
    while True:
        suite = input("Digite o número da suíte: ")
        if Usefull.isNumber(suite) == True:
            suite = int(suite)
            if 0 < suite <= len(suites):
                return suite
            else:
                print(">>>>>>Suíte inserida inválida, tente novamente<<<<<<\n")
                continue
        else:
            print(">>>>>>Suíte inserida inválida, tente novamente<<<<<<\n")
            continue