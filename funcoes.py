def anoBissexto(ano):
    ano = int(data[6:])
    if ano % 4 == 0:
        if ano % 100 == 0 and ano % 400 != 0:
            return False
        else:
            return True
    else:
        return False

def validarData(data):
    if data[2] or data[5] != '-':
        return True
    if len(data) == 10:
        mes = int(data[3:5])
        dia = int(data[:2])
        if mes in (1, 3, 5, 7, 8, 10, 12):
            if dia not in range(0, 32):
                return True
        elif mes in (4, 6, 9, 11):
            if dia not in range(0,31):
                return True
        elif mes == 2:
            if anoBissexto(data):
                if dia not in range(0,30):
                    return True
            elif dia not in range(0,29):
                return True
    else:
        return True

def validarCpf(cpf):
    if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        return ('CPF inválido!')
    count = 0
    cpfLimpo = (cpf[0:3] + cpf[4:7] + cpf[8:11])
    s = 10
    soma = 0
    for n in cpfLimpo:
        for num in range(9):
            if n == cpfLimpo[num]:
                count += 1
            if count == 81:
                return False
                break
            else:
                continue
    for i in range(9):
        soma += int(cpfLimpo[i]) * s
        s -= 1
    soma = (soma * 10) % 11
    if soma == 10:
        soma = 0
    if soma == int(cpf[12]):
        cpfLimpo = cpf[0:3] + cpf[4:7] + cpf[8:11] + cpf[12]
        s = 11
        soma = 0
        for i in range(10):
            soma += int(cpfLimpo[i]) * s
            s -= 1
        soma = (soma * 10) % 11
        if soma == int(cpf[13]):
            return True
        else:
            return False
        
def checkIn(numSuite, quartosOcupados):
    if numSuite in quartosOcupados:
        return True

def checkOut(numSuite, quartosVagos):
    if numSuite in quartosVagos:
        return False
    else:
        return True

def reserva(numSuite, quartosReservados):
    if numSuite in quartosReservados:
        return False
    else:
        return True