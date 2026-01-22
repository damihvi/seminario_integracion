"""
Sistema de Bonificación por Desempeño - Instituto Educativo
Evalúa el desempeño académico (1-5) y otorga bonificación en la pensión
Desempeño 5: 15% descuento
Desempeño 4: 10% descuento
Desempeño 3: 5% descuento
Desempeño 2: 2% descuento
Desempeño 1: Sin descuento
"""

print("=== BONIFICACIÓN POR DESEMPEÑO ACADÉMICO ===")
nombre = input("Nombre del estudiante: ")
pension = float(input("Pensión mensual actual (S/.): "))
desempeño = int(input("Calificación de desempeño (1-5): "))

if desempeño > 4:
    descuento = pension * 0.15
elif desempeño > 3:
    descuento = pension * 0.10
elif desempeño > 2:
    descuento = pension * 0.05
elif desempeño > 1:
    descuento = pension * 0.02
else:
    descuento = 0

pension_final = pension - descuento

print(f"\n--- RESUMEN DE BONIFICACIÓN ---")
print(f"Estudiante: {nombre}")
print(f"Pensión original: S/. {pension:.2f}")
print(f"Descuento por desempeño: S/. {descuento:.2f}")
print(f"Pensión final: S/. {pension_final:.2f}")