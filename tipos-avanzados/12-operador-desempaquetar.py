lista = [1, 2, 3, 4]
print(lista)
print(*lista)  # para mostrar los elementos en una solo linea y sin coma


lista2 = [1, 2, 3, 4]

# mostrar listas desempaquetadas y tambien agregar string
combinada = ["hola", *lista, "shinano", *lista2]
print(combinada)

punto1 = {"x": 1}
punto2 = {"y": 12}

# desempaquetar diccionarios o arreglos asociados se usa **, pero si hay un nombre de elemento igual entre los diccionarios tomara el nombre de elemento y valor de la segundo dicinario
nuevoPunto = {**punto1, "lala": 2, **punto2, "z": "mundo"}
print(nuevoPunto)
