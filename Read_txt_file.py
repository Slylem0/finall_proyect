
# Reading the txt and organazing it as a list
with open("Datos_Vuelos_Finales.txt", "r") as archivo:
    datos = archivo.readlines()

lista_limpia = []
for a in datos[1:]:
    a = a.split(",")
    lista_limpia.append(a)

place_from = []
for i in lista_limpia:
    place_from.append(i[7])

arrive_to = []
for i in lista_limpia:
    arrive_to.append(i[8])

print(lista_limpia)


# Functions to find the flight that satisfy the requirements
def search_flight(where_from):
    counter = 0
    ubi_flight = []
    go_to = []
    for i in place_from:
        if where_from == i:
            ubi_flight.append(counter)
        counter += 1
    for i in ubi_flight:
        go_to.append(lista_limpia[i][1]+", "
                     + lista_limpia[i][8].strip("\n"))
    return go_to


print(search_flight("Cali"))
