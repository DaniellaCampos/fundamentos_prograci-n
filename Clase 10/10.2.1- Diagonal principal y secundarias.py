def diagonales_matriz():
    n = int(input().strip())
    matriz = []
    for _ in range(n):
        fila = list(map(int, input().split(',')))
        matriz.append(fila)
    
    principal = [matriz[i][i] for i in range(n)]
    secundaria = [matriz[i][n-1-i] for i in range(n)]
    
    print(principal)
    print(secundaria)
     
diagonales_matriz()