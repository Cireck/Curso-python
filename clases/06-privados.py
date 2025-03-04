class Perro:
  # para usar el constuctor se usa __init__(self,variable que tendra el constructor)
    # con ctrl+shift+p buscamos rename symbol es para cambiar el nombre de una variable y remplzar con otro nombre en todo el codigo
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # se agrega nombre al self que es el constructor
        # __ la variable se comvirte en privado y no se podra moficar el valor y  no se puede acceder fuera de clase
        self.edad = edad  # se agrega edad al self que es el constructor
        print(nombre)

    def get_nombre(self):  # para obtener el nombre que se convertio en privado
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def habla(self):  # cls es igual a self y puede usar la clase
        print(f"{self.__nombre} guau guau")

    @classmethod
    def factory(cls):
        return cls("chas", 3)


perro1 = Perro.factory()

perro1.habla()
print(perro1.get_nombre())
print(perro1.__dict__)  # __dict__ es para obtener todos las variables de la clase
print(perro1._Perro__nombre)
