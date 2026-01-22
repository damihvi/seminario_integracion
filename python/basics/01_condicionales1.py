"""
escribe un programa que pida edad, años de experiencia y si tiene titulo universitario.
un candidato es eslegible si tiene >= 21 años y experiencia >= 2 años o titulo
muestra elegible o no elegible """

edad = int(input("edad del candidato: "))
exp = float(input("años de experiencia: "))
tiene_titulo = input("tiene titulo universitario? s/n: ") .strip(). lower() == "si"


if (edad>=21 and (exp>=2 or tiene_titulo=="s")):
    print("Elegible")
else:
    print("No Elegible")