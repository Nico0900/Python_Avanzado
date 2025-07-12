# Introducción a Type Hinting en Python

Antes de entender a qué nos referimos con **type hinting** en Python, es necesario conocer algunos conceptos relacionados al **tipado** de un lenguaje.

El **tipado** hace referencia a cómo son declaradas las variables dentro de un lenguaje de programación. Existen dos enfoques principales:

## Tipado Estático

En un lenguaje de **tipado estático**, los errores de tipo de datos son validados **antes de ejecutar** el código, es decir, en tiempo de compilación.  
- El tipo de dato debe ser **declarado explícitamente**.  
- Ejemplos: **Java**, **C**.

## Tipado Dinámico

En un lenguaje de **tipado dinámico**, los tipos de datos son validados **en tiempo de ejecución**.  
- No se declara el tipo de dato previamente.  
- Ejemplos: **Python**, **JavaScript**.

---

## ¿Qué es Type Hinting?

Cuando hablamos de **type hinting** en Python, nos referimos a una herramienta que permite **simular el tipado estático**, especificando de antemano el tipo de dato esperado.

### Características:

- Especificado en [PEP 484](https://peps.python.org/pep-0484/).
- Disponible desde **Python 3.5**.
- Permite declarar el tipo de variable tanto **dentro como fuera** de una función.
- Ayuda a indicar qué tipo de dato **se espera como parámetro** y qué tipo de dato **retornará** una función o método.

### Ejemplo:

```python
def suma(a: int, b: int) -> int:
    return a + b
