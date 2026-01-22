salario = int(input("ingrese su salario"))
desempeño = int(input("ingrese desempeño"))
if desempeño > 4:
    aumento = salario * 0.15
elif desempeño > 3:
    aumento = salario * 0.10
elif desempeño > 2:
    aumento = salario * 0.05
elif desempeño > 1:
    aumento = salario * 0.02
else:
    aumento = 0

print("Su sueldo es",aumento + salario )