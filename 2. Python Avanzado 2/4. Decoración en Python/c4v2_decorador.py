


"""
los decoradores pertenecen al patron de diseño de programación orientada a objetos conocido como "decorador". este patrón permite añadir funcionalidad a una función o clase sin modificar su código original. en Python, los decoradores son funciones que reciben otra función como argumento y devuelven una nueva función con la funcionalidad añadida.
los decoradores se utilizan para modificar el comportamiento de una función o clase, añadiendo funcionalidades adicionales, como la validación de parámetros, la autenticación de usuarios, el registro de eventos, o la medición del tiempo de ejecución, entre otros.
los decoradores se aplican a funciones o métodos utilizando el símbolo "@" seguido del nombre del decorador antes de la definición de la función o método. esto permite aplicar el decorador de manera más legible y concisa, sin necesidad
de modificar el código original de la función o método.
los decoradores son una herramienta poderosa en Python que permite modificar el comportamiento de las funciones y clases
de manera flexible y reutilizable. al utilizar decoradores, se puede mejorar la legibilidad del código, reducir la duplicación de código y añadir funcionalidades adicionales sin modificar el código original.
"""
def funcion_decorador(funcion):
    
    def funcion_wrapper():

        print("Dentro de la función wrapper")
        funcion()

    return funcion_wrapper


def funcion_prueba():
    print("Función de prueba")


# Añadir el decorador como instancia
funcion_prueba = funcion_decorador(funcion_prueba) #decorador añadido como instancia
funcion_prueba()


# Añadir el decorador de manera Pythonica
@funcion_decorador #decorador añadido de manera Pythonica
def funcion_prueba():
    print("Función de prueba")


funcion_prueba()
