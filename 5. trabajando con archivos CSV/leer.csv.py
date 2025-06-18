import csv

"""mostrar como columnas y listas con reader"""
with open("datos-Cap5-CSV.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.reader(archivo, delimiter=",")
    columnas = next(reader) #esta funcion quita el header (primera linea)
    print("Columnas", columnas)
    for datos in reader:
        print(datos[0])

"""mostrar como diccionario con DicReader"""
with open("datos-Cap5-CSV.csv", "r", encoding="UTF-8") as archivo:
    reader = csv.DictReader(archivo, delimiter=",")
    for datos in reader:
        print(datos)
        # print(datos["nombre"])