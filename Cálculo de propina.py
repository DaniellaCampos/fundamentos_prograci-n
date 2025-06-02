#Pide al usuario el total de una cuenta y el porcentaje de propina (por ejemplo, 10%, 15%, 20%). Calcula y muestra en pantalla el total a pagar.
total_cuenta = float(input("Ingrese el total de la cuenta: $"))
porcentaje_propina = float(input("Ingrese el porcentaje de propina (por ejemplo, 10, 15, 20): "))

propina = total_cuenta * (porcentaje_propina / 100)
total_con_propina = total_cuenta + propina

print(f"Total de la cuenta: ${total_cuenta}")
print(f"Propina: ${propina}")
print(f"Total de la cuenta con propina ({int(porcentaje_propina)}%): ${total_con_propina}")

