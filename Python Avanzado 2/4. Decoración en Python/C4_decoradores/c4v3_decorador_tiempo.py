import time

"""
un decorador es una función que recibe otra función como argumento y devuelve una nueva función que generalmente la modifica y la retorna
"""
def medir_tiempo_ejecucion(funcion):

    def wrapper(): #Funcion envoltura que añade funcionalidad
        print("Iniciando la medición del tiempo de ejecución...")
        inicio = time.time()
        funcion()
        fin = time.time()
        tiempo_total = fin - inicio
        print(f"Tiempo total de ejecución: {tiempo_total}")

    return wrapper


@medir_tiempo_ejecucion
def recorrer_ciclo():

    for i in range(5):
        print(i)
        time.sleep(1)


recorrer_ciclo()
