"""
vacaciones por antiguedad
pide años de antiguedad y muestra dias de vacaciones segun
<1=0
<3=3
<5=15=0
>=5=15
"""

años_antiguedad = int(input("ingrese años de antiguedad: "))

if años_antiguedad < 1:
    print("0 dias de vacaiones")
elif años_antiguedad < 3:
    print("3 dias de vacaciones")
elif años_antiguedad <5:
    print("10 dias de vacaciones")
else:
    años_antiguedad >= 5
    print("15 dias de vacaciones")
    