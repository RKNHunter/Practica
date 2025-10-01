class Carro():
    largochasis = 250
    anchochasis = 120
    ruedas = 4
    enmarcha = False

    def arrancar(self):
        pass
    def estado(self):
        if self.arrancar:
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

miCarro = Carro()
print("El largo del coche es: ", miCarro.largochasis)
print("El coche tiene: ", miCarro.ruedas, "ruedas")
miCarro.arrancar()

print(miCarro.estado())