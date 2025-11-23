"""
pide el numero de empleados y luego el sueldo de cada uno
suma y muestra la nomina total
"""

numero_empleados = int(input("numero de empleados"))
nomina_total = 0
for i in range(numero_empleados):
    sueldo = float(input(f"sueldo empleado {i+1}: "))
    nomina_total += sueldo
print(f"nomina total: {nomina_total}")