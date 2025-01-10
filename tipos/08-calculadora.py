# input es para obtener datos del usuario en la consola
n1 = input("ingresa primer numero: ")
n2 = input("ingresa segundo numero: ")
n1 = int(n1)  # int es para convertir el string a numero
n2 = int(n2)
suma = n1 + n2
resta = n1 - n2
div = n1 / n2
multi = n1 * n2
mensaje = f"""para los numero {n1} y {n2}, el resultado de la suma es {suma},
el resultado de la resta es {resta},
el resultado de la division es {div},
el resultado de la multiplicacion es {multi},
"""  # para usar {variable} o mostrar variables en parrafo o text se usa f antes de los ""
print(mensaje)
# print(n1, n2)
