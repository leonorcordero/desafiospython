import math

print("Calculo de utilidades")

p = float(input("Ingrese el precio de suscripción: "))
ur = int(input("Ingrese el número de usuarios: "))
GT = float(input("Ingrese los gatos totales "))
UAA = float(input("Ingrese las utilidades del año anterior (debe ser distinto de cero): "))

utilidades = (p * ur) - GT

try:
    razon = round(utilidades / UAA, 2)
    print(f"La razon de las utilidades es: {razon} ")

except:
    print("Error: No se puede dividir por cero.")


