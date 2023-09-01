departamentos = []
for x in range(1,4):
    departamentos.append(float(input("ingrese el salario del departamento " + str(x) + ": ")))

salarioVendedores = float(input("ingrese el salario de los vendedores: "))

totalVentas = sum(departamentos)
porcentajeVentas = totalVentas * 0.33
salarios = []

for x in range(0,len(departamentos)):
    if departamentos[x]>porcentajeVentas:
        salarios.append(salarioVendedores + (0.2*salarioVendedores))
    else:
        salarios.append(salarioVendedores)

print("SALARIO VENDEDORES DEPTO. 1:", salarios[0], "\nSALARIO VENDEDORES DEPTO. 2:", salarios[1], "\nSALARIO VENDEDORES DEPtO. 3:", salarios[2])