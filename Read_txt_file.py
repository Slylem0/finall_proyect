from tabulate import tabulate

with open("Datos_Vuelos_Finales.txt", "r") as archivo:
    datos = archivo.readlines()

lista_limpia = []
for a in datos[1:]:
    a = a.split(",")
    lista_limpia.append(a)

place_from = []
for i in lista_limpia:
    place_from.append(i[7])

to_arrive = []
for i in lista_limpia:
    to_arrive.append(i[8])

print(tabulate(lista_limpia))
print(tabulate(place_from))
print(tabulate(to_arrive))
