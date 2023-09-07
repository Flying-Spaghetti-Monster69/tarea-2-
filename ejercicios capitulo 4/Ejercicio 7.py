# Pedir Al Usuario Que Ingrese Los Valores De A Y B
A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))

# Comparar A Y B Y Mostrar Un Mensaje En Consecuencia
if A > B:
    mensaje = "A es mayor que B"
elif A < B:
   mensaje = "A es menor que B"
else:
   mensaje = "A es igual a B"

# Mostrar El Mensaje
print(mensaje)
