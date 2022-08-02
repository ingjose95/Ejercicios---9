from functools import reduce

filtrar = filter(lambda x: x%2 != 0, [1,2,3,4,5,6,7,8,9,10])

lista = list(filtrar)

print(lista)

sumar = reduce(lambda a, b: a+b, lista)

print('El resultado de la suma es: ', sumar)