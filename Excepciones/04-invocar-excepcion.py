def division(n=0):
    if n == 0:
        # raise es para lamar un exception
        raise ZeroDivisionError("no se puede dividir por 0", f"{n}")
        return 5 / n


try:
    division()
except ZeroDivisionError as e:
    print("Error: ", e)
