"""lista = [ expresion(elemento) for elemento in objetivo_iterable ] """

def calcular_cuadrado(numero):
    return numero**2

lista_num = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrados = []
for num in lista_num:
    cuadrado = calcular_cuadrado(num)
    lista_cuadrados.append(cuadrado)

print("ciclo for", lista_cuadrados)

"""Ejemplo de list comprenhension"""
lista_comprehension = [num**2 for num in lista_num]
print("list comprehension", lista_comprehension)