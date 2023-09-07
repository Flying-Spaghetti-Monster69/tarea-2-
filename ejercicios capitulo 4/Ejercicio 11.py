x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))
z = int(input("Ingrese el tercer número: "))

mayor = x # Inicializamos la variable x como el número mayor

if y > mayor:
    mayor = y  # Compara x y y
if z > mayor:
    mayor = z  # Compara x y z

print("El número mayor es:", mayor)