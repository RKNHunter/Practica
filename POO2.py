class carro():

    def __init__(self):
        self.largochasis = 250
        self.anchochasis = 120
        self.ruedas = 4
        self.enmarcha = False

def arrancar(self, arrancamos):
    self.enmarcha = arrancamos
    
    if(self.enmarcha):
        return "El coche esta en marcha"
    else:
        return "El coche esta parado"
    
def estado(self):
    print("el coche tiene ", self.ruedas, "ruedas. un ancho de ", self.anchochasis, "y un largo de ", self.largochasis)

miCarro = carro()
print(miCarro.arrancar(True))
miCarro.estado()
print("------------A continuacion creamos el segundo objeto----------")
miCarro2 = carro()
print(miCarro2.arrancar(False))
miCarro2.estado()

