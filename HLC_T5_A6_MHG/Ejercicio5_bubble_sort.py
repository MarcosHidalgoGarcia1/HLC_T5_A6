def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

# 1a iteracion: i=0, j=0, lista[j]=8, lista[j+1]6 > [6,8,1,4]
# 2a iteracion: i=0, j=1, 8, 1 > [6,1,8,4]
# 3a iteracion: i=0, j=2, 8, 4 > [6,1,4,8]
# 4a iteracion: i=0, j=3, 8, index out of range > []

                
lista_ordenada = bubble_sort([8,6,1,4])
print(lista_ordenada)