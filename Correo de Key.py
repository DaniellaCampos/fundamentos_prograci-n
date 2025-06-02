#Solicita al usuario su nombre completo (asume dos nombres y dos apellidos). Luego, el programa generará, su correo con el formato:
# - primer_nombre.primer_apellido@keyinstitute.edu.sv

nombres=input('Ingrese sus nombres: ')
apellidos=input('Ingrese sus apellidos:')

lista_nombres = nombres.strip().split()
lista_apellidos = apellidos.strip().split()

primer_nombre = lista_nombres[0].lower()
primer_apellido = lista_apellidos[0].lower()

correo = primer_nombre + "." + primer_apellido + "@keyinstitute.edu.sv"

print("El correo que se debe asignar al usuario ingresado es:", correo)