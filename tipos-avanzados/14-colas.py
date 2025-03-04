pila = []
pila.append(1)
pila.append(2)
pila.append(3)
pila.append(4)
print(pila)
ultimoElemento = pila.pop()  # pop para obtener el ultimo elemento
print(ultimoElemento)
print(pila)
print(pila[-1])  # con -1 se muestra el ultimo elemento
if not pila:
    print("La pila esta vacia")
