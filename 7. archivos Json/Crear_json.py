"""Serializar un Json en Python"""

import json

persona = {
    "nombre" : "Javier",
    "apellido" : "Quinonez",
    "edad" : 24
}

"""opcion 1 de manera cascada ordenado"""
objeto_json = json.dumps(persona, indent=2)
with open("persona-CAP7.json", "w") as archivo_json:
    archivo_json.write(objeto_json)

"""opcion 2 de manera lista ordenado"""
# with open("persona-CAP7.json", "w") as archivo_json:
#     json.dump(persona, archivo_json)  