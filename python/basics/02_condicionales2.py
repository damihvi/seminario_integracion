"""
sistema que pida pago por hora y horas trabajadas.
las primeras 40h son normales , las extra se pagan al 150%
calcula y muetra el total semanal
"""

pago_horas = float(input("pago por hora: "))
horas_trabajadas = float(input("horas trabajadas: "))

if horas_trabajadas <= 40:
    calculo= horas_trabajadas * pago_horas
else:
    hora_extra = horas_trabajadas - 40
    calculo = (pago_horas*40)+(pago_horas*1.5 * hora_extra )

print("total semanal:", calculo )