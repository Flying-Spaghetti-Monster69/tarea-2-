# Pedir Información Del Empleado
codigo_empleado = input("Ingrese el código del empleado: ")
nombres = input("Ingrese los nombres del empleado: ")   
horas_trabajadas = float(input("Ingrese el número de horas trabajadas al mes: "))
valor_hora = float(input("Ingrese el valor de la hora trabajada: "))
porcentaje_retencion = float(input("Ingrese el porcentaje de retención en la fuente: "))

# Calcular Salario Bruto
salario_bruto = horas_trabajadas * valor_hora

# Calcular Retención En La Fuente
retencion_fuente = salario_bruto * (porcentaje_retencion / 100)

# Calcular Salario Neto
salario_neto = salario_bruto - retencion_fuente

# Mostrar Los Resultados
print("Código del empleado:", codigo_empleado)
print("Nombres del empleado:", nombres)
print("Salario bruto:", salario_bruto)
print("Salario neto:", salario_neto)
