esferas = {"esfera A":float(input("ingrese el peso de la esfera A: ")),
    "esfera B":float(input("ingrese el peso de la esfera B: ")),
    "esfera C":float(input("ingrese el peso de la esfera C: ")),
    "esfera D":float(input("ingrese el peso de la esfera D: "))
}

valores = list(esferas.values())
maximo = max(valores)
key = list(esferas.keys())

if valores.count(maximo) == 3:
    print("la",key[valores.index(min(valores))],"es la diferente y es de menor peso")
else:
    print("la",key[valores.index(maximo)],"es la diferente y es de mayor peso")