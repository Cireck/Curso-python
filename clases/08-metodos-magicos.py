class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):  # funcion para eliminar un elemento
        print(f"El perro {self.nombre} ha sido destruido")

    def __str__(self):  # funcion para mostrar contenido
        return f"Perro: {self.nombre}, Edad: {self.edad}"

    def habla(self):
        print(f"{self.nombre} guau guau")


perro = Perro("adada", 1)
print(perro)
texto = str(perro)  # para llamar el metod str
del perro  # formar de llamar un metodo magico
