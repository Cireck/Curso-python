from pathlib import Path

path = Path("rutas")
# path.exists()#si exite
# path.mkdir()#si no exite se crea el directorio
# path.rmdir()#elimina el directorio pero que este vacio
# path.rename("directori")#cambiar le nombre de directorio
print(path.iterdir())

for p in path.iterdir():
    print(p)
# para obtener solo los archivos
archivos = [p for p in path.iterdir() if not p.is_dir()]
archivos = [p for p in path.glob("*.py") if not p.is_dir()]#para buscar archivos con un tipo archivo o caracteres
# para buscar archivos con un tipo archivo o caracteres con * para obtener culquier archivo que tenga .py
archivos = [p for p in path.glob("01-*.py") if not p.is_dir()]
archivos = [p for p in path.glob("**/*.py") if not p.is_dir()]#para obtener todas las archivos y capertas
# otra forma de obtener  todas las archivos y capertas
archivos = [p for p in path.rglob("*.py") if not p.is_dir()]
print(archivos)