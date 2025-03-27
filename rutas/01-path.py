from pathlib import Path  # para referenciar una ruta dentro de la maquina

# Path(r"C:/Archivos de Programa")#para llamar ruta en windows
# Path("/usr/bin")#en mac y es ruta absoluta
# Path()
# Path.home()
# Path("one/__init__.py")#ruta relativa y es

path = Path("hola-mundo/mi-archivo.py")
path.is_file()  # si es archivo
path.is_dir()  # direccion del archivo
path.exists()  # si existe el archivo

print(path.name, path.stem, path.suffix, path.parent, path.absolute)

p= path.with_name("shinano.py")#para cambiar el nombre del archivo y su tipo de archivo

print(p)
p = path.with_suffix(".bat")#para cambiar tipo de archivo

print(p)
p = path.with_stem("feliz")#cambiar el nombre del archivo

print(p)
