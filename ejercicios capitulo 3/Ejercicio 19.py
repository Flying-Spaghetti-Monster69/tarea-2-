import math

# Pedir El Valor Del Lado Del Triángulo Equilátero
lado = float(input("Ingrese el valor del lado del triángulo equilátero: "))

# Calcular El Perímetro Del Triángulo
perimetro = 3 * lado

# Calcular La Altura Del Triángulo
altura = (math.sqrt(3) / 2) * lado

# Calcular El Área Del Triángulo
area = (math.sqrt(3) / 4) * lado**2

# Mostrar Los Resultados
print("Perímetro del triángulo:", perimetro)
print("Altura del triángulo:", altura)
print("Área del triángulo:", area)
