"""enumerate (iterabl, start = 0)"""


nombres = ["Paco", "Emilio", "Javier", "Ana"]
nombres_enumerados = enumerate(nombres, start = 1)
print(list(nombres_enumerados))


"""ejemplos for"""

for indice, elemento in enumerate(nombres):
    print(indice , elemento)