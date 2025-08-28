import Usefull

def CPF():
    while True:
        cpf = input("Confirme o CPF do hóspede: ")
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