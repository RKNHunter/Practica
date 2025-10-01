# # def suma(num1, num2):
# #     return num1 + num2

# # def resta(num1, num2):
# #     return num1 - num2

# # def multiplica(num1, num2):
# #     return num1 * num2

# # def divide(num1, num2):
# #     try:
# #         return num1 / num2
# #     except ZeroDivisionError:
# #         print("No se puede dividir entre 0")
# #         return "Operación errónea"
# # while True:
# #     try:
# #       op1 = int(input("Introduce el primer número: "))
# #       op2 = int(input("Introduce el segundo número: "))
# #       break
    
# #     except ValueError:
# #      print("Debes introducir un número")
    


# # operacion = input("Introduce la operación a realizar (suma, resta, multiplica, divide): ")

# # if operacion == "suma":
# #     print(suma(op1, op2))
# # elif operacion == "resta":
# #     print(resta(op1, op2))
# # elif operacion == "multiplica":
# #     print(multiplica(op1, op2))
# # elif operacion == "divide":
# #     print(divide(op1, op2))
# # else:
# #     print("Operación no reconocida")

# def divide():

#     try:
#         op1=(float(input("Introduce el primer número: ")))
#         op2=(float(input("Introduce el segundo número: ")))
            
#         print("El resultado es: " + str(op1/op2))
#     except ValueError:
#         print("Debes introducir un número")

#     except ZeroDivisionError:
#         print("No se puede dividir entre 0")

#     print("Operación finalizada")

# divide()

def divide():
 while True:
    
    try:
        op1=(float(input("Introduce el primer número: ")))
        op2=(float(input("Introduce el segundo número: ")))

        print("El resultado es: " + str(op1/op2))
        print("Operación finalizada")
        break
            
        

    except ValueError:
        
        print("haz ingresado un valor invalido")
        continue
    

  
    print("El resultado es: " + str(op1/op2))
    print("Operación finalizada")

divide()