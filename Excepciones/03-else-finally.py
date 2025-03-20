try:
    n1 = int(input("Ingresa primer numero: "))
except Exception as e:
    print("Error: Debe ingresar un numero entero.")
else:  # mostrar este mensaje o hacer la operacion si no hay errores
    print("no ocurrio ningun error.")
finally:  # mostrar el mensaje o hacer la operacion si no hay errores o haya errores
    print("se ejecutando simeprem")
