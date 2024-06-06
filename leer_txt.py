from tabulate import tabulate

with open(fr"C:\Users\pnico\Documents\Finall_proyect\finall_proyect\Datos_Vuelos _Finales.txt", "r") as archivo:
    datos = archivo.readlines()

lista_limpia = []
for a in datos[1:]:
    a = a.split(",")
    lista_limpia.append(a)

place_from = []
for i in lista_limpia:
    # Remove spaces and quotes
    cleaned_data = i[7].replace(" ", "").replace("'", "")
    place_from.append(cleaned_data)

to_arrive = []
for i in lista_limpia:
    # Remove spaces and quotes
    cleaned_data = i[8].replace(" ", "").replace("'", "")
    to_arrive.append(cleaned_data)

print(tabulate(lista_limpia))
print(tabulate(place_from))
print(tabulate(to_arrive))