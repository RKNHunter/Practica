# def generaPares(Limite):
#     num = 1
#     while num <= Limite:
      
#         yield num
#         num = num + 1

# devuelvePares = generaPares(10)

# print(generaPares(10))

def generaPares(Limite):
    num = 1
    while num < Limite:
      
        yield num*2
        num = num + 1

devuelvePares = generaPares(10)

print(next(devuelvePares))

print("Aqui prodriamos tener mas codigo")
print(next(devuelvePares))

print("Aqui prodriamos tener mas codigo")
print(next(devuelvePares))

print("Aqui prodriamos tener mas codigo")
print(next(devuelvePares))

print("Aqui prodriamos tener mas codigo")
print(next(devuelvePares))

print("Aqui prodriamos tener mas codigo")
print(next(devuelvePares))


