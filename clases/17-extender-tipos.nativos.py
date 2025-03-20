class Lista(list):
    def prepend(self, item):
        self.insert(0, item)


lista = Lista([2, 34, 5])
lista.append(2)
lista.prepend(0)
print(lista)
