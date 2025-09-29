def evaluacion (nota):
    va ="aprobado"
    if nota < 5:
        va = "suspendido"
    return va
    
print(evaluacion(4))

print("progama de evaluacion de notas")
nota = input("introduce la nota del alumno: ")
print(evaluacion(int(nota)))

