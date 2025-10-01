def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        # for subElemento in elemento:
            yield from elemento

cuidades_devuelve=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(cuidades_devuelve))
print(next(cuidades_devuelve))

