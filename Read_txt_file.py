from tabulate import tabulate

with open("Datos_Vuelos_Finales.txt", "r") as archivo:
    datos = archivo.readlines()

lista_limpia = []
for a in datos[1:]:
    a = a.split(",")
    lista_limpia.append(a)

print(tabulate(lista_limpia))
