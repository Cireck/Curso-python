class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro):  # para realizar comporacion y si los objetos son iguales o no, esta funcion se usa cunado se ultilice =
        return self.lat == otro.lat and self.lon == otro.lon

    def __ne__(self, otro):  # para comprobar si son diferentes valores entre los elementos, esta funcion se usa cunado se ultilice !
        return self.lat != otro.lat and self.lon != otro.lon

    def __lt__(self, otro):  # es para comparacion de menor o mayor,, esta funcion se usa cunado se ultilice <
        return self.lat + self.lon < otro.lat + otro.lon

    def __le__(self, otro):  # es para comparacion de menor o iguales
        return self.lat + self.lon <= otro.lat + otro.lon


coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)

print(coords == coords2)  # para colobarar si son el mismo objeto
print(coords != coords2)  # para colobarar si diferente
print(coords < coords2)  # para colobarar si menor
print(coords > coords2)  # para colobarar si es mayor
print(coords <= coords2)  # para colobarar si es menor o igual
print(coords >= coords2)  # para colobarar si es mayor o igual
