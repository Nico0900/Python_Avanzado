"""
la funcion zip sirve para unir listas segun sus posiciones transformandolos asi en tuplas,
si un elemto de alguna de las listas que estan en uso tiene un elemento mas que la otra
este no se incluira como tupla.
""" 

"""
ejemplos 

nombres = ["Paco", "Emilio", "Javier"]
apellidos = ["Botero", "Tafur", "Quiñonez"]

nombre_completo = zip(nombres, apellidos)
print(list(nombre_completo))

>>> [('Paco', 'Botero'), ('Emilio', 'Tafur'), ('Javier', 'Quiñonez')]

"""
#ejercicio
nombres = ["Paco", "Emilio", "Javier"]
apellidos = ["Botero", "Tafur", "Quiñonez"]

nombre_completo = zip(nombres, apellidos)
print(list(nombre_completo))


"""separados por posiciones"""
nombres_unzip, apellidos_unzip = zip(*nombre_completo)
print(nombres_unzip)
print(apellidos_unzip)

"""ciclo imprimiendo los elementos segun se index (posicion)"""
for nombre, apellidos in zip(nombres, apellidos):
    print(nombres, apellidos)