"""
sistema que pida pago por hora y horas trabajadas. las primeras 40 horas son normales
las extra se pagan al 150%
calcula y muestra el total semanal
"""
pago_hora = float(input("pago por hora: "))
horas_trabajadas = float(input("horas trabajadas: "))
if horas_trabajadas <= 40:
    total = pago_hora * horas_trabajadas
else:
    horas_extra = horas_trabajadas - 40
    total = (pago_hora * 40) + (pago_hora * 1.5 * horas_extra)
print("total semanal: ", total)