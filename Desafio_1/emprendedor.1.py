import math

print("Calculo de utilidades")
p = float(input("Ingrese el precio de suscripción: "))
ur = int(input("Ingrese el número de usuarios: "))
GT = float(input("Ingrese los gatos totales "))

utilidades = round((p * ur) - GT, 2)
print(f"Las utilidades son de: {utilidades} ")