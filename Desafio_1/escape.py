import math

print("Velocidad de Escape")
g = float(input("Ingrese la corresponde a la constante gravitacional en [m/s2]: "))
r = float(input("Ingrese el radio del planeta en [km]: "))

Ve = round(math.sqrt(2 * g *r *1000),1)
print(f"La velocidad de Escape es de: {Ve}[m/s]")