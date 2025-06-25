
"""son trozos de código que realizan una tarea específica y pueden ser reutilizadas en diferentes partes del programa.
pueden recibir parámetros y devolver valores.
"""
# Función
def funcion(param1, param2):
    return param1 + param2


"""
los objetos de primera clase son aquellos que pueden ser pasados como argumentos a otras funciones, ser retornados por otras funciones y asignados a variables. en Python, las funciones son objetos de primera clase.
"""
# Funciones de primera clase
def funcion_primera_clase():
    return


variable = funcion_primera_clase
variable()


"""
las funciones pueden ser asignadas a variables, pasadas como argumentos a otras funciones, donde la funciona interna recibe una función como parámetro, y pueden ser retornadas por otras funciones. (Ejemplo : Closures)
"""
# Funciones anidadas
def funcion_principal():

    nombre = "Ana"

    def funcion_anidada():
        print(nombre)

    funcion_anidada()

"""
las funciones de orden superior son aquellas que pueden recibir otras funciones como argumentos o devolver funciones como resultado. en Python, las funciones son objetos de primera clase, lo que permite crear funciones de orden superior.
"""
# Funciones de orden superior
def saludar():

    mensaje = "Buen día"

    def imprimir_saludo():
        print(mensaje)

    return imprimir_saludo
