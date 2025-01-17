mascotas = ["aaa", "bbb", "ccc"]
# para agregar elemento en la lista con insert(lugar donde se agregara,valor)
mascotas.insert(1, "aaas")
mascotas.append("aasdd")  # para agregar elemento al final de la lista


# para eliminar el elemento remove("valor del elemento que va eliminar") solo elimina un elemento ala vez y si hay mas no los elimina
mascotas.remove("aaas")
mascotas.pop(1)  # para eliminar el ultimo elemento de la lista y pop(si ser coloca el numero se elimina el valor desde la derecha hasta llegar el numero de indece )
# para eliminar elementos en un arreglo, del lista[numero de index del elemento]
del mascotas[0]
# clear es para limpiar lista, digamos que elimina todos los elementos de la lista
mascotas.clear()
print(mascotas)
