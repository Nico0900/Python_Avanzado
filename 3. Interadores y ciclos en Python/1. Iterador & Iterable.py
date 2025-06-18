"""
Que es Iterable?
Son conjuntos de elementos que permiten 
retornar los elementos que los componen 
y se pueden recorrer usando ciclos

estos son objetos que permites "recorrer" un objeto iterable

"""

"""
Que es Iterador?

son aquellos que podemos recorrer un ciclo entre ellos
Cadenas de texto, listas, tuplas, diccionarios

"""

"""
solo existen dos funciones 

funcion iter()
funcion next()

"""

"""
ejemplo de uso 

numeros =[1,2,3]
>>> iterador = iter(numeros)
>>> iterador
<list_iterator object at 0x0000022D7F253400>
>>> next(iterador)
1
>>> next(iterador)
2
>>> next(iterador)
3
>>> next(iterador)
Traceback (most recent call last):
  File "<python-input-15>", line 1, in <module>
    next(iterador)
    ~~~~^^^^^^^^^^
StopIteration

"""