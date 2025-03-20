# from abc import ABC, abstractmethod


# class Model(ABC):

#   @property
#  @abstractmethod
# def guardar(self):
#    pass


class Usuario():
    def guardar(self):
        print("Guardando usuario...")


class Sesion():
    def guardar(self):
        print("Guardando sesión...")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()

# se usa para mostrar dos funciones en una sola o realizar una operacion con dos o mas elementos
guardar([sesion, usuario])
