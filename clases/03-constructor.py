class Perro:
    # para usar el constuctor se usa __init__(self,variable que tendra el constructor)
    def __init__(self, nombre, edad):
        self.nombre = nombre  # se agrega nombre al self que es el constructor
        self.edad = edad  # se agrega edad al self que es el constructor
        print(nombre)

    def habla(self):
        print(f"{self.nombre} guau guau")


mi_perro = Perro('nombre', 2)
mi_perro.habla()
