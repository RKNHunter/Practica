class carro():

    def __init__(self):
        self.largochasis = 250
        self.anchochasis = 120
        self.ruedas = 4
        self.enmarcha = False

    def arrancar(self, arrancamos):
      self.enmarcha = arrancamos

      if(self.enmarcha):
        chequeo = self.chequeo()

      if(self.enmarcha and chequeo):
        return "El coche esta en marcha"
      
      elif(self.enmarcha and chequeo==False):
          return "Algo ha ido mal en el chequeo, no podemos arrancar"
      
      else:
        return "El coche esta parado"
    
    def estado(self):
        print("el coche tiene ", self.ruedas, "ruedas. un ancho de ", self.anchochasis, "y un largo de ", self.largochasis)

    def chequeo(self):
        print("Realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
           return True
        else:
           return False


miCarro = carro()
print(miCarro.arrancar(True))
miCarro.estado()
print("------------A continuacion creamos el segundo objeto----------")
miCarro2 = carro()
print(miCarro2.arrancar(False))
miCarro2.estado()

