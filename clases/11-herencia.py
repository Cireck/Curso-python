class Animal:
    def comer(self):
        print("comiendo")


class Perro(Animal):  # cuando se usa (clase que hara herencia para tomar sus metodos  y propiedades)
    def pasear(self):
        print("El perro está paseando")


class Chanchito(Perro):  # cuando se usa una clase que ya tiene una herencia se tomara toda la clase junto su herencia y no se mas de 2 niveles de herencia para evitar problemas
    def programar(self):
        print("El chanchito está pro")


chanchito = Chanchito()
chanchito.comer()
perro = Perro()


