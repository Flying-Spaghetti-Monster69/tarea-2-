A = int(input("A > "))
B = int(input("B > "))
C = int(input("C > "))

D = B**2 - 4*A*C

if D < 0:
  print("No hay solucion en R")
elif D == 0:
  print("Soluciones iguales x1,2 =",-B/2*A)
else:
  print("x1 = ", (-B + D**1/2)/2*A)
  print("x2 = ", (-B - D**1/2)/2*A)