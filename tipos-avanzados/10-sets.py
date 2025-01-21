# set significa grupo o conjunto
# es para evitar numeros duplicados y solo mostrar un numero de cada elemento encontrado y para usar set se usa {}
primer = {1, 2, 2, 3, 31, 1}
# primer.add(5)
# primer.remove(1)
# print(primer)

segundo = [3, 1, 2, 5, 6]
segundo = set(segundo)  # para convertir la variable en un set
# solo mostrarla un numero de cada elemento y elimina los duplicados pero se usa con | que signifaca union
print(primer | segundo)
# con & significa interseccion solo mostraran los numeros que concindan entre los dos sets y solo mostrar un numero y elimina los duplicados
print(primer & segundo)
# con - significa diferencia elimina los elementos del primer set si hay un numero parecido y solo mostrarla los numeros que no considan entre sets
print(primer - segundo)
# con ^ diferencia simetrica es para mostrar los elementos que no se encuentre entre los dos sets, digamos que eliminan los elementos duplicados entre los sets
print(primer ^ segundo)
# los sets no encuentran ordenados y no se pueden ordenar
# solo se puede hacer comprobaciones si existe un elemento en el set
if 5 in segundo:
    print("ada")
