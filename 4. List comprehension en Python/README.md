# Creación de una lista usando la función map() en Python

Este proyecto muestra cómo usar la función `map()` para aplicar una función a todos los elementos de una lista y crear una nueva lista con los resultados.

---

## ¿Qué es la función map()?

La función `map()` recibe dos argumentos principales:

1. Una función que será aplicada a cada elemento.
2. Un iterable (como una lista) cuyos elementos serán procesados.

`map()` devuelve un objeto **map**, que es un iterador con los resultados de aplicar la función a cada elemento del iterable.

---

## Ejemplo clásico sin usar map()

```python
# Función que calcula el cuadrado de un número
def calcular_cuadrado(numero):
    return numero ** 2

# Lista original de números
lista_num = list(range(1, 11))

# Lista vacía para almacenar resultados
lista_cuadrados = []

# Usando un ciclo for para calcular los cuadrados
for numero in lista_num:
    cuadrado = calcular_cuadrado(numero)
    lista_cuadrados.append(cuadrado)

print(lista_cuadrados)
# Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
