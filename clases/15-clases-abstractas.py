from abc import ABC, abstractmethod


class Model(ABC):

    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(self, id):
        print(f"Buscando  por id {id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "usuario"

    def guardar(self):
        print("guardando usuario")


usuario = Usuario()
usuario.guardar()
usuario.buscar_por_id(1)
Usuario.buscar_por_id(12)
