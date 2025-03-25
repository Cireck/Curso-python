# para usar o importar un archivo y podemos especificar que funciones o cualquier cosa que queremos
# despues de import que funciones se van importar como un trait
# from usuarios.acciones import guardar, pagar_impuestos #esta forma se recomienda usar mejor
# import usuarios.acciones
# from carperta import archivo
# from usuarios import acciones
# funciones del archivo importado por from
# guardar()
# pagar_impuestos()

# para usar funciones del archivo importado por import
# acciones.guardar()
# formar de usar subcapertas y importar archivo fuera de la caperta raiz del archivo
# from usuarios.impuestos.utilidades import guardar, pagar_impuestos  # subcapertas
# pagar_impuestos()
# uso de dir donde muestra la ruta desde el inicio hasta llegar al archivo
# from usuarios.impuestos.utilidades import guardar, pagar_impuestos
# import usuarios

# print(dir(usuarios))
# print(usuarios.__name__)
# print(usuarios.__package__)
# print(usuarios.__path__)
# print(usuarios.__file__)


# paquete con nombre dinamicos
from usuarios.impuestos.utilidades import guardar, pagar_impuestos
pagar_impuestos()
print(__name__)
