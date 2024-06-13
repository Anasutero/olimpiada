def calculo_nota_corte(N, K, notas):
    # Validar se os valores de N e K estão dentro dos limites
    if not (1 <= int(K) <= int(N) <= 500):
        print("Valores inválidos para N e K.")
        return

    K = int(K)
    N = int(N)

    # Converter as notas para inteiros e verificar se estão dentro do intervalo permitido
    notas = [int(nota) for nota in notas.split()]
    if not all(1 <= nota <= 100 for nota in notas):
        print("Notas inválidas inseridas.")
        return

    # Ordenar as notas em ordem decrescente
    notas.sort(reverse=True)
    
    # Calcular a nota de corte
    nota_corte = notas[K - 1]
    return nota_corte


# Entradas
N = input("")
K = input("")
notas_participantes = input("")

# Calcular a nota de corte
nota_de_corte = calculo_nota_corte(N, K, notas_participantes)

# Imprimir a nota de corte se for válida
if nota_de_corte is not None:
    print(nota_de_corte)


