from random import randint

secreto = randint(1, 100)
respuesta = 0

while respuesta != secreto:
    respuesta = int(input("Adivina el número secreto: "))

    if respuesta < secreto:
        print("El número secreto es mayor")
    elif respuesta > secreto:
        print("El número secreto es menor")

print("¡Felicidades! Has adivinado el número secreto")
