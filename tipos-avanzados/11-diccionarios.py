# serian los arrreglos asosiciados por un numbre del elemento con su valor
# "solo acepta string para nombre del elemento": acepta cualquier valor
punto = {"x": 0, "y": 50}
print(punto)
print(punto["x"])

punto["z"] = 50  # crear o agregar nuevo elemento
print(punto)
# print(punto, punto["lala"])
if "lala" in punto:  # para validar o buscar si existe un elemento en la llist
    print("encontre lala", punto["lala"])

print(punto.get("x"))  # obtener el elemento de otra manera
# cuando se usa get si el elemento no se encuentra se debera poner un valor por defecto usando la , valor
print(punto.get("lala", 97))
del punto["x"]  # del es para eliminar elmento de una lista
del (punto["y"])

print(punto)
punto["x"] = 10

for valor in punto:
    # el valor muestra el nombre del elemento, punto[valor] muestra el valor del elemento
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)  # muestra el nombre del elemento y el valor del elemento en manera de tupla que no se puede editar los elementos

for llave, valor in punto.items():
    # donde se asigna el nombre del valor ala variable llave y el valor del elemento en valor
    print(llave, valor)

usuarios = [{"id": 1, "name": "shinano"}, {
    "id": 2, "name": "shinano1"}, {"id": 3, "name": "shinano2"}]

for usuario in usuarios:
    print(usuario["name"])
