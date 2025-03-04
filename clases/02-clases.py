class Perro:
    def habla(self):  # los def se convierten en metodo y no funciones y el parametro de entrada  debe incluir self
        print("guau guau")


miPerro = Perro()
miPerro.habla()
print(type(miPerro))
# con isinstance(metodo a buscar, Clase donde se va a buscar) es para comprobar si el metodo existe en la clase
print(isinstance(miPerro, Perro))
