lista = [1, 2, 3, 4, 5, 6]

def sumaPares(lista):
    suma = 0
    for i in lista:
        if i % 2 == 0:
            suma += i
    return suma

print(sumaPares(lista))