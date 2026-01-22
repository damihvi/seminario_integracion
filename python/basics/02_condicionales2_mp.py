"""
Sistema de Cálculo de Pensión - Instituto Educativo
Calcula la pensión mensual considerando créditos académicos
Primeros 15 créditos: tarifa normal
Créditos adicionales: 120% de la tarifa
"""

print("=== CÁLCULO DE PENSIÓN MENSUAL ===")
pago_credito = float(input("Costo por crédito académico (S/.): "))
creditos_matriculados = int(input("Créditos matriculados: "))

if creditos_matriculados <= 15:
    pension = creditos_matriculados * pago_credito
else:
    creditos_extra = creditos_matriculados - 15
    pension = (pago_credito * 15) + (pago_credito * 1.2 * creditos_extra)

print(f"\n--- RESUMEN DE PENSIÓN ---")
print(f"Total de créditos: {creditos_matriculados}")
print(f"Pensión mensual: S/. {pension:.2f}")