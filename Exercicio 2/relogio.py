def calcular_horas(H, M, S, T):
    if not (0 <= H < 24 and 0 <= M < 60 and 0 <= S < 60 and T >= 0):
        print("Valores inválidos inseridos.")
        return

    tempo_inicial_em_segundos = H * 3600 + M * 60 + S
    novo_tempo_em_segundos = tempo_inicial_em_segundos + T


    novo_H = novo_tempo_em_segundos // 3600
    novo_M = (novo_tempo_em_segundos % 3600) // 60
    novo_S = (novo_tempo_em_segundos % 3600) % 60

    
    novo_H %= 24
    return novo_H, novo_M, novo_S

H = int(input(""))
M = int(input(""))
S = int(input(""))
T = int(input(""))

novo_horario = calcular_horas(H, M, S, T)


if novo_horario:
    print(novo_horario)
