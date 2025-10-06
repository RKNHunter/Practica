# NombreUsuario = input("Introduce tu nombre de usuario: ")
# print("El nombre de usuario es: " + NombreUsuario.capitalize())
# print("El nombre de usuario es: " + NombreUsuario.upper())
# print("El nombre de usuario es: " + NombreUsuario.lower())




edad = input("Introduce tu edad: ")

while(edad.isdigit()==False):
    print("Error, introduce un numero")
    edad = input("Introduce tu edad: ")

if (int(edad) <18):
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

