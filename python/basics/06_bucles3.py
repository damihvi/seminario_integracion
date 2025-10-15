"""
pide numero de empleados
cada empleado solicita nombre y salario
determina quien tiene el mayor salario y muestralo
"""

num_empleados = int(input("ingrese los empleados"))
mayor_salario = 0
for i in range(num_empleados):
    nombre = input(f"ingrese el nombre del empleado {i+1}: ")
    salario = float(input(f"ingrese el salario de {nombre}: "))
    if salario > mayor_salario:
        mayor_salario = salario
        empleado_mayor_salario = nombre 
print(f"el empleado con mayor salario es {empleado_mayor_salario} con un salario de {mayor_salario}")

