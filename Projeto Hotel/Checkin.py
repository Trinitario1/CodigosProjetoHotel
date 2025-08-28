import Usefull

def Suite(suites):
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
def Name():
    return input("Digite o nome do hóspede: ")
def CPF():
    while True:
        cpf = input("Digite o CPF do novo hóspede: ")
        if len(cpf) !=14:
            print(">>>>>>CPF inválido, tente novamente<<<<<<\n")
            continue
        if Usefull.isNumber(cpf[0:3]) == True and Usefull.isNumber(cpf[4:7]) == True and Usefull.isNumber(cpf[8:11]) == True and Usefull.isNumber(cpf[12:]):
            if Usefull.validarCpf(cpf) == True:
                return cpf
            else:
                print(">>>>>>CPF inválido, tente novamente<<<<<<\n")
        else:
                print(">>>>>>CPF inválido, tente novamente<<<<<<\n")
def DayIn():
    while True:
        day =  input("Digite a data de check-in: ")
        if Usefull.validarData(day) == True:
            return day
        else:
            print(">>>>>>Data inválida inserida, tente novamente<<<<<<")
def DayOut():
    while True:
        day =  input("Digite a data prevista de check-out: ")
        if Usefull.validarData(day) == True:
            return day
        else:
            print(">>>>>>Data inválida inserida, tente novamente<<<<<<")