"""podran ver que se imprimen los numeros, del 1 hasta el 3"""

numeros = [1,2,3,4,5]

for numero in numeros:
    if numero == 3:
        break
    print(numero)


"""podran ver que se imprimen todos los numeros, menos el 3"""

numeros = [1,2,3,4,5]

for numero in numeros:
    if numero == 3:
        continue
    print(numero)


"""aqui podras ver que el for se termina en la primera vuelta"""
numeros = [1,2,3,4,5]

for numero in numeros:
    print(numero)
    break