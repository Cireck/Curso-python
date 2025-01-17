def no_space(texto):
    nuevoTexto = ""
    for char in texto:  # char es para recorer letra por letra de un string
        if char != " ":  # es para comprobar si hay espacio entre letras
            nuevoTexto += char
    return nuevoTexto


def reverse(texto):
    textoAlReves = ""
    for char in texto:  # char es para recorer letra por letra de un string
        textoAlReves = char + textoAlReves  # para dar vuelta el string
    return textoAlReves


def es_palindromo(texto):
    texto = no_space(texto)
    textoAlReves = reverse(texto)
    return texto.lower() == textoAlReves.lower()


print("abba", es_palindromo("abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo para"))
