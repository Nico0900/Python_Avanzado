# Iterables e Iteradores en Python

Este proyecto explica los conceptos de **iterables** e **iteradores** en Python, fundamentales para el manejo de ciclos y recorridos de datos.

---

## ¿Qué es un iterable?

Un **iterable** es un conjunto de elementos que puede ser recorrido para obtener sus valores uno a uno. En Python, los iterables incluyen:

- Cadenas de texto (`str`)
- Listas (`list`)
- Tuplas (`tuple`)
- Diccionarios (`dict`)

Un objeto es iterable si permite devolver sus elementos uno a uno para recorrerlos.

---

## ¿Qué es un iterador?

Un **iterador** es un objeto que permite recorrer un iterable. El iterador mantiene el estado interno del recorrido y devuelve el siguiente elemento cada vez que se le solicita.

---

## Funciones clave en Python para iterar

- `iter(objeto_iterable)`: recibe un iterable y retorna un iterador.
- `next(iterador)`: recibe un iterador y retorna el siguiente elemento del iterable. Si no hay más elementos, lanza un error `StopIteration`.

---

## Ejemplo en Python

```python
# Creamos un iterable (lista)
numeros = [1, 2, 3]

# Creamos un iterador a partir de la lista
iterador = iter(numeros)

print(iterador)  # <list_iterator object at 0x...>

# Obtenemos elementos usando next()
print(next(iterador))  # Output: 1
print(next(iterador))  # Output: 2
print(next(iterador))  # Output: 3

# Si intentamos obtener un elemento más, se lanzará un error StopIteration
# print(next(iterador))  # StopIteration
