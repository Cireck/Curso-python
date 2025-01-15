def suma(*numeros):  # para tomar todos los paramentros de entrada que ingresen y asi evitar nombralos uno por uno, para usar hay que poner *nombre e pural, se usaria con arreglos un ejemplo
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 6)
suma(2, 6, 66)
suma(2, 6, 666)
suma(2, 6, 4)
