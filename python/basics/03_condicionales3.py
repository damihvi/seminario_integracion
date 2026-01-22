"""
vacaciones por antiguedad
pide años de antiguedad y muestra dias de vacaciones segun 
<1=0
<3=3
<5=10
>=5=15
"""

anios_antiguedad= float(input("¿cuantos años de antiguedad tienes?: "))

if anios_antiguedad <1:
    print("corresponde a 0 dias de vacaciones ")
elif anios_antiguedad <3:
    print("corresponde a 3 dias de vacaciones ")
elif anios_antiguedad<5:
    print("corresponde a 10 dias de vacaciones")
else:
    anios_antiguedad >=5 
    print("corresponde a 15 dias de vacaciones")