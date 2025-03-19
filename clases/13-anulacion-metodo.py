class Ave:
    def __init__(self):
        self.volador = "voaldor"

    def vuela(self):
        print('El ave vuela')


class Pato(Ave):
    def __init__(self):
        super().__init__()  # ejectua un metodo de clase padre antes de ejecutar el metodo del hijo
        self.nada = True

    def vuela(self):
        super().vuela()  # ejectua un metodo de clase padre antes de ejecutar el metodo del hijo
        print('El pato vuela')


pato = Pato()
pato.vuela()
print(pato.volador, pato.nada)
