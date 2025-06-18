lista_numeros = [1,2,3,4,5,6,7,8]

"""
uso de la funcion filter, esto devolvera un objeto de tipo filter
el cual se debe transformar a un objeto de tipo lista con la funcion *list()*
"""
lista_pares = list(filter(lambda numero : numero %2 == 0, lista_numeros))
print(lista_pares)


"""
uso de la funcion map, esto devolvera un objeto de tipo map
el cual se debe transformar a un objeto de tipo lista con la funcion *list()*
"""
nueva_lista= list(map(lambda numero : numero *10, lista_numeros))
print(nueva_lista)