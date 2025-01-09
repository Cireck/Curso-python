animal = "   shinano  ass   "
print(animal.upper())  # upper es para transformar el string en mayusculas
print(animal.lower())  # lower es para transformar el string en minusculas
print(animal.capitalize())
# capitalize es para tomar la primera letra en mayuscula y el resto en minusculas

print(animal.title())
# title es para tomar la primera letra de cada palabra en mayusculas y el resto en minusculas
# strip es eliminar ala izquierda y derecha los espacios en blanco en el string y en medio no los elimina
print(animal.strip())
print(animal.strip().capitalize())  # se puede encadenar los metodos, se usara primero strip ya que capitalize esta tomando el espacio ala izquierda y esta transformando en mayusculas y el resto en minusculas, con ello quedar bien la funcion
# lstrip para eliminar los espacios ala izquierda de la primera letra
print(animal.lstrip())
# rstrip para eliminar los espacios ala derecha de la ultima letra
print(animal.rstrip())
print(animal.find('na'))  # find("palabra que buscaremos dentro de la cadena") nos arroja el indice donde se encuentra la primera letra de la busqueda y encaso que no se encuentra la busqueda arroja un -1
# replace("palabra que buscaremos dentro de la cadena que se va replazar los caracteres","carecteres que replazaran ala busqueda") si no encuentra la busqueda no hace nada
print(animal.replace("nano1", "ss"))
print("yamato " in animal)# "caracteres que se buscaran en la cadena" in variable string es para saber si existe la busqueda en la cadena, si esta la busqueda nos arroja true y si no false 
# "caracteres que se buscaran en la cadena"not in variable string es para saber si la busqueda no esta en la cadena, si esta la busqueda nos arroja false y si no true
print("yamato" not in animal)
