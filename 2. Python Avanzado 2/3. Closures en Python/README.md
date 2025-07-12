# Closures en Python: Funciones Anidadas

## Introducción

En Python, un **closure** es un tipo especial de función anidada que tiene acceso a variables del scope superior incluso después de que la función exterior ha finalizado su ejecución. Antes de entender en profundidad qué es un closure, es necesario comprender dos conceptos fundamentales: **scope** (ámbito) y **funciones anidadas**.

---

## ¿Qué es el Scope?

El **scope** se refiere al ámbito en el cual una variable es definida y puede ser accedida. En Python, existen principalmente dos tipos de scope:

- **Scope local:** Corresponde al contexto dentro de una función. Las variables declaradas en este nivel solo son accesibles dentro de esa función.
- **Scope global:** Es el contexto del programa principal, fuera de cualquier función. Las variables globales pueden ser accedidas desde cualquier parte del código.

```python
# Ejemplo de scope local
def scope_local():
    nombre = "Ana"
    print(nombre)  # Accesible dentro de la función

# Ejemplo de scope global
fecha = "21-06-2025"

def mostrar_fecha():
    print(fecha)  # Accede a la variable global
