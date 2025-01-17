mascotas = ["shinano", "yamato", "aa", "ss"]
print(mascotas[0])
mascotas[0] = "yamato"  # para cambiar el valor del dato en la lista
print(mascotas)
# para no mostrar un elemento y es desde izquierda a derecha
print(mascotas[-1])
print(mascotas[2:])
print(mascotas[1:2:2])

numeros = list(range(21))
print(numeros[::2])#para mostrar los numeros pares 
print(numeros[1::2])#para mostrar los numeros impares 
