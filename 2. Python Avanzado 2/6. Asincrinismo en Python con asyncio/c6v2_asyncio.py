import asyncio
import time

# Esta función es síncrona: se ejecuta de principio a fin bloqueando el hilo principal
def funcion_sincrona():
    print("Ejecutando función síncrona")
    time.sleep(1)  # simula una operación que tarda 1 segundo
    print("Fin función síncrona")

# Esta función es asíncrona: permite que el event loop siga ejecutando otras tareas mientras espera
async def funcion_asincrona():
    print("Ejecutando función asíncrona")
    await asyncio.sleep(1)  # simula una operación que tarda 1 segundo, pero sin bloquear
    print("Fin función asíncrona")

# Esta función principal es asíncrona y se encarga de crear y esperar varias corutinas
async def main():
    # Creamos una lista de dos corutinas que ejecutan la misma función asíncrona
    corrutinas = [funcion_asincrona(), funcion_asincrona()]
    # Esperamos a que ambas corutinas terminen en paralelo usando asyncio.gather
    await asyncio.gather(*corrutinas)

# Medimos el tiempo de ejecución del bloque asíncrono
inicio = time.time()
asyncio.run(main())  # ejecuta el event loop y llama a la función main
print(f"Tiempo asíncrono: {time.time() - inicio}")

# Medimos el tiempo de ejecución del bloque síncrono
inicio = time.time()
funcion_sincrona()  # llamada 1, se ejecuta de forma secuencial y bloqueante
funcion_sincrona()  # llamada 2, se ejecuta después de que termine la anterior
print(f"Tiempo síncrono: {time.time() - inicio}")
