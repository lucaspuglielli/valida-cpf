#Versão fracionada do codigo para facilitar compreensao

def verifica_cpf(cpf):
    numeros = retorna_numeros(cpf)
    if len(numeros) == 11:
        if numeros[-2:] == retorna_comparativo(numeros):
            print("CPF válido")
        else:
            print("CPF inválido")
    else:
        print("Formato de CPF inválido")

def retorna_numeros(cpf):
    numeros_cpf = []
    for numero in list(str(cpf)):
        if numero.isnumeric():
            numeros_cpf.append(numero)
    numeros_cpf = [int(x) for x in numeros_cpf]
    return numeros_cpf

def retorna_comparativo(numeros):
    comparativo = []
    passo = 1
    while passo < 3:
        resto = retorna_resto(numeros, 3 - passo)
        resultado = 11 - resto
        passo += 1
        if resultado < 10:
            comparativo.append(resultado)
        else:
            comparativo.append(0)
    return comparativo

def retorna_resto(numeros, qtd):
    index = 0
    regressivo = 12 - qtd
    resultado = 0
    for numero in numeros:
        if index < len(numeros) - qtd:
            resultado = resultado + numero * regressivo
            regressivo -= 1
            index += 1
    return resultado % 11

verifica_cpf(input("Informe seu cpf:"))