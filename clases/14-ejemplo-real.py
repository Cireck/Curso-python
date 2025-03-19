class Model():
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Erro, tienes que definir una tabl")

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, id):
        print(f"Buscando  por id {id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "usuario"


usuario = Usuario()
usuario.guardar()
usuario.buscar_por_id(1)
Usuario.buscar_por_id(12)
