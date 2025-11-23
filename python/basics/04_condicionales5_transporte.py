"""
Sistema de bonificación por calificación del conductor
Pide salario base y calificación del conductor (1-5 estrellas)
Si la calificación es:
> 4 estrellas = 20% de bonificación
> 3 estrellas = 12% de bonificación
> 2 estrellas = 5% de bonificación
> 1 estrella = 2% de bonificación
<= 1 estrella = Sin bonificación
"""

salario_base = float(input("Ingrese el salario base del conductor: $"))
calificacion = int(input("Ingrese la calificación del conductor (1-5): "))

if calificacion > 4:
    bonificacion = salario_base * 0.20
elif calificacion > 3:
    bonificacion = salario_base * 0.12
elif calificacion > 2:
    bonificacion = salario_base * 0.05
elif calificacion > 1:
    bonificacion = salario_base * 0.02
else:
    bonificacion = 0

salario_final = salario_base + bonificacion
print(f"Salario base: ${salario_base:.2f}")
print(f"Bonificación: ${bonificacion:.2f}")
print(f"Salario final: ${salario_final:.2f}")
