nombre = input("ingrese el nombre del trabajador: ")
horasTrabajadas = float(input("ingrese el numero de horas trabajadas: "))
valorPorHora = float(input("ingrese el valor de cada hora trabajada: "))
devengo = 0

if (horasTrabajadas > 40):
    if (horasTrabajadas > 48):
        devengo = 40*valorPorHora + 8*2*valorPorHora + (horasTrabajadas - 48)*3*valorPorHora
    else:
        devengo = 40*valorPorHora+(horasTrabajadas - 40)*2*valorPorHora
else:
    devengo = horasTrabajadas*valorPorHora

print("el trabajador",nombre,"devengo: $",devengo)