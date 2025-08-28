def isNumber(string):
    valid = True
    for letter in string:
        if not(letter == "0" or letter == "1" or letter == "2" or letter == "3" or letter == "4" or letter == "5" or letter == "6" or letter == "7" or letter == "8" or letter == "9"):
                valid = False
    return valid

def validarCpf(cpf):
    if cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':
        return False
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
        if soma == 10:
            soma = 0
        if soma == int(cpf[13]):
            return True
        else:
            return False

def anoBissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0 and ano % 400 != 0:
            return False
        else:
            return True
    else:
        return False

def validarData(data):
    if data[2] != "-" or data[5] != '-':
        return False
    if len(data) == 10:
        if isNumber(data[6:]) == False:
            return False
        if isNumber(data[3:5]) == False:
            return False
        if isNumber(data[:2]) == False:
            return False
        dia , mes, ano = separateData(data)
        if mes in (1, 3, 5, 7, 8, 10, 12):
            if dia not in range(1, 32):
                return False
            else:
                return True
        elif mes in (4, 6, 9, 11):
            if dia not in range(1,31):
                return False
            else:
                return True
        elif mes == 2:
            if anoBissexto(ano):
                if dia not in range(1,30):
                    return False
                else:
                    return True
            elif dia not in range(1,29):
                return False
            else:
                return True
    else:
        return False

def verifyDays(data1,data2):
    day1 , month1 , year1 = separateData(data1)
    day2 , month2 , year2 = separateData(data2)
    minusYear = year2 - year1
    minusMonth = month2 - month1
    minusDay = day2 - day1
    if minusYear > 0:
        return True
    elif minusYear < 0:
        return False
    else:
        if minusMonth > 0:
            return True
        elif minusMonth < 0:
            return False
        else:
            if minusDay > 0:
                return True
            else:
                return False

def separateData(data):
    day = data[:2]
    month = data[3:5]
    year = data[6:]
    return int(day),int(month),int(year)

def collisionChecker(minData1 , maxData1 , minData2 , maxData2):
    if verifyDays(minData2,minData1) == True:
        if verifyDays(maxData2,minData1) == True:
            return True
        else:
            return False
    if verifyDays(minData1 , minData2) == True:
        if verifyDays(maxData1,minData2) == True:
            return True
        else:
            return False
    else:
        return False