#      Caso de Estudio: Consumo Energético

import numpy as np

consumo =  np.array([
    [12.5,13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])  

print("Dimensiones: ", consumo.ndim)
print("Forma: ", consumo.shape)
print("Tipos de datos: ", consumo.dtype)
print("Consumo primer hogar: ", consumo[0])
print("Consumo el miércoles (día 3): ", consumo[:,2])

#Promedio de consumo por hogar
promedio_por_hogar = np.mean(consumo, axis = 1)
#Promedio de consumo diario de todos los hogares
promedio_por_dia = np.mean(consumo, axis = 0)
#suma total de consumo en la semana de los 10 hogares
total_consumo = np.sum(consumo)

print(promedio_por_hogar)
print(promedio_por_dia)
print(total_consumo)

#Maximo por hogares
maximos = np.max(consumo, axis= 1)

#Minimo por dia
minimos = np.min(consumo, axis= 0)

#Desviacion estandar global
desviacion = np.std(consumo)

#Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)
#Indice del hogar con mayor consumo
hogar_mayor_consumo = np.argmax(consumo_total_hogar)
#Indice del hogar con menor consumo
hogar_mas_eficiente = np.argmin(consumo_total_hogar)

print(consumo_total_hogar)
print(hogar_mayor_consumo)
print(hogar_mas_eficiente)


#    Filtrar los hogares de Alto Consumo

#suma por hogar(semana)
consum_total_hogar = np.sum(consumo, axis=1)
print(f'Consumo total de cada hogar durante la semana:{consumo_total_hogar}')

#Compara cada hogar con un valor mayor a 100
altos = consumo_total_hogar > 100
#Filtrando hogares que cumplen la condicion:
consumo_mayor_100 = np.where(altos)[0]

print(f'ids de hogares con consumo mayor a 100:{consumo_mayor_100}')

#Aplicando normalizacion MinMax al conjunto de datos
consumo_normalizado = (consumo - consumo.min()) / (consumo.max()-consumo.min())
#Resultado
print(consumo_normalizado)

#                Cuestionario de Trabajo

#Instruciones:
#Responde cada pregunta escribiendo el código necesario para obtener la respuesta.
#Agrega también comentarios o respuestas escritas cuando se solicite explicación.
#No borres las secciones anteriores del archivo python desarrollado para esta guía de trabajo, simplemente agrega tus respuestas al final.
#Puedes auxiliarte de tu herramienta IA preferida, pero recuerda las buenas prácticas para su uso. Somos responsables de comprender el resultado.

#Cuestionario:
#1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
consumo_hogar5_viernes = consumo[5, 4]
print("1. Consumo hogar 5 viernes:", consumo_hogar5_viernes)

#2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
ultimos_hogares_domingo = consumo[-3:, 6]  # Últimas 3 filas, columna 6
print("\n2. Consumo últimos 3 hogares domingo:", ultimos_hogares_domingo)

#3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
consumo_findes = consumo[:, [5, 6]]        # Todas las filas, columnas 5 y 6
promedio_findes = np.mean(consumo_findes)
print("\n3. Promedio fines de semana:", round(promedio_findes, 2))

#4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
desviaciones = np.std(consumo, axis=0)     # Desviación por día (columnas)
dia_max_desv = np.argmax(desviaciones)     # Índice del día con máxima desviación
print("\n4. Día con mayor desviación estándar:", dia_max_desv)
print("   Esto indica que el consumo entre hogares varía más en este día")

#5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
consumo_total = np.sum(consumo, axis=1)  # Suma por filas (hogares)
indices_menores = np.argsort(consumo_total)[:3]  # Índices de los 3 menores

print("\n5. Hogares con menor consumo total:")
print("   Índices:", indices_menores)
print("   Valores:", consumo_total[indices_menores])

#6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
hogar3 = consumo[2]  # Hogar 3 está en índice 2
nuevo_total = np.sum(hogar3 * 1.1)  # Aumento del 10% y suma

print("\n6. Nuevo consumo semanal del hogar 3:", round(nuevo_total, 1))