"""
Crea una función que almacene un directorio de personas.
La función debe permitir agregar personas con su nombre, edad y ciudad.
Utiliza un closure para mantener el estado del directorio.
"""
# Crea un directorio de personas utilizando un closure.
# La función interna debe permitir agregar personas al directorio y mantener el estado entre llamadas.
# Cada vez que se llama a la función interna, se actualiza el directorio con la nueva persona.
# El estado del directorio se mantiene entre llamadas, permitiendo agregar múltiples personas sin perder la información previamente almacenada.

def agregar_persona_directorio():
    """
    Crea un directorio de personas utilizando un closure.
    """
    directorio = {}

    """
    Función interna que agrega una persona al directorio.
    """
    def agregar(nombre, edad, ciudad):
        directorio[nombre] = {"edad": edad, "ciudad": ciudad}
        return directorio
    
    """
    Retorna la función interna para agregar personas al directorio.
    Esta función mantiene el estado del directorio entre llamadas, permitiendo agregar múltiples personas sin perder la información previamente almacenada.
    """
    return agregar

"""
Llamada a la función para crear el closure y almacenar personas en el directorio.
"""
"""
La función `agregar_persona_directorio` crea un closure que permite agregar personas al directorio.
Cada vez que se llama a la función interna `agregar`, se actualiza el directorio con la nueva persona.
El estado del directorio se mantiene entre llamadas, permitiendo agregar múltiples personas sin perder la información previamente almacenada.
"""
almacenar = agregar_persona_directorio()
directorio = almacenar("Paco", 27, "Cali")
directorio = almacenar("Javier", 25, "Madrid")
directorio = almacenar("Emilio", 26, "Brisbane")

print(directorio)
