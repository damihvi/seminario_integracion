"""
Sistema de cálculo de salario semanal para conductor de bus
Pide tarifa por hora y horas trabajadas. Las primeras 40 horas son normales
Las horas extra se pagan al 150%
Calcula y muestra el salario total semanal
"""

tarifa_hora = float(input("Tarifa por hora del conductor: "))
horas_trabajadas = float(input("Horas trabajadas en la semana: "))

if horas_trabajadas <= 40:
    total = tarifa_hora * horas_trabajadas
else:
    horas_extra = horas_trabajadas - 40
    total = (tarifa_hora * 40) + (tarifa_hora * 1.5 * horas_extra)

print(f"Salario semanal total: ${total:.2f}")
