#caso 1 
total = sum([num for num in range(100)])

#correccion caso 1
total = sum(num for num in range(100))


#caso 2
[print (element) for element in range(1)]

#correcion caso 2
for element in range(10):
    print(element)


##caso 3
lista_anidada = [[1,2], [3,4], [5,6]]

valores_lista = [numero for elemento in lista_anidada for numero in elemento]
print(valores_lista)

#correccion caso 3 
lista_anidada = [[1,2], [3,4], [5,6]]
valores_lista = []
for elemento in lista_anidada:
    for numero in elemento:
        valores_lista.append(numero)

print(valores_lista)