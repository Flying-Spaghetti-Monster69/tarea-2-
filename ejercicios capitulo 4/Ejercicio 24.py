esferas = {"esfera A":float(input("ingrese el peso de la esfera A: ")),
    "esfera B":float(input("ingrese el peso de la esfera B: ")),
    "esfera C":float(input("ingrese el peso de la esfera C: ")),
}

valores = list(esferas.values())
maximo = max(valores)
key = list(esferas.keys())

print("la",key[valores.index(maximo)],"es la de mayor peso")