"""
Sistema de cálculo de recaudación total de múltiples rutas
Pide el número de rutas de bus y luego la recaudación diaria de cada una
Suma y muestra la recaudación total del sistema
"""

numero_rutas = int(input("Número de rutas de bus: "))
recaudacion_total = 0

for i in range(numero_rutas):
    recaudacion = float(input(f"Recaudación de la ruta {i+1}: $"))
    recaudacion_total += recaudacion

print(f"Recaudación total del sistema: ${recaudacion_total:.2f}")
