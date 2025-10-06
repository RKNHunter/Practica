# # return "{}{}{}".format(self.nombre, self.apellido, self.edad)
# # return f"{self.nombre} {self.apellido} {self.edad}"

# x,y = 10, 20

# print(f"El valor de x es {x} y el valor de y es {y}, y su suma es {x+y}")
# print("la suma de {} y {} es {}".format(x,y,x+y))

import timeit

nombre = "Juan"
edad = 30

# Usando f-strings
calculo_f_string = timeit.timeit(
    'f"Hola {nombre} tienes {edad} años."', 
    globals=globals(), 
    number=1000000
)

# Usando .format()
calculo_format = timeit.timeit(
    '"Hola {} tienes {} años.".format(nombre, edad)', 
    globals=globals(), 
    number=1000000
)

print(f"Tiempo usando f-strings: {calculo_f_string} segundos")
print(f"Tiempo usando .format(): {calculo_format} segundos")

