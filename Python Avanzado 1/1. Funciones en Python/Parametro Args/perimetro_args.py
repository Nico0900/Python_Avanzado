def calcular_perimetro(*args):
    """print(args)""" #solo muestra lo que contenga args
    perimetro = 0
    for lado in args:
        perimetro += lado
    return perimetro

cuadrado = calcular_perimetro(1,2,3,4)
print(cuadrado)

triangulo = calcular_perimetro(1,2,3)
print(triangulo)