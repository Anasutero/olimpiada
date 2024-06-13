def imprimir_matriz(matriz):
    for linha in matriz:
        print(''.join(map(str, linha)))

def mudar_grupos_vivos(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    matriz_resultante = [[0] * colunas for _ in range(linhas)]

    for i in range(linhas):
        for j in range(colunas):
            vizinhos = [
                (i - 1, j),
                (i + 1, j),
                (i, j - 1),
                (i, j + 1),
                (i - 1, j - 1),
                (i - 1, j + 1),
                (i + 1, j - 1),
                (i + 1, j + 1)
            ]

            vizinhos_vivos = 0
            for x, y in vizinhos:
                if 0 <= x < linhas and 0 <= y < colunas:
                    if matriz[x][y] == 1:
                        vizinhos_vivos += 1

            if matriz[i][j] == 1:
                if vizinhos_vivos < 2 or vizinhos_vivos > 3:
                    matriz_resultante[i][j] = 0
                else:
                    matriz_resultante[i][j] = 1
            else:
                if vizinhos_vivos == 3:
                    matriz_resultante[i][j] = 1

    return matriz_resultante

if __name__ == "__main__":
    N, Q = map(int, input("").split())
    
    matriz = []
    print("Insira a matriz:")
    for _ in range(N):
        linha = list(map(int, input().strip()))
        matriz.append(linha)

    matriz_resultante = mudar_grupos_vivos(matriz)

    print("")
    imprimir_matriz(matriz_resultante)
