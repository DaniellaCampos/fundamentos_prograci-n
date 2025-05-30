numeros = input("ingrese la lista, cada número separado por espacios: ")

lista = numeros.split(" ")

resultado = ""

for x in lista:
    count = 0
    for y in lista:
        if x == y:
            count +=1

    if (count >1):
        for h in range (1, count):
            lista.remove(x)
        
for n in lista:
    resultado += n +" "

print (resultado)