usuarios1 = [["aa", 4], ["aa", 3], ["asda", 1]]


# nombres = []
# for usuario in usuarios1:
#     nombres.append(usuario[0])
# print(nombres)

# map
# nombres = [expresion que se va aplicar for item in items]
# para tomar una lista y obtener, trasnformar y realizar varias cosas en la lista
# para obtener el nombre de cada lista
nombres = [usuario[0] for usuario in usuarios1]
print(nombres)
# filter
# nombres = [expresion que se va aplicar for item in items comprobacion o expresion ]

# para obtener lista con una comprobacion o filtro, ejemplo es que el index sea mayor a 2
nombres = [usuario for usuario in usuarios1 if usuario[1] > 2]
print(nombres)
# se puede usar las dos formas al mismo tiempo
nombres = [usuario[0] for usuario in usuarios1 if usuario[1] > 2]
print(nombres)

# map(lambda nombre de variable donde se va a guardar: elemento que va tomar de la lista dada, lista que se va realizar las operaciones)
nombres = list(map(lambda usuario: usuario[0], usuarios1))
print(nombres)
# filter(lambda nombre de variable donde se va a guardar: elemento que va tomar de la lista dada y comprobacion, lista que se va realizar las operaciones)
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios1))
print(menosUsuarios)
