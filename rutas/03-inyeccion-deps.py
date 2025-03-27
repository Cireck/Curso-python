from pathlib import Path

path = Path()

# se obtiene todos los directorios
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {"db": "base de datos",
                "api": "esta es la api", "graphql": "esto es graphql"}


def load1(p):
    paquete = __import__(str(p).replace("/", "."))
    try:
        # desampaquetamiento para otener todo el contenido
        paquete.init(**dependencias)
    except:
        print("Error")


list(map(load1, paths))
