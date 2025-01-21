numeros = [2, 4, 5, 6, 4, 44]
numeros.sort()  # sort es para ordenar lista
# sort(reverse=True)es para ordenar de manera acedente de mayor a menor
# sorted() tambien es para ordenar listas
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

usuarios = [[4, "aa"], [2, "aa"], [4, "asda"]]
usuarios.sort()  # sort es para ordenar lista
print(usuarios)

usuarios1 = [["aa", 4], ["aa", 3], ["asda", 1]]

# funcion para obtener el index de cada lista


def ordena(elemento):
    return elemento[1]


# key es para dar que elemento va tomar para realizar el orden
# lambda paramentros:valorRetorno para hacer un funcion anonima si solo se  va usar esta funcion una vez esta bien pero si se usa mas en otros apartados se recomienda usar funciones normales
usuarios1.sort(key=lambda el: el[1])
print(usuarios1)
