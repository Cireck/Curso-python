# tuplas es para evitar modificaciones en el listado y nunca se puede modificar
numeros = (1, 2, 3, 34)+(4, 5, 6, 4)
print(numeros)

numeros1 = [1, 32, 1, 1, 5]
# tuple()es para corvetir una lista los elementos en uuna  tupla
punto = tuple(numeros1)
print(punto)
menosNumeros = numeros1[:2]
print(menosNumeros)

primero, segundo, *otros = numeros1
print(primero, segundo, otros)

# papa editar una tupla a qe pasarla una list

listaNumeros = list(numeros)
listaNumeros[0] = "sasa"
print(listaNumeros)
