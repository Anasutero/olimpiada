def verificacao_numero(E, D):
    if E > D:
        soma = E + D
        return soma
    else:
        operacao = 2 * (D - E) 
        return operacao

def calcular_aritmetica(E, D):
    calculo = (D + E) / 2
    return calculo

def verificar_e_calcular(E, D):
    resultado_verificacao = verificacao_numero(E, D)
    resultado_calculo = calcular_aritmetica(E, D)
    return resultado_verificacao, resultado_calculo

E = int(input(""))
D = int(input(""))

resultado_verificacao, resultado_calculo = verificar_e_calcular(E, D)

print(resultado_verificacao)

