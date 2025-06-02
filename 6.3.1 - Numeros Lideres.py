def numeros_lideres(lista):
    lideres = []
    mayor = -1
    for num in reversed(lista):
        if num > mayor:
            lideres.append(num)
            mayor = num
    lideres.reverse()
    print(*lideres)


entrada = [1, 65, 1, 16, 5, 6, 8, 6, 4]
numeros_lideres(entrada)


