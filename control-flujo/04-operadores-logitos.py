# and para dos condicciones es lo mismo que en php
# or lo mismo que php si una de las dos condicciones se cumple da true ala comprobacion
# not niega la operacion, ejemplo si no tiene , es para negar si hay o no hay

gas = True
encendido = True
edad = 18
# () cuando se usan en una operacion son los primeros que se realizan0
# if se ejecuta de izquierda a derecha y si hay dos () se ejecuta el primero ala izquierda
if gas and (encendido and edad > 17):
    print("El coche esta encendido y tiene gasolina")

if gas or encendido:
    print("El coche esta encendido o tiene gasolina1")

if not gas:
    print("El coche no tiene gasolina")
