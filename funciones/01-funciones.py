def hola():  # para definir funciones es con def
    print("Hola Mundo!")
    print("shinano")


hola()  # para ejecutar la funcion es con ()


def shinano(name, sub):
    print(f"hola {name} {sub}")


shinano("yamaato", "shinano")  # para ejecutar

# paramentros opcionales para funciones


# para hacer un paramentro opcional hay que asignar un valor al paramentro si no hay entrad de datos y si hay toma el dato de entrada
def shinano_opcionales(name, sub="shinano"):
    print(f"hola {name} {sub}")


shinano_opcionales("yamaato", 'ss')  # para ejecutar
shinano_opcionales("yamaato")  # para ejecutar

#argumentos nombrados
shinano(name="ss",sub="ssa")#para asignar una entrada o argumento especifico con un valor hay que usar su nombre y dar valor

