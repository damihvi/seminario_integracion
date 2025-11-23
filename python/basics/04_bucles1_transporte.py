"""
Sistema de registro de puntualidad de buses
Pide cuántos días registrarás
Para cada día ingresa: T (tarde), P (puntual), A (ausencia)
Cuenta y muestra el total de retrasos
"""

dias = int(input("¿Cuántos días vas a registrar? "))
retrasos = 0

for i in range(dias):
    estado = input(f"Día {i+1} (T=tarde, P=puntual, A=ausencia): ").strip().upper()
    if estado == "T":
        retrasos += 1

print(f"Total de retrasos en el período: {retrasos}")
