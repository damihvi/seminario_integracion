"""
Sistema de clasificación de rutas por recaudación diaria
Pide la recaudación diaria de una ruta y clasifica según:
< $5000 = Ruta de baja demanda
$5000 - $15000 = Ruta de demanda media
> $15000 = Ruta de alta demanda
"""

recaudacion = float(input("Ingrese la recaudación diaria de la ruta: $"))

if recaudacion < 5000:
    print("Ruta de baja demanda")
elif recaudacion <= 15000:
    print("Ruta de demanda media")
else:
    print("Ruta de alta demanda")
