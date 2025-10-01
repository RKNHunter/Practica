# # i=1

# # while 1<=6:
# #     print("Ejecutado " + str(i))

# #     i=i+1
# # print("Fin del bucle")

# edad=int(input("Introduce tu edad: "))

# while edad<0 or edad>100:
#     print("Has introducido una edad incorrecta")
#     edad=int(input("Introduce tu edad: "))

# print("Edad correcta, " + "edad ingresasda: " + str(edad))

import math

print("Calculo de raiz cuadrada")
numero=int(input("Introduce un numero: "))

intentos=0

while numero<0:
    print("No se puede hallar la raiz de un numero negativo")

    if intentos==2:
        print("Has consumido demasiados intentos, el programa ha finalizado")
        break;
    numero=int(input("Introduce un numero: "))
    if numero<0:
        intentos=intentos+1

if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))

