def es_bisiesto(año):
    if not (1 <= año <= 10**7):
        return "No bisiesto"
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return "Bisiesto"
    else:
        return "No bisiesto"
año = int(input())
print(es_bisiesto(año))