"""
pide cuantos dias registraras 
para cada lista ingresa  
"""

dias=int (input("¿cuantos dias vas a cargar "))
tardes = 0 
for i  in range(dias):
    marca =input(f"dia {i+1}(T= tarde, O=ok, P=permiso)").strip().upper()
    if marca == "T":
        tardes +1
print (f"Tardanzas totales:{tardes}")