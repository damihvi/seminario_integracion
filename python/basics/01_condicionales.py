"""
escribe un programa que pida edad, años de experiencia y si tiene
titulo universitario
un candidato es elegible si tiene >=21 años y expericencia>=2 años o titulo
muestra elegible o no elegible
"""

edad = int(input("edad del candidato: "))
exp = float(input("años de experiencia: "))
titulo = input("tiene titulo universitario? s/n: ").strip().lower() == 's'
if edad >= 21 and (exp >= 2 or titulo):
    print("elegible")
else:
    print("no elegible")


