"""Funcion compleja de python"""
def separar_par_impar(lista_numeros):
    pares = []
    impares = []
    for numero in lista_numeros:
        if numero %2 == 0:
            pares.append(numero)
        else: 
            impares.append(numero)
    return pares, impares
"""Funcion compleja de python posible transformar a Funcion lambda"""
def calcular_area_cuadrado(lado):
    return lado ** 2

"""Funcion transformada a Funcion lambda"""
calcular_cuadrado = lambda lado : lado ** 2
print(calcular_cuadrado(2))