"""
Sistema de Clasificación de Becas - Instituto Educativo
Clasifica el tipo de beca según ingreso familiar
< S/. 1500: Beca Completa (100%)
S/. 1500-3000: Beca Parcial (50%)
> S/. 3000: Beca por Mérito (según rendimiento)
"""

print("=== CLASIFICACIÓN DE BECAS ===")
nombre = input("Nombre del postulante: ")
ingreso_familiar = float(input("Ingreso familiar mensual (S/.): "))

if ingreso_familiar < 1500:
    print(f"\n{nombre} califica para: BECA COMPLETA (100%)")
    print("Cubre pensión, matrícula y materiales")
elif ingreso_familiar <= 3000:
    print(f"\n{nombre} califica para: BECA PARCIAL (50%)")
    print("Cubre el 50% de pensión y matrícula")
else:
    print(f"\n{nombre} califica para: BECA POR MÉRITO")
    print("Requiere promedio mayor a 16 para aplicar")