import math

print("Calculo de utilidades")
pb = float(input("Ingrese el precio de suscripción base: "))
pp = pb * 1.5
ur = int(input("Ingrese el número de usuarios regulares: "))
up = int(input("Ingrese el número de usuarios premium: "))
GT = float(input("Ingrese los gatos totales "))

utilidades = round((up * pp) + (ur * pb) - GT, 2)
print(f"Las utilidades son de: {utilidades} ")