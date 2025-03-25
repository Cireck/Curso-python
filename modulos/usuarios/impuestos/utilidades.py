if __name__ != '__main__':  # colobora si el archivo es la raiz donde se ejecuta la operacion
    print("Este archivo no se puede ejecutar como script")

    # usar archivo dentro de otra caperta fuera de la caperta raiz del archivo
    # cada . es un salto a fuera de la caperta raiz donde esta el archivo
    # import relativo donde hay que llegar ala caperta desde saltos
    from ..gestion.crud import guardar
    # import absoluto donde usamos el nombre de la caperta principal donde se encuentra el archivo
    from usuarios.gestion.crud import guardar
    print(__name__)

    def pagar_impuestos():
        print("Pagar impuestos")
        guardar()

if __name__ == '__main__':  # colobora si el archivo es la raiz donde se ejecuta la operacion
    print("tarea en mantenimiento")
