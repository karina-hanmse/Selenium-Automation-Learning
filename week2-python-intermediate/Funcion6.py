#una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
def Cuadrados(lista):
    list = []
    for i in lista:
        list.append(i**2)
    return list    


print (Cuadrados([1,8,6,4]))