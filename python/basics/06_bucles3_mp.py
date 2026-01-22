"""
Sistema de Mejor Promedio - Instituto Educativo
Ingresa los datos de estudiantes y encuentra al de mejor promedio
"""

print("=== BÚSQUEDA DEL MEJOR ESTUDIANTE ===")
numero_estudiantes = int(input("¿Cuántos estudiantes evaluarás?: "))
mejor_promedio = 0
mejor_estudiante = ""

for i in range(numero_estudiantes):
    print(f"\nEstudiante {i+1}:")
    nombre = input("  Nombre: ")
    promedio = float(input("  Promedio (0-20): "))
    
    if promedio > mejor_promedio:
        mejor_promedio = promedio
        mejor_estudiante = nombre

print(f"\n--- RESULTADO ---")
print(f"Mejor estudiante: {mejor_estudiante}")
print(f"Promedio más alto: {mejor_promedio:.2f}")