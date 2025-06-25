import time


def medir_tiempo_ejecucion(funcion):
    """
    en este caso, el decoracdor, exijira el parametro que llamamos [rango]
    """
    # def wrapper(rango):
    """
    pero podemos reemplazar el parametro por *args y **kwargs para que el decorador pueda recibir cualquier cantidad de parametros
    """
    def wrapper(*args, **kwargs):
        inicio = time.time()
        funcion(*args, **kwargs)
        fin = time.time()
        tiempo_total = fin - inicio
        print(f"Tiempo total de ejecución: {tiempo_total}")

    return wrapper


@medir_tiempo_ejecucion
def recorrer_ciclo(rango):

    for i in range(rango):
        print(i)
        time.sleep(1)


recorrer_ciclo(rango=5)
