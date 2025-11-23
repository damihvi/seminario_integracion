"""
pide salario y clasificar el cargo
<1000 junior
1000-2000 semi senior
>2000 senior
"""
salario = int(input("ingrese su salario: "))

if salario < 1000:
    print("junior")
elif salario <= 2000:
    print("semi senior")
else:
    print("senior")

    