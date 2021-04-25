class CPF:
    def __init__(self, cpf):
        numeros = []
        for numero1 in list(str(cpf)):
            if numero1.isnumeric():
                numeros.append(numero1)
        numeros = [int(x) for x in numeros]
        if len(numeros) == 11:
            comparativo = []
            passo = 1
            while passo < 3:
                index = 0
                regressivo = 9 + passo
                resto = 0
                for numero2 in numeros:
                    if index < len(numeros) - (3 - passo):
                        resto = resto + numero2 * regressivo
                        regressivo -= 1
                        index += 1
                resto = resto % 11
                resultado = 11 - resto
                passo += 1
                if resultado < 10:
                    comparativo.append(resultado)
                else:
                    comparativo.append(0)
            if numeros[-2:] == comparativo:
                self.retorno = "CPF válido"
            else:
                self.retorno = "CPF inválido"
        else:
            self.retorno = "Formato de CPF inválido"