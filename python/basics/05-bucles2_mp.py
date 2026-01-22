"""
Sistema de Cálculo de Pensiones - Instituto Educativo
Ingresa el número de estudiantes y la pensión de cada uno
Calcula y muestra el ingreso total por pensiones
"""

print("=== CÁLCULO DE INGRESOS POR PENSIONES ===")
estudiantes = int(input("¿Cuántos estudiantes tiene el aula?: "))
total_pensiones = 0

for i in range(estudiantes):
    print(f"\nEstudiante {i+1}:")
    nombre = input("  Nombre: ")
    pension = float(input("  Pensión mensual (S/.): "))
    total_pensiones += pension

print(f"\n--- RESUMEN FINANCIERO ---")
print(f"Total de estudiantes: {estudiantes}")
print(f"Ingreso total por pensiones: S/. {total_pensiones:.2f}")
print(f"Pensión promedio: S/. {total_pensiones/estudiantes:.2f}")