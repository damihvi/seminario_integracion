"""
Sistema de Asignación de Nivel Académico - Instituto Educativo
Asigna el nivel de aula según el promedio del estudiante
Promedio < 11: Aula de Reforzamiento
Promedio < 14: Aula Regular
Promedio < 17: Aula Avanzada
Promedio >= 17: Aula de Excelencia
"""

print("=== ASIGNACIÓN DE NIVEL ACADÉMICO ===")
nombre = input("Nombre del estudiante: ")
promedio = float(input("Promedio del último ciclo (0-20): "))

if promedio < 11:
    print(f"\n{nombre} → Aula de REFORZAMIENTO")
    print("Recibirá apoyo adicional y tutorías")
elif promedio < 14:
    print(f"\n{nombre} → Aula REGULAR")
    print("Programa estándar de estudios")
elif promedio < 17:
    print(f"\n{nombre} → Aula AVANZADA")
    print("Programa con contenido complementario")
else:
    print(f"\n{nombre} → Aula de EXCELENCIA")
    print("Programa intensivo con retos académicos")