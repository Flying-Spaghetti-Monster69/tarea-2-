# Pedir Las Coordenadas De Dos Puntos (X1, Y1) Y (X2, Y2)
X1 = float(input("Ingrese la coordenada X del primer punto: "))
Y1 = float(input("Ingrese la coordenada Y del primer punto: "))
X2 = float(input("Ingrese la coordenada X del segundo punto: "))
Y2 = float(input("Ingrese la coordenada Y del segundo punto: "))

# Calcular Los Parámetros De La Recta (A, B, C)
A = Y2 - Y1
B = X1 - X2
C = X2 * Y1 - X1 * Y2

# Mostrar Los Parámetros De La Recta
print("Parámetros de la recta: A =", A, ", B =", B, ", C =", C)
