"""
pide salario y clasificar el cargo
<1000 junior
1000-2000 semi senior
>2000 senior
"""

pide_salario=int (input("¿cuantos es tu salario "))

if pide_salario <1000:
    print("salario Junior ")
elif pide_salario <=2000:
    print("salario semi senior")

else:
    print("salario senior")