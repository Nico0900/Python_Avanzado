import json

with open("persona-CAP7.json", "r") as archivo_json:
    datos_json = json.load(archivo_json)

#tipo de dato
print(type(datos_json))
#opcion 1 para ver json
print(datos_json)

#opcion 2 para ver json
print(f"""
Nombre : {datos_json["nombre"]},
Apellido : {datos_json["apellido"]},
Edad : {datos_json["edad"]} 
""")