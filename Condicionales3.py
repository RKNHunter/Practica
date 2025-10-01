# Edad = -7

# if 0 < Edad < 100:
#     print("edad correcta")
# else:
#     print("edad incorrecta")


Salario_presodente =int(input("Introduce el salario del presidente: "))
print("Salario presidente: " + str(Salario_presodente))
Salario_director =int(input("Introduce el salario del director: "))
print("Salario director: " + str(Salario_director))
Salario_jefe_area =int(input("Introduce el salario del jefe de area: "))
print("Salario jefe de area: " + str(Salario_jefe_area))
Salario_administrativo =int(input("Introduce el salario del administrativo: "))
print("Salario administrativo: " + str(Salario_administrativo))

if Salario_administrativo < Salario_jefe_area < Salario_director < Salario_presodente:
    print("Todo funciona correctamente")
else:
    print("Algo falla en esta empresa")



