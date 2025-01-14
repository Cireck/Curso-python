buscar = 10
for numero in range(5):  # for variable que almacena el valor in range
    # range es un rango de numero desde 0 hasta el numero dado pero se resta -1
    print(f"Esta es la iteracion {numero + 1}")
    if numero == buscar:
        print("encontrado", buscar)
        break  # para terminar el loop cuando encuentra el numero buscado
else:
    # si no se encuentra el numero buscado en el for
    print("numero no encontrado")

for char in "Ultinate":  # char es para mostrar letra por letra el string
    print(char)
