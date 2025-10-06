class carro():
    def dezplamiento(sself):
        print("El coche se esta desplazando 2")

class moto():
    def dezplamiento(self):
        print("La moto se esta desplazando 4")

class camion():
    def dezplamiento(self):
        print("El camion se esta desplazando 6")


def dezpazamientoVehiculo(vehiculo):
    vehiculo.dezplamiento()

mivehiculo = camion()
dezpazamientoVehiculo(mivehiculo)

