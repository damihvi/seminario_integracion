"""
Sistema para determinar la ruta con mayor recaudación
Pide número de rutas de bus
Para cada ruta solicita nombre y recaudación diaria
Determina cuál tiene la mayor recaudación y la muestra
"""

num_rutas = int(input("Ingrese el número de rutas: "))
mayor_recaudacion = 0
ruta_mayor = ""

for i in range(num_rutas):
    nombre_ruta = input(f"Ingrese el nombre de la ruta {i+1}: ")
    recaudacion = float(input(f"Ingrese la recaudación de {nombre_ruta}: $"))
    
    if recaudacion > mayor_recaudacion:
        mayor_recaudacion = recaudacion
        ruta_mayor = nombre_ruta

print(f"\nLa ruta con mayor recaudación es '{ruta_mayor}' con ${mayor_recaudacion:.2f}")
