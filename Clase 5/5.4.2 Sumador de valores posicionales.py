numero = input()
while len(numero) > 1:
    suma = 0
    for digito in numero:
        suma = suma + int(digito)
    numero = str(suma)

print("El número reducido es:", numero)