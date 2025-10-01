# # # for letra in "python":
    
# # #     if letra=="h":
# # #         continue

# # # print("viendo la letra: " + letra)

# # nombre="Sebastian"

# # contador=0

# # for 1 in nombre:
# #     contador=contador+1

# # print(contador)

# while True:
#     pass # sirve para que el programa no de error, pero no hace nada

emcail=input("Introduce tu email: ")

for i in emcail:
    if i=="@":
        arroba=True
        break;
else:
    arroba=False

print(arroba)