"""
    lista = [ expresion(elemento) for element in objetivo_iterable if conditions ] 
    lista = [ expresion(condition) for elemento in objeto_iterable ]  
"""

def calcular_cuadrado(numero):
    return numero**2

def es_par(numero):
    return numero % 2 == 0

lista_num = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrados = []
for num in lista_num:
    cuadrado = calcular_cuadrado(num)
    lista_cuadrados.append(cuadrado)

print("ciclo for", lista_cuadrados)

"""Ejemplo de list comprenhension"""
lista_comprehension = [num**2 for num in lista_num]
print("list comprehension", lista_comprehension)

"""Ejemplo de list comprenhension con 1 condicion"""
lista_comprehension_pares = [calcular_cuadrado(num) for num in lista_num if es_par(num)]
print("list comprehension es par", lista_comprehension_pares)

"""Ejemplo de list comprenhension con doble condicion"""
lista_comprehension_pares = [calcular_cuadrado(num) if es_par(num) else 0 for num in lista_num]
print( lista_comprehension_pares)