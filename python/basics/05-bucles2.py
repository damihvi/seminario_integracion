"""
pide el numero de empleados y luego el sueldo de cada uno 
suma y muestra la nomima total 
"""


empleados=int (input("¿cuantos empreados tienes? "))
total = 0 
for i  in range(empleados):
    sueldo =float(input(f" sueldo {i+1}"))
    total+=sueldo
print (f"nomina total:{total}")