# para usar kwargs se usa **variable esto es usaria con arreglos asociados
def get_product(**datos):
    print(datos)
    # para acceder a un variable en especifico se usa ["nombre de la variable"]
    print(datos["nombre"], datos["apellido"])


# se puede pasar mas argumentos sin necesidad de especificarlos en la llamada
get_product(nombre="Shinano", apellido="Yamato", edad=25)
