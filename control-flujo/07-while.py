numero = 1
while numero < 100:  # si la varible es todavia true se siguiera ejecutando hasta que de false en la compobacion
    print(numero)
    numero *= 2

comando = ""
while comando.lower() != "salir":
    comando = input("Introduce un comando (salir para terminar): ")
    print(comando)

#loops infinitos
while True:
    comando1 = input("Introduce un comando (salir para terminar): ")
    print(comando1)
    if comando1.lower() == "salir":
        break
    print(comando1)
