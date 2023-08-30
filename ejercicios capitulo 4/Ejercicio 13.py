valorCompra = float(input("ingrese el valor de la compra: "))
colorBola = input("ingrese el color de la bola: ").upper()
costo = 0

if (colorBola == "BLANCO"):
    costo = valorCompra
elif (colorBola == "VERDE"):
    costo = valorCompra - (valorCompra*0.1)
elif (colorBola == "AMARILLO"):
    costo = valorCompra - (valorCompra*0.25)
elif (colorBola == "AZUL"):
    costo = valorCompra - (valorCompra*0.5)
else:
    costo = 0

print("el cliente debe pagar: $",costo)