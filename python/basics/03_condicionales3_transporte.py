"""
Sistema de días de vacaciones para conductores según antigüedad
Pide años de antigüedad y muestra días de vacaciones según:
< 1 año = 0 días
< 3 años = 7 días
< 5 años = 14 días
>= 5 años = 21 días
"""

años_antiguedad = int(input("Ingrese años de antigüedad del conductor: "))

if años_antiguedad < 1:
    print("0 días de vacaciones")
elif años_antiguedad < 3:
    print("7 días de vacaciones")
elif años_antiguedad < 5:
    print("14 días de vacaciones")
else:
    print("21 días de vacaciones")
