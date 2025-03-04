class Perro:
    patas = 4
  # para usar el constuctor se usa __init__(self,variable que tendra el constructor)

    def __init__(self, nombre, edad):
        self.nombre = nombre  # se agrega nombre al self que es el constructor
        self.edad = edad  # se agrega edad al self que es el constructor
        print(nombre)

    def habla(self):
        print(f"{self.nombre} guau guau")


Perro.patas = 3  # se puede cambiar el valor de propiedades dentro de la clase
mi_perro = Perro('nombre', 2)
# solo se cambia el valor dentro del variable y no el valor de la propiedad de la clase
mi_perro.patas = 2
mi_perro.habla()
print(Perro.patas)
print(mi_perro.patas)
