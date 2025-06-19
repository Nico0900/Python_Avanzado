import csv

columnas = ["nombre", "apellido", "edad"]
dato = ["Paco", "Botero", 26]

datos_lista=[
    ["Paco", "Botero", 26],
    ["Javier", "Quinonez", 24],
    ["Emilio", "Tafur", 25]
]

datos_dict = [
    {"nombre":"Paco", "apellido": "Botero", "edad":26},
    {"nombre":"Javier", "apellido": "Quinonez", "edad":24},
    {"nombre":"Emilio", "apellido": "Tafur", "edad":25}
]

# with open("datos.csv", "w", newline="") as archivo: 
#     writer = csv.writer(archivo, delimiter=",")
#     writer.writerow(columnas) #aqui se inserta como primera fila los nombres de las columnas
#     """writer.writerow(dato)""" #sirve para enviar solo una fila de datos
#     """writer.writerows(datos_lista)""" #sirve para enviar una lista anidada

with open("datos-Cap5-CSV.csv", "w", newline="") as archivo: 
    writer = csv.DictWriter(archivo, fieldnames=columnas) #fieldnames toma los datos que existen en la lista "columnas" para dejarlo como primer fila
    writer.writeheader() #aqui tomamos los fieldnames y los dejamos como primera fila
    writer.writerows(datos_dict) #aqui tomamos el diccionario que tenemos guaradado

