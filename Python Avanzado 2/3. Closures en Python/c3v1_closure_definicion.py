"""
DATO IMPORTANTE:
Scope = alcance de una variable en el código.
En Python, existen 4 tipos de scope:
1. Local: variables definidas dentro de una función.
2. Enclosing: variables definidas en una función externa a la función actual.
3. Global: variables definidas en el ámbito global del programa.
4. Built-in: variables predefinidas por Python, como `print`, `len
`, etc.
"""

# Scope global
fecha = "01-01-2000"


"""
Scope Local:
Define una variable local y la retorna. Esta variable no es accesible fuera de la función.
"""
def funcion_scope_local():
    # Scope local
    nombre = "Ana"
    return nombre

"""
Funciones Anidadas y Closures:
- Una función anidada es una función definida dentro de otra función.
- Un closure es una función anidada que recuerda el entorno en el que fue  creada, incluso si la función externa ya ha terminado de ejecutarse.  
- Los closures permiten acceder a variables de la función externa desde la función anidada.
"""

def funcion_principal():

    nombre = "Ana"
    """Definición de una función anidada dentro de la función principal."""
    def funcion_anidada():
        print(nombre)
    """Llamada a la función anidada."""
    funcion_anidada()


funcion_principal()

"""Ejemplo de Closure:
- La función `saludar` define una variable `mensaje` y una función anidada `imprimir_saludo`.
- La función `imprimir_saludo` puede acceder a la variable `mensaje` incluso después de que `saludar` haya terminado de ejecutarse.
- Al llamar a `saludar`, se retorna la función `imprimir_saludo`, que mantiene una referencia al entorno de `saludar`, permitiendo acceder a `mensaje` cuando se llama a `imprimir_saludo`.
"""
def saludar():

    mensaje = "Buen día"

    def imprimir_saludo():
        print(mensaje)

    return imprimir_saludo

"""Llamada a la función `saludar` y asignación del closure a la variable `saludo`.
Luego, se llama a `saludo`, que ejecuta `imprimir_saludo` y muestra el mensaje."""
saludo = saludar()
saludo()
