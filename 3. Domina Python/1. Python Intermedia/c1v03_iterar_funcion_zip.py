# Creamos una lista de nombres
lista_nombres = ["Ana", "Paco", "Javier", "Emilio"]

# Creamos una lista de edades correspondientes a los nombres
lista_edades = [25, 27, 25, 26]

# Usamos la función zip para combinar ambas listas en pares (nombre, edad)
datos_zip = zip(lista_nombres, lista_edades)

# Imprimimos el objeto zip (esto solo muestra que es un objeto zip, no su contenido)
print(datos_zip)

# Convertimos el objeto zip en una lista de tuplas y la imprimimos
print(list(datos_zip))

# Intentamos iterar sobre datos_zip, pero ya fue consumido al convertirlo en lista, así que este bucle no imprime nada
for nombre, edad in datos_zip:
    print(nombre, edad)