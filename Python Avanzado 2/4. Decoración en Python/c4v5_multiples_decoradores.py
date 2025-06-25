import time

"""
tambien es posible multiplicar decoradores, es decir, aplicar varios decoradores a una misma funcion 
en este caso, el decorador [medir_tiempo_ejecucion] se ejecutara primero, y luego el decorador [decorador_puntos]
"""
def medir_tiempo_ejecucion(funcion):

    def wrapper(*args, **kwargs):
        inicio = time.time()
        funcion(*args, **kwargs)
        fin = time.time()
        tiempo_total = fin - inicio
        print(f"Tiempo total de ejecución: {tiempo_total}")

    return wrapper


def decorador_puntos(funcion):

    def wrapper(*args, **kwargs):
        print("..........")
        funcion(*args, **kwargs)
        print("..........")

    return wrapper

"""
aca se pueden aplicar varios decoradores a la misma funcion,
en este caso, el decorador [medir_tiempo_ejecucion] se ejecutara primero, y luego el decorador [decorador_puntos].

Todo esto tiene una gerarquia, es decir, el decorador que se aplica primero es el que se ejecuta primero. con esto podemos ver que SI importa el orden de los decoradores. en a impresion de la consola se puede ver que primero se imprime el tiempo de ejecucion, y luego los puntos.
"""

@decorador_puntos
@medir_tiempo_ejecucion
def recorrer_ciclo(rango):

    for i in range(rango):
        print(i)
        time.sleep(1)


recorrer_ciclo(rango=5)
