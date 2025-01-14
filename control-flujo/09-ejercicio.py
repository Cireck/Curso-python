# verificar numero si ha ingresado n1
# ingrese operacion op
# ingrese otro numero n2
# mostrar resultado y pasar el valor al n1
# ingrese operacion op
# ingrese n2

print("Bienvenidos a la calculadora")
print("Para salir escribe Salir")
print("Las operaciones son suma, multi, div y resta")
resultado = ""
while True:
    if not resultado:
        resultado = input("ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("ingresa operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("ingrese otro numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    elif op.lower() == "resta":
        resultado -= n2
    else:
        print("operacion no valida")
        break
    print(f"el resultado es {resultado}")
