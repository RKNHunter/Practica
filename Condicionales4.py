# print("Progragama de becas año 2025")
# distancia =int (input("Introduce la distancia a la que vives de la universidad en km: "))
# print(distancia)

# numero_hermanos =int (input("Introduce el numero de hermanos que tienes: "))
# print(numero_hermanos)

# salario_familiar =int (input("Introduce el salario anual de tu familia sin puntos ni comas: "))
# print(salario_familiar)

# if distancia > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
#     print("Seleccionado para beca")
# else:
#     print("No seleccionado para beca")

print("Asignaturas complementarias año 2025")
print("asginaturas complementarias: Ingles - Frances -Aleman - Programacion - Diseno web")
opcion = input("Introduce la asignatura escogida: ")

asignatura = opcion.lower()

if asignatura in ("ingles", "frances", "aleman", "programacion", "diseno web"):
    print("Asignatura elegida: " + asignatura)
else:
    print("Asignatura no contemplada")
