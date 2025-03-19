class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    @property  # property para hacer una funcion en una propiedad donde no se mostrar en la terminar con print y no se mostra en el autocompletado del codigo
    def nombre(self):
        return self.__nombre

    @nombre.setter  # nombre es una propiedad y se le puede asignar una funcion para dar valor al elemento
    def nombre(self, nombre):
        print("aasasa")
        if nombre.strip():
            self.__nombre = nombre
        return


perro = Perro("shinano")
print(perro.nombre)
