listaPaises = []

paises = input('Ingrese una lista de paises (separados por coma y sin espacios):' )

#con title se garantiza que el nombre del pais tenga su primera
#letra en mayuscula, y con split se separa la lista luego de la coma

listaPaises = paises.title().split(',')

#se eliminan o verifican elementos repetidos

listaDepurada = set(listaPaises)

#se ordena en orden alfabetico

listaOrdenada = sorted(listaDepurada)

print(listaOrdenada)
