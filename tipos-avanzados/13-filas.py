from collections import deque

fila = deque([1, 2])
fila.append(1)  # agregar elemento nuevo a la fila
fila.append(2)
fila.append(3)
print(fila)
fila.popleft()  # elimina elemento en la fila
print(fila)
if not fila:
    print("La fila esta vacia")  # para validar si hay elementos en la fila
