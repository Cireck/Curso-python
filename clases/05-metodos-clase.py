class Perro:
    patas = 4
  # para usar el constuctor se usa __init__(self,variable que tendra el constructor)

    def __init__(self, nombre, edad):
        self.nombre = nombre  # se agrega nombre al self que es el constructor
        self.edad = edad  # se agrega edad al self que es el constructor
        print(nombre)

    @classmethod  # se crea un metodo de clase
    def habla(cls):  # cls es igual a self y puede usar la clase
        print("guau guau")

    @classmethod
    def factory(cls):
        return cls("chas", 3)


Perro.habla()
perro1 = Perro('asa', 1)
perro2 = Perro('asa1', 12)
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)
