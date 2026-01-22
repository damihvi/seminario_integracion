"""
Sistema de Registro de Asistencias - Instituto Educativo
Registra las asistencias diarias del estudiante
A = Asistió, F = Falta, T = Tardanza, J = Justificado
Calcula el total de faltas injustificadas
"""

print("=== REGISTRO DE ASISTENCIAS ===")
nombre = input("Nombre del estudiante: ")
dias = int(input("¿Cuántos días vas a registrar?: "))
faltas = 0

for i in range(dias):
    marca = input(f"Día {i+1} (A=Asistió, F=Falta, T=Tardanza, J=Justificado): ").strip().upper()
    if marca == "F":
        faltas += 1

print(f"\n--- RESUMEN DE ASISTENCIAS ---")
print(f"Estudiante: {nombre}")
print(f"Faltas injustificadas: {faltas}")
if faltas >= 3:
    print("⚠ ALERTA: Riesgo de desaprobación por inasistencias")
else:
    print("✓ Asistencia dentro del límite permitido")