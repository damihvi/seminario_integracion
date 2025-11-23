"""
pide cuantos dias registraras
para cada dia ingresa t(tarde) o o(ok) p(permiso)
cuenta y muestra tardanzas totales
"""

dias = int(input("cuantos dias vas a cargar"))
tardes = 0

for i in range(dias):
    marca = input(f"dia {i+1} (t=tarde, o=ok, p=permiso)").strip().upper()
    if marca=="t":
        tardes+=1
print(f"tardanzas totales: {tardes}")