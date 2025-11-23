"""
Sistema de verificación de conductor de transporte público
Pide edad, años de experiencia y si tiene licencia profesional
Un conductor es apto si tiene >=21 años y (experiencia>=2 años o licencia profesional)
Muestra APTO o NO APTO para conducir transporte público
"""

edad = int(input("Edad del conductor: "))
exp = float(input("Años de experiencia conduciendo: "))
licencia = input("¿Tiene licencia profesional? s/n: ").strip().lower() == 's'

if edad >= 21 and (exp >= 2 or licencia):
    print("APTO para conducir transporte público")
else:
    print("NO APTO para conducir transporte público")
