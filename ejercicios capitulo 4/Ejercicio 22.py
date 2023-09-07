nombre = input("Nombre > ")
salario = int(input("Salario por Hora > "))
horas = int(input("Horas Trabajadas por Mes > "))

if salario*horas > 450000:
  print(nombre, salario*horas)
else:
  print(nombre)