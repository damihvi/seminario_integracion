"""
Programa de admisión para instituto educativo.
Solicita edad, promedio de notas y si tiene certificado de bachillerato.
Un estudiante es admitido si tiene >= 16 años y promedio >= 14 o tiene certificado de bachillerato.
Muestra "Admitido" o "No Admitido"
"""

edad = int(input("Edad del postulante: "))
promedio = float(input("Promedio de notas (escala 0-20): "))
tiene_certificado = input("¿Tiene certificado de bachillerato? (s/n): ").strip().lower() == "s"


if edad >= 16 and (promedio >= 14 or tiene_certificado):
    print("Admitido")
else:
    print("No Admitido")