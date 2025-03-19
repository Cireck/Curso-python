class Animal:
    def comer(self):
        print("comiendo")


class Perro:
    def pasear(self):
        print("El perro está paseando")


class Volador:
    def volar(self):
        print("El perro está volando")


class Nadador:
    def nadar(self):
        print("El perro está nadando")


class Pato(Volador, Nadador, Animal):
    def pato(self):
        print("El pato está patando")


class Chanchito(Perro, Animal):  # (cuando se usa , es para usar varios clases para hacer herencia ) se recomienda que los metodos no concienden los nombres entre los metodos que haya en las clases para evitar la problemas de sustituir entre ellas
    def programar(self):
        print("El chanchito está pro")
